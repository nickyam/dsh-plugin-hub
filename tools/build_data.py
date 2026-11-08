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
    total_refs = 0
    for p in plugins:
        # 参考来源（发现来源）：优先 refs，否则从旧 mentions 的 source 推导
        seen, refs = set(), []
        for r in (p.get("refs") or [m.get("source") for m in p.get("mentions") or []]):
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

        p["source_count"] = len(seen)
        p["repo_confirmed"] = bool(p.get("repo"))
        p["category_label"] = cat_map[p["category"]]
        p["status_label"] = STATUS_LABEL[p["status"]]
        # 已确认官方仓库的排前面，其次参考文章多的排前面
        p["weight"] = (1000 if p["repo_confirmed"] else 0) + p["source_count"] * 10
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
        {"title": "插件库", "description": "按官方仓库整理的 DSH 插件条目"},
        "全部插件条目。每条都链到官方 GitHub 仓库，简介、安装与功能亮点以 README 为准；公众号与社区文章仅作发现来源参考。",
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
        {"title": "来源台账", "description": "本站发现插件所参考的文章与目录"},
        "每一条来源都有独立页面，列出本站从它发现 / 参考过的插件。",
    )
    for s in sources:
        mentioned = [
            {"id": p["id"], "name": p["name"], "repo_confirmed": p["repo_confirmed"]}
            for p in plugins
            if s["id"] in [r["id"] for r in p["refs"]]
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
            "repo_confirmed": p["repo_confirmed"],
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
            "refs_total": total_refs,
            "repos_confirmed": sum(1 for p in plugins if p["repo_confirmed"]),
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
    }
    (DATA / "derived.json").write_text(
        json.dumps(derived, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    print(f"✓ 校验通过：{len(plugins)} 个插件 / {len(sources)} 条来源 / {total_refs} 条参考")
    print(f"  已确认官方仓库 {derived['stats']['repos_confirmed']} · 参考文章 {derived['stats']['refs_total']} 条")
    if warnings:
        print(f"  ⚠ 提示 {len(warnings)} 条：")
        for w in warnings[:10]:
            print("    - " + w)


if __name__ == "__main__":
    main()
