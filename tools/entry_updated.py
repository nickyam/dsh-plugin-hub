#!/usr/bin/env python3
"""从 git 历史推导每个插件条目的「最后更新时间」。

为什么要单独存一份：
    详情页原来显示的「本站整理于」读的是构建时间，每次部署都变，
    等于在说「这条昨天才核对过」。真实可信的口径是 data/plugins.yaml 里
    这一条最后一次被改动是哪天，只能从 git 历史里算。

做法：
    逐个遍历改过 data/plugins.yaml 的提交，把文件按 `- id:` 切成若干块，
    每块解析成 YAML 后丢掉 refs（内部去重台账，站点不展示，改了不算内容更新），
    再和上一个提交比。变了的 id 记这个提交的时间。

产物：
    data/entry_updated.json  {"generated": "...", "entries": {"<id>": "YYYY-MM-DD"}}
    产物要入库：构建时只读它，不跑 git（ECS / CI 可能没有完整历史）。

用法：
    python3 tools/entry_updated.py
"""

import json
import re
import subprocess
from datetime import datetime
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
YAML_PATH = "data/plugins.yaml"
OUT = ROOT / "data" / "entry_updated.json"

BLOCK_RE = re.compile(r"(?m)^- id: (.+)$")
# 不参与「条目更新」判定的字段：内部台账，不进产物
IGNORED_KEYS = {"refs"}


def git(*args: str) -> str:
    return subprocess.run(
        ["git", *args], cwd=ROOT, capture_output=True, text=True, check=True
    ).stdout


def split_blocks(text: str) -> dict[str, str]:
    """把 plugins.yaml 正文切成 {id: 块内容}。"""
    marks = list(BLOCK_RE.finditer(text))
    blocks: dict[str, str] = {}
    for i, m in enumerate(marks):
        end = marks[i + 1].start() if i + 1 < len(marks) else len(text)
        blocks[m.group(1).strip()] = text[m.start():end].strip()
    return blocks


def fingerprint(body: str) -> str:
    """块的可见内容指纹：解析 YAML、丢掉内部字段、规范化序列化。"""
    try:
        data = yaml.safe_load(body) or {}
    except yaml.YAMLError:
        return body  # 解析失败就退回原文比较，宁可多报一次更新
    # 块以 "- id:" 开头，safe_load 出来是只含一个 dict 的 list
    if isinstance(data, list) and len(data) == 1:
        data = data[0]
    if isinstance(data, dict):
        data = {k: v for k, v in data.items() if k not in IGNORED_KEYS}
    return json.dumps(data, sort_keys=True, ensure_ascii=False, default=str)


def main() -> None:
    log = git("log", "--format=%H%x09%cI", "--", YAML_PATH).strip().splitlines()
    if not log:
        raise SystemExit("没有找到 data/plugins.yaml 的提交历史")

    commits = [line.split("\t") for line in log]  # 新 → 旧
    commits.reverse()  # 旧 → 新，后来居上覆盖

    updated: dict[str, str] = {}
    prev: dict[str, str] = {}

    for sha, iso in commits:
        date = iso[:10]
        try:
            text = git("show", f"{sha}:{YAML_PATH}")
        except subprocess.CalledProcessError:
            continue  # 该提交里文件不存在，跳过
        cur = {pid: fingerprint(body) for pid, body in split_blocks(text).items()}
        for pid, fp in cur.items():
            if prev.get(pid) != fp:
                updated[pid] = date
        prev = cur

    # 只保留当前仍存在的条目；历史上删掉的不写进产物
    current = split_blocks((ROOT / YAML_PATH).read_text(encoding="utf-8"))
    missing = [pid for pid in current if pid not in updated]
    if missing:
        fallback = commits[-1][1][:10]
        for pid in missing:
            updated[pid] = fallback

    kept = {pid: updated[pid] for pid in current}
    # 2026-11-27：generated 原来每次都刷新，一份时间戳就让 entry_updated.json 每次构建
    # 都变脏（进而被提交、被部署、被重传）。现在只有 entries 真变时才更新时间，
    # 内容没变就不落盘 —— 和 build_data.py 的 write_if_changed 是同一个思路。
    text_entries = dict(sorted(kept.items()))
    prev = {}
    try:
        prev = json.loads(OUT.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        prev = {}
    if prev.get("entries") == text_entries and prev.get("generated"):
        generated = prev["generated"]
    else:
        generated = datetime.now().astimezone().strftime("%Y-%m-%d %H:%M")
    payload = {"generated": generated, "entries": text_entries}
    text = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
    try:
        unchanged = OUT.read_text(encoding="utf-8") == text
    except OSError:
        unchanged = False
    if not unchanged:
        OUT.write_text(text, encoding="utf-8")

    dates = sorted(kept.values())
    print(f"条目 {len(kept)} 个（当前站点 {len(current)} 条），时间跨度 {dates[0]} ~ {dates[-1]}")
    print(f"{'写入' if not unchanged else '未变，跳过写入'} {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
