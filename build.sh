#!/usr/bin/env bash
# 一键：校验数据 → 生成页面/索引 → 构建静态站
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"
python3 tools/build_data.py
# --cleanDestinationDir：条目被删掉后，public/ 里对应的旧页一起清掉，不留幽灵页面
hugo --minify --cleanDestinationDir
echo "✓ 输出目录：public/"
