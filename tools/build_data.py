#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DSH 插件图谱 · 内容生成

data/sources.yaml + data/plugins.yaml + data/discrepancies.yaml + data/categories.yaml
        ↓ 校验 / 去重 / 计算印证
content/plugins/*.md、content/sources/*.md、static/search.json、data/derived.json

用法：python3 tools/build_data.py
只依赖 Python 标准库 + PyYAML。content/plugins/ 与 content/sources/ 由本脚本全权管理，请勿手改。
"""
import json
import sys
from datetime import datetime
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
REQUIRED_PLUGIN = ("id", "name", "category", "status", "summary", "mentions")


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
    discrepancies = load("discrepancies.yaml")

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
        for m in p.get("mentions") or []:
            if m.get("source") not in source_map:
                errors.append(f"插件 {p.get('id')} 引用了不存在的来源：{m.get('source')}")
            if m.get("stance") not in VALID_STANCE:
                errors.append(f"插件 {p.get('id')} 的 stance 不合法：{m.get('stance')}")
            if not m.get("quote"):
                errors.append(f"插件 {p.get('id')} 有一条证据没有引文")

    for d in discrepancies:
        for side in d.get("sides") or []:
            if side.get("source") not in source_map:
                errors.append(f"口径核对 {d.get('id')} 引用了不存在的来源：{side.get('source')}")

    # 别名撞车检查：只警告，不阻断（撞车往往正是需要人工合并的信号）
    warnings = []
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
    total_mentions = 0
    for p in plugins:
        seen, mentions = set(), []
        for m in p["mentions"]:
            src = source_map[m["source"]]
            mention = dict(m)
            mention["source_title"] = src["title"]
            mention["source_url"] = src["url"]
            mention["source_kind_label"] = KIND_LABEL[src["kind"]]
            mention["source_publisher"] = src["publisher"]
            mentions.append(mention)
            seen.add(m["source"])
        p["mentions"] = mentions
        total_mentions += len(mentions)

        p["source_count"] = len(seen)
        p["has_conflict"] = any(m["stance"] == "有出入" for m in mentions)
        if p["has_conflict"]:
            p["agreement"] = "口径有出入"
        elif p["source_count"] >= 2:
            p["agreement"] = "多篇印证"
        else:
            p["agreement"] = "单篇提及"
        p["confidence"] = "高" if p["source_count"] >= 3 else ("中" if p["source_count"] == 2 else "待核实")
        p["category_label"] = cat_map[p["category"]]
        p["status_label"] = STATUS_LABEL[p["status"]]
        p["weight"] = p["source_count"] * 100 + (20 if p["has_conflict"] else 0)
        p["url"] = f"/plugins/{p['id']}/"

    # ── 生成插件页 ──────────────────────────────────────────────
    pdir, sdir = CONTENT / "plugins", CONTENT / "sources"
    pdir.mkdir(parents=True, exist_ok=True)
    sdir.mkdir(parents=True, exist_ok=True)
    for d in (pdir, sdir):
        for old in d.glob("*.md"):
            old.unlink()

    write_front_matter(
        pdir / "_index.md",
        {"title": "插件库", "description": "按证据链整理的 DSH 插件条目"},
        "全部插件条目。每条都挂了来源引文，多篇说法不一致的会单独标出。",
    )
    for p in plugins:
        front = {
            "title": p["name"],
            "description": p["summary"],
            "categories": [p["category"]],
            "tags": p.get("tags") or [],
            "weight": p["weight"],
            "params": {"plugin": p, "generated": True},
        }
        write_front_matter(pdir / f"{p['id']}.md", front, p["summary"])

    # ── 生成来源页 ──────────────────────────────────────────────
    write_front_matter(
        sdir / "_index.md",
        {"title": "来源台账", "description": "本站读过的每一篇文章"},
        "每一条来源都有独立页面，列出它提到过的插件。",
    )
    for s in sources:
        mentioned = [
            {"id": p["id"], "name": p["name"], "agreement": p["agreement"]}
            for p in plugins
            if any(m["source"] == s["id"] for m in p["mentions"])
        ]
        payload = dict(s)
        payload["kind_label"] = KIND_LABEL[s["kind"]]
        payload["mentioned"] = mentioned
        payload["mentioned_count"] = len(mentioned)
        front = {
            "title": s["title"],
            "description": s.get("note", ""),
            "params": {"source": payload, "generated": True},
        }
        write_front_matter(sdir / f"{s['id']}.md", front, s.get("note") or "")

    # ── 搜索索引 ────────────────────────────────────────────────
    index = [
        {
            "id": p["id"],
            "name": p["name"],
            "aliases": p.get("aliases") or [],
            "category": p["category"],
            "category_label": p["category_label"],
            "summary": p["summary"],
            "tags": p.get("tags") or [],
            "status_label": p["status_label"],
            "agreement": p["agreement"],
            "source_count": p["source_count"],
            "flag": p.get("flag", ""),
            "url": p["url"],
        }
        for p in sorted(plugins, key=lambda x: -x["weight"])
    ]
    (STATIC / "search.json").write_text(
        json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    # ── 派生统计 ────────────────────────────────────────────────
    derived = {
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "stats": {
            "plugins": len(plugins),
            "sources": len(sources),
            "wechat": sum(1 for s in sources if s["kind"] == "wechat"),
            "mentions": total_mentions,
            "corroborated": sum(1 for p in plugins if p["source_count"] >= 2),
            "conflicts": sum(1 for p in plugins if p["has_conflict"]),
            "discrepancies": len(discrepancies),
            "categories": len(categories),
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
        "source_map": {
            s["id"]: {
                "title": s["title"],
                "url": s["url"],
                "publisher": s["publisher"],
                "kind_label": KIND_LABEL[s["kind"]],
            }
            for s in sources
        },
        "source_kind_label": KIND_LABEL,
        "status_label": STATUS_LABEL,
        "stance_label": STANCE_LABEL,
    }
    (DATA / "derived.json").write_text(
        json.dumps(derived, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    print(f"✓ 校验通过：{len(plugins)} 个插件 / {len(sources)} 条来源 / {total_mentions} 条证据")
    print(f"  多篇印证 {derived['stats']['corroborated']} · 口径有出入 {derived['stats']['conflicts']} · 待核对 {derived['stats']['discrepancies']}")
    if warnings:
        print(f"  ⚠ 别名提示 {len(warnings)} 条：")
        for w in warnings[:10]:
            print("    - " + w)


if __name__ == "__main__":
    main()
