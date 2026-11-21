#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DSH 插件图谱 · 内容生成

data/sources.yaml + data/plugins.yaml + data/categories.yaml
        ↓ 校验 / 去重 / 计算仓库确认数
content/plugins/*.md、content/sources/*.md、static/search.json、data/derived.json

用法：python3 tools/build_data.py
只依赖 Python 标准库 + PyYAML。content/plugins/ 与 content/sources/ 由本脚本全权管理，请勿手改。

内容来源：每个插件以官方 GitHub 仓库（repo）为准，简介/安装/功能亮点均依据 README 整理；
公众号与社区文章仅作为「发现来源 / 参考」（refs），不渲染原文、不作为正文。
只收能核实到官方仓库的插件：缺 repo 直接报错，不留「待确认」占位条目。
"""
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("缺少 PyYAML：pip3 install pyyaml")

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
CONTENT = ROOT / "content"
STATIC = ROOT / "static"

KIND_LABEL = {
    "wechat": "公众号",
    "official": "官方文档",
    "encyclopedia": "百科",
    "media": "第三方媒体",
    "catalog": "目录站",
    "guide": "教程 / 指南",
}
STATUS_LABEL = {
    "official": "官方",
    "community": "社区",
    "unknown": "原文未说明",
}
STANCE_LABEL = {
    "印证": "印证",
    "补充": "补充",
    "仅提及": "仅提及",
    "有出入": "有出入",
}
VALID_STANCE = set(STANCE_LABEL)
REQUIRED_PLUGIN = ("id", "name", "category", "status", "summary")


def load(name):
    path = DATA / name
    if not path.exists():
        sys.exit(f"缺少数据文件：{path}")
    with path.open(encoding="utf-8") as f:
        return yaml.safe_load(f) or []


def dump_yaml(obj):
    return yaml.safe_dump(
        obj, allow_unicode=True, sort_keys=False, default_flow_style=False, width=10000
    )


def write_front_matter(path, front, body):
    text = "---\n" + dump_yaml(front) + "---\n\n" + body.strip() + "\n"
    path.write_text(text, encoding="utf-8")


def main():
    sources = load("sources.yaml")
    categories = load("categories.yaml")
    plugins = load("plugins.yaml")

    errors = []
    source_ids = [s.get("id") for s in sources]
    source_map = {s["id"]: s for s in sources if s.get("id")}
    if len(source_ids) != len(set(source_ids)):
        errors.append("sources.yaml 里有重复的 id")
    for s in sources:
        for key in ("id", "title", "kind", "publisher", "url"):
            if not s.get(key):
                errors.append(f"来源 {s.get('id')} 缺字段 {key}")
        if s.get("kind") not in KIND_LABEL:
            errors.append(f"来源 {s.get('id')} 的 kind 不合法：{s.get('kind')}")

    cat_ids = [c["id"] for c in categories]
    cat_map = {c["id"]: c["label"] for c in categories}
    if len(cat_ids) != len(set(cat_ids)):
        errors.append("categories.yaml 里有重复的 id")
    if "builtin" in cat_ids:
        errors.append("categories.yaml 不应含 builtin：官方内置能力开箱即用，本站不展示")

    plugin_ids = [p.get("id") for p in plugins]
    if len(plugin_ids) != len(set(plugin_ids)):
        errors.append("plugins.yaml 里有重复的 id")
    warnings = []
    for p in plugins:
        for key in REQUIRED_PLUGIN:
            if not p.get(key):
                errors.append(f"插件 {p.get('id')} 缺字段 {key}")
        if p.get("status") == "builtin" or p.get("category") == "builtin":
            errors.append(
                f"插件 {p.get('id')} 是官方内置能力：本站只收需要额外安装的插件，请勿建条目"
            )
        if p.get("category") not in cat_ids:
            errors.append(f"插件 {p.get('id')} 的分类不存在：{p.get('category')}")
        if p.get("status") not in STATUS_LABEL:
            errors.append(f"插件 {p.get('id')} 的 status 不合法：{p.get('status')}")
        # refs（参考来源）：优先用 refs 列表，否则从旧 mentions 的 source 字段推导；
        # 公众号等文章只作为发现来源，不要求原文引文。
        refs = p.get("refs") or [m.get("source") for m in p.get("mentions") or []]
        for r in refs:
            if r not in source_map:
                errors.append(f"插件 {p.get('id')} 引用了不存在的来源：{r}")
        if not p.get("repo"):
            errors.append(
                f"插件 {p.get('id')} 缺少 repo：本站只收已确认官方仓库的插件，"
                "找不到可信仓库就不要建条目（不要留空占位）"
            )

    # 别名撞车检查：只警告，不阻断（撞车往往正是需要人工合并的信号）
    names = {}
    for p in plugins:
        for key in [p["name"]] + (p.get("aliases") or []):
            k = key.strip().lower()
            if k in names and names[k] != p["id"]:
                warnings.append(f"别名「{key}」同时出现在 {names[k]} 与 {p['id']}")
            names[k] = p["id"]

    if errors:
        print("数据校验未通过：", file=sys.stderr)
        for e in errors:
            print("  ✗ " + e, file=sys.stderr)
        sys.exit(1)

    # ── 派生字段 ────────────────────────────────────────────────
    # GitHub 仓库数据（star / fork / 最后更新）：由 tools/fetch_repo_stats.py 抓取，
    # 缓存进 data/repo_stats.json。没抓到就是 None，页面上按「暂无」处理，不编造。
    repo_stats, repo_stats_at = {}, ""
    stats_path = DATA / "repo_stats.json"
    if stats_path.exists():
        try:
            _rs = json.loads(stats_path.read_text(encoding="utf-8"))
            repo_stats = _rs.get("repos", {}) or {}
            repo_stats_at = _rs.get("generated_at", "")
        except Exception as exc:
            print(f"⚠ data/repo_stats.json 解析失败，跳过 GitHub 数据：{exc}", file=sys.stderr)

    # 条目最后更新时间：由 tools/entry_updated.py 从 git 历史推导（改了这条才记这天），
    # 构建只读产物，不跑 git。用来替代原来的「本站整理于 <构建时间>」——那个每次部署都变。
    entry_updated, entry_updated_at = {}, ""
    eu_path = DATA / "entry_updated.json"
    if eu_path.exists():
        try:
            _eu = json.loads(eu_path.read_text(encoding="utf-8"))
            entry_updated = _eu.get("entries", {}) or {}
            entry_updated_at = _eu.get("generated", "")
        except Exception as exc:
            print(f"⚠ data/entry_updated.json 解析失败，跳过条目更新时间：{exc}", file=sys.stderr)

    GH_KEYS = ("stars", "forks", "issues", "language", "license", "pushed_at", "archived")

    def human(n):
        """星标 / Fork 缩写：上万才用 k（12.9k），一万以下给原数，比「1k」诚实。"""
        if n is None:
            return None
        if n >= 10000:
            return f"{n / 1000:.1f}k"
        return str(n)

    def _median(nums):
        vals = sorted(nums)
        if not vals:
            return None
        mid = len(vals) // 2
        return vals[mid] if len(vals) % 2 else round((vals[mid - 1] + vals[mid]) / 2)

    def updated_label(pushed_at):
        """把 pushed_at 换成「N 天前更新」。只描述仓库最近提交，不冒充本站核对时间。"""
        if not pushed_at:
            return None, None
        try:
            ts = datetime.strptime(pushed_at[:19], "%Y-%m-%dT%H:%M:%S")
        except ValueError:
            return None, None
        days = max((datetime.now(timezone.utc).replace(tzinfo=None) - ts).days, 0)
        if days == 0:
            label = "今天有提交"
        elif days == 1:
            label = "昨天有提交"
        elif days < 30:
            label = f"{days} 天前有提交"
        elif days < 365:
            label = f"{days // 30} 个月前有提交"
        else:
            label = f"{days // 365} 年前有提交"
        return label, days

    total_refs = 0
    for p in plugins:
        # 参考来源（发现来源）：优先 refs，否则从旧 mentions 的 source 推导
        raw_refs = p.get("refs") or [m.get("source") for m in p.get("mentions") or []]
        seen, refs = set(), []
        for r in raw_refs:
            if r and r not in seen:
                seen.add(r)
                refs.append(
                    {
                        "id": r,
                        "title": source_map[r]["title"],
                        "url": source_map[r]["url"],
                        "kind_label": KIND_LABEL[source_map[r]["kind"]],
                        "publisher": source_map[r]["publisher"],
                    }
                )
        p["refs"] = refs
        total_refs += len(refs)

        # refs 去重后如果比原文短，说明 yaml 里有重复行（不影响产物，但台账会虚高）
        if len(raw_refs) != len(seen):
            warnings.append(
                f"插件 {p.get('id')} 的 refs 有 {len(raw_refs) - len(seen)} 条重复，已自动去重"
            )

        p["source_count"] = len(seen)
        p["repo_confirmed"] = bool(p.get("repo"))

        # GitHub 公开数据：只留展示需要的字段，别把整包元数据塞进 HTML
        slug = ""
        repo = p.get("repo") or ""
        if repo.startswith("https://github.com/"):
            slug = "/".join(repo[len("https://github.com/"):].strip("/").split("/")[:2])
        raw = repo_stats.get(slug) or {}
        gh = {k: raw.get(k) for k in GH_KEYS if raw.get(k) is not None}
        if gh:
            gh["slug"] = slug
            gh["stars_label"] = human(gh.get("stars"))
            gh["forks_label"] = human(gh.get("forks"))
            if gh.get("pushed_at"):
                gh["pushed_date"] = gh["pushed_at"][:10]
                label, days = updated_label(gh["pushed_at"])
                if label:
                    # 卡片上替代「社区 / 官方」这类恒定徽章：更新活跃度才是真信号
                    gh["updated_label"] = label
                    gh["updated_days"] = days
                    gh["stale"] = days > 180
        p["gh"] = gh or None
        # 条目本身最近一次被改动是哪天（不含 refs 这类内部台账）
        p["entry_updated"] = entry_updated.get(p["id"])
        p["category_label"] = cat_map[p["category"]]
        p["status_label"] = STATUS_LABEL[p["status"]]
        # 已确认官方仓库的排前面，其次参考文章多的排前面
        p["weight"] = (1000 if p["repo_confirmed"] else 0) + p["source_count"] * 10
        p["url"] = f"/plugins/{p['id']}/"

    # ── 生成插件页 ──────────────────────────────────────────────
    # 来源台账（data/sources.yaml）只作仓库内部记录：校验 refs 完整性用，
    # 2026-11-18 起站点不再生成来源页、也不在页面上展示任何来源信息。
    sdir = CONTENT / "sources"
    if sdir.exists():
        for old in sdir.glob("*.md"):
            old.unlink()
        try:
            sdir.rmdir()
        except OSError:
            pass

    pdir = CONTENT / "plugins"
    pdir.mkdir(parents=True, exist_ok=True)
    for old in pdir.glob("*.md"):
        old.unlink()

    write_front_matter(
        pdir / "_index.md",
        {"title": "插件库", "description": "按官方仓库整理的 DSH 插件条目"},
        "全部插件条目。每条都链到官方 GitHub 仓库，简介、安装与功能亮点以 README 为准。",
    )
    for p in plugins:
        # refs / source_count 只用于内部台账与排序，不进产物（站点不展示任何来源信息）
        payload = {k: v for k, v in p.items() if k not in ("refs", "source_count")}
        front = {
            "title": p["name"],
            "description": p["summary"],
            "categories": [p["category"]],
            "tags": p.get("tags") or [],
            "weight": p["weight"],
            "params": {"plugin": payload, "generated": True},
        }
        write_front_matter(pdir / f"{p['id']}.md", front, p["summary"])

    # ── 搜索索引 ────────────────────────────────────────────────
    # 2026-11-21：这份索引过去生成了却没人读（首页搜索走 DOM 的 data-hay）。
    # 现在给 baseof 的搜索浮层用，字段要覆盖「用户可能怎么描述它」：
    # 名字 / 别名 / 简介 / 标签 / 功能亮点 / 备注 / 安装命令。
    index = [
        {
            "id": p["id"],
            "name": p["name"],
            "aliases": p.get("aliases") or [],
            "category": p["category"],
            "category_label": p["category_label"],
            "summary": p["summary"],
            "tags": p.get("tags") or [],
            "features": p.get("features") or [],
            # notes 通常一两百字，进搜索只为覆盖「剪贴板 / WebDAV」这类只在备注里出现的词，截断够用
            "notes": (p.get("notes") or "")[:160],
            "install": p.get("install") or "",
            "status_label": p["status_label"],
            "repo_confirmed": p["repo_confirmed"],
            "stars": (p["gh"] or {}).get("stars"),
            "stars_label": (p["gh"] or {}).get("stars_label"),
            "updated_label": (p["gh"] or {}).get("updated_label"),
            "url": p["url"],
        }
        for p in sorted(plugins, key=lambda x: -x["weight"])
    ]
    (STATIC / "search.json").write_text(
        json.dumps(index, ensure_ascii=False, separators=(",", ":")), encoding="utf-8"
    )

    # ── 派生统计 ────────────────────────────────────────────────
    # 🔴 2026-11-18 用户决定：站点不再有「来源」板块。
    # derived.json 会随站点发布，所以这里绝不能带任何来源标题 / 链接 / 计数。
    derived = {
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "generated_date": datetime.now().strftime("%Y-%m-%d"),
        "stats": {
            "plugins": len(plugins),
            "repos_confirmed": sum(1 for p in plugins if p["repo_confirmed"]),
            "categories": len(categories),
            # 星标只做「中位数」不做合计：合计会被 DSH 本体仓库（28 万星）和几个大项目拉偏，
            # 中位数才代表「典型插件大概多少星」，也不会误导成插件生态总量。
            "stars_median": _median(
                [p["gh"]["stars"] for p in plugins if p["gh"] and p["gh"].get("stars") is not None]
            ),
            "stars_median_label": human(
                _median(
                    [p["gh"]["stars"] for p in plugins if p["gh"] and p["gh"].get("stars") is not None]
                )
            ),
            "gh_synced": sum(1 for p in plugins if p["gh"]),
            "gh_synced_at": repo_stats_at,
        },
        "categories": [
            {
                "id": c["id"],
                "label": c["label"],
                "desc": c["desc"],
                "count": sum(1 for p in plugins if p["category"] == c["id"]),
            }
            for c in categories
        ],
        "category_map": cat_map,
        "status_label": STATUS_LABEL,
    }
    (DATA / "derived.json").write_text(
        json.dumps(derived, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    print(f"✓ 校验通过：{len(plugins)} 个插件 / {len(categories)} 个分类")
    print(f"  已确认官方仓库 {derived['stats']['repos_confirmed']}")
    print(f"  台账（不上站）：{len(sources)} 条来源 / {total_refs} 条参考，仅用于 refs 完整性校验")
    if warnings:
        print(f"  ⚠ 提示 {len(warnings)} 条：")
        for w in warnings[:10]:
            print("    - " + w)


if __name__ == "__main__":
    main()
