#!/usr/bin/env python3
"""从 GitHub 拉取每个插件仓库的 star / fork / 最后更新等公开数据。

写入 data/repo_stats.json，由 build_data.py 合并进插件数据。

限流说明：
  - 有 GITHUB_TOKEN 环境变量 → 走 /repos/{owner}/{repo}，5000 次/小时，106 个几秒跑完
  - 无 token → 走 search API（匿名 10 次/分钟），串行 + 6.5s 间隔，约 12 分钟跑完
  - 两者都会命中本地缓存，默认 7 天内不重复拉

用法：
    python3 tools/fetch_repo_stats.py              # 增量刷新（7 天过期）
    python3 tools/fetch_repo_stats.py --all        # 全部重刷
    python3 tools/fetch_repo_stats.py --only a/b   # 只刷某一个
    GITHUB_TOKEN=xxx python3 tools/fetch_repo_stats.py --all
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
PLUGINS = ROOT / "data" / "plugins.yaml"
STATS = ROOT / "data" / "repo_stats.json"

UA = "dsh-plugin-hub/1.0 (+https://ai.limzero.com/dsh/)"
TOKEN = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
FRESH_DAYS = 7


def strip_env_proxy() -> None:
    """本机 Bash 会注入 HTTP(S)_PROXY 指向本地代理，偶发不通，直连更稳。"""
    for k in ("HTTP_PROXY", "HTTPS_PROXY", "http_proxy", "https_proxy",
              "ALL_PROXY", "all_proxy"):
        os.environ.pop(k, None)


def api_get(url: str) -> tuple[int, dict | None]:
    req = urllib.request.Request(url, headers={
        "User-Agent": UA,
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    })
    if TOKEN:
        req.add_header("Authorization", f"Bearer {TOKEN}")
    # macOS 上 urllib 会读系统代理配置（_scproxy），本机代理偶发 TLS 失败 —— 强制直连
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    try:
        with opener.open(req, timeout=25) as r:
            return r.status, json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = None
        try:
            body = json.loads(e.read().decode("utf-8"))
        except Exception:
            pass
        return e.code, body
    except Exception as e:  # 网络层失败
        return 0, {"_error": str(e)}


def shape(item: dict) -> dict:
    lic = item.get("license") or {}
    return {
        "full_name": item.get("full_name"),
        "stars": item.get("stargazers_count"),
        "forks": item.get("forks_count"),
        "issues": item.get("open_issues_count"),
        "watchers": item.get("subscribers_count"),
        "language": item.get("language"),
        "license": lic.get("spdx_id") or (lic.get("name") if lic else None),
        "pushed_at": item.get("pushed_at"),
        "created_at": item.get("created_at"),
        "archived": bool(item.get("archived")),
        "description": (item.get("description") or "").strip() or None,
        "html_url": item.get("html_url"),
        "fetched_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }


def fetch_one(slug: str, core_ok: bool = True) -> tuple[dict | None, str]:
    """返回 (stats, 说明)。slug 形如 owner/repo。

    无 token 时两条腿走路：先试 core API（匿名 60 次/小时，最准），用完再退到
    search API（匿名 10 次/分钟，一次请求也能拿到完整 repo 对象）。
    """
    if core_ok:
        code, data = api_get(f"https://api.github.com/repos/{slug}")
        if code == 200 and data:
            return shape(data), "core"
        if code == 404:
            return None, "404"
        if code in (403, 429):
            return None, "core限流"
        if code != 0:
            return None, f"HTTP {code}"

    # search API：匿名 10 次/分钟
    code, data = api_get(
        "https://api.github.com/search/repositories?q="
        + urllib.parse.quote(f"repo:{slug}", safe=":/")
    )
    if code == 200 and data and data.get("items"):
        item = data["items"][0]
        if (item.get("full_name") or "").lower() == slug.lower():
            return shape(item), "search"
        return None, "名字不匹配"
    if code == 200:
        return None, "404"
    if code in (403, 429):
        return None, "限流"
    return None, f"HTTP {code}"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--all", action="store_true", help="忽略缓存，全部重拉")
    ap.add_argument("--only", help="只刷 owner/repo")
    ap.add_argument("--max-age", type=int, default=FRESH_DAYS)
    args = ap.parse_args()

    strip_env_proxy()

    raw = yaml.safe_load(PLUGINS.read_text(encoding="utf-8"))
    items = raw["plugins"] if isinstance(raw, dict) and "plugins" in raw else raw

    slugs: list[str] = []
    for it in items:
        repo = (it.get("repo") or "").strip().rstrip("/")
        if repo.startswith("https://github.com/"):
            slug = repo[len("https://github.com/"):]
            slug = "/".join(slug.split("/")[:2])
            if slug and slug not in slugs:
                slugs.append(slug)

    cache: dict[str, dict] = {}
    if STATS.exists():
        try:
            old = json.loads(STATS.read_text(encoding="utf-8"))
            cache = old.get("repos", {}) if isinstance(old, dict) else {}
        except Exception:
            cache = {}

    now = time.time()
    queue: list[str] = []
    for slug in slugs:
        if args.only and slug != args.only:
            continue
        if not args.all and slug in cache:
            try:
                ts = datetime.strptime(
                    cache[slug].get("fetched_at", ""), "%Y-%m-%dT%H:%M:%SZ"
                ).replace(tzinfo=timezone.utc).timestamp()
                if now - ts < args.max_age * 86400:
                    continue
            except Exception:
                pass
        queue.append(slug)

    total = len(queue)
    if not total:
        print(f"✓ 全部 {len(slugs)} 个仓库都在 {args.max_age} 天缓存内，无需请求")
        return 0

    mode = "core API（有 token）" if TOKEN else "search API（匿名，10 次/分钟）"
    print(f"→ 待拉取 {total} / {len(slugs)} 个仓库，走 {mode}")

    ok = fail = 0
    failed: list[str] = []
    core_ok = True  # 无 token 也先试 core，用完 60 次再退 search

    def pace(how: str) -> None:
        """core 接口宽松，search 接口 10 次/分钟。"""
        time.sleep(0.4 if how == "core" else 6.5)

    for i, slug in enumerate(queue, 1):
        stats, how = fetch_one(slug, core_ok)
        if how == "core限流":
            core_ok = False
            print("  · core 匿名额度（60/小时）已用完，转 search API（10 次/分钟）")
            stats, how = fetch_one(slug, False)

        if stats:
            cache[slug] = stats
            ok += 1
            print(f"  [{i}/{total}] ✓ {slug:44} ★{stats['stars']}  ⑂{stats['forks']}  ({how})")
            pace(how)
            continue

        if how == "限流":
            # 撞到 search API 的 10 次/分钟上限，等 60 秒再来一次
            print(f"  [{i}/{total}] … {slug} 撞 search 限流，等 60s")
            time.sleep(60)
            stats, how = fetch_one(slug, core_ok)
            if stats:
                cache[slug] = stats
                ok += 1
                print(f"  [{i}/{total}] ✓ {slug:44} ★{stats['stars']}  ({how})")
                pace(how)
                continue

        fail += 1
        failed.append(f"{slug} ({how})")
        print(f"  [{i}/{total}] ✗ {slug:44} {how}")
        pace("core" if core_ok else "search")

    payload = {
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "source": "GitHub REST API" + ("（已鉴权）" if TOKEN else "（匿名）"),
        "repos": dict(sorted(cache.items())),
    }
    STATS.parent.mkdir(parents=True, exist_ok=True)
    STATS.write_text(
        json.dumps(payload, ensure_ascii=False, indent=1) + "\n", encoding="utf-8"
    )

    print(f"\n✓ 完成：成功 {ok}，失败 {fail}，缓存共 {len(cache)} 个仓库")
    if failed:
        print("  未拿到：")
        for f in failed:
            print("   -", f)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
