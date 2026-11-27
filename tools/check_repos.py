#!/usr/bin/env python3
"""巡检 data/plugins.yaml 里每个插件仓库是否还在原地。

为什么要单独有这个脚本：GitHub 上的仓库会改名、会迁移 owner、会被删。站内
`repo` 一旦指到旧地址，浏览器还能靠 301 跳过去，但卡片上的规范地址是错的，
`install: ... github:old/name` 也会跟着跳；而抓取脚本只在「拉数据失败」时
才偶然暴露，不做专项检查根本发现不了。

判据（对 https://github.com/<owner>/<repo> 发 HEAD，不跟随重定向）：
  200            → 正常
  301 / 302      → 改名或迁移，Location 里有新地址
  404            → 已删除或转为私有
  其它 / 网络错   → 记一笔，人工看

用法：
    python3 tools/check_repos.py            # 只报告，不改文件
    python3 tools/check_repos.py --json x   # 额外写一份 JSON 报告

注意：走的是 github.com 网页端而不是 api.github.com，不消耗 API 额度
（匿名 API 只有 60 次/小时，141 个仓库不够用）。
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
PLUGINS = ROOT / "data" / "plugins.yaml"
UA = "dsh-plugin-hub-repo-check/1.0 (+https://ai.limzero.com/dsh/)"


def strip_env_proxy() -> None:
    """本机 Bash 注入的本地代理偶发不通，直连更稳（同 fetch_repo_stats.py）。"""
    for k in ("HTTP_PROXY", "HTTPS_PROXY", "http_proxy", "https_proxy",
              "ALL_PROXY", "all_proxy"):
        os.environ.pop(k, None)


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):  # noqa: D401
        return None  # 让 3xx 直接以 HTTPError 抛出，好拿到 Location


OPENER = urllib.request.build_opener(urllib.request.ProxyHandler({}), NoRedirect())


def probe(slug: str) -> tuple[str, str]:
    """返回 (状态, 说明)。状态取 ok / renamed / gone / error。"""
    url = f"https://github.com/{slug}"
    req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": UA})
    try:
        with OPENER.open(req, timeout=20) as r:
            return ("ok", "") if r.status == 200 else ("error", f"HTTP {r.status}")
    except urllib.error.HTTPError as e:
        if e.code in (301, 302, 307, 308):
            loc = (e.headers.get("Location") or "").rstrip("/")
            new = loc.split("github.com/", 1)[-1] if "github.com/" in loc else loc
            return "renamed", new
        if e.code == 404:
            return "gone", "404"
        return "error", f"HTTP {e.code}"
    except Exception as e:  # 网络层
        return "error", str(e)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", help="把结果另存为 JSON")
    ap.add_argument("--delay", type=float, default=0.4, help="每次请求间隔秒数")
    args = ap.parse_args()

    strip_env_proxy()

    raw = yaml.safe_load(PLUGINS.read_text(encoding="utf-8"))
    items = raw["plugins"] if isinstance(raw, dict) and "plugins" in raw else raw

    seen: dict[str, list[str]] = {}
    for it in items:
        repo = (it.get("repo") or "").strip().rstrip("/")
        if not repo.startswith("https://github.com/"):
            continue  # 非 GitHub 仓库（gitcode 等）不在此脚本职责内
        slug = "/".join(repo[len("https://github.com/"):].split("/")[:2])
        seen.setdefault(slug, []).append(it.get("id") or "?")

    print(f"→ 巡检 {len(seen)} 个 GitHub 仓库（{len(items)} 条插件）")
    problems: list[dict] = []
    for i, (slug, ids) in enumerate(sorted(seen.items()), 1):
        state, info = probe(slug)
        if state == "ok":
            print(f"  [{i}/{len(seen)}] ✓ {slug}")
        else:
            label = {"renamed": "改名", "gone": "已删除", "error": "异常"}[state]
            print(f"  [{i}/{len(seen)}] ✗ {slug} → {label} {info}")
            problems.append({"slug": slug, "state": state, "detail": info, "ids": ids})
        time.sleep(args.delay)

    print(f"\n结论：{len(seen) - len(problems)} 个正常，{len(problems)} 个要处理")
    for p in problems:
        ids = ", ".join(p["ids"])
        if p["state"] == "renamed":
            print(f"  - {p['slug']} → {p['detail']}（{ids}）")
        elif p["state"] == "gone":
            print(f"  - {p['slug']} 已 404，条目该删或换仓库（{ids}）")
        else:
            print(f"  - {p['slug']} 探测异常：{p['detail']}（{ids}）")

    if args.json:
        Path(args.json).write_text(
            json.dumps({"checked": len(seen), "problems": problems},
                       ensure_ascii=False, indent=1) + "\n",
            encoding="utf-8",
        )
        print(f"  报告已写入 {args.json}")

    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
