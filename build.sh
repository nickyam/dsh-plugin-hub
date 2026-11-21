#!/usr/bin/env bash
# 一键：校验数据 → 生成页面/索引 → 构建静态站
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"

# 每个条目的「最后更新于」靠 git 历史推导（tools/entry_updated.py），产物 data/entry_updated.json 入库。
# 只在有完整历史时刷新；CI 浅克隆 / 无 .git 的场景沿用已有产物，不阻断构建。
if git rev-parse --git-dir >/dev/null 2>&1 \
   && [ "$(git rev-parse --is-shallow-repository 2>/dev/null)" != "true" ]; then
  python3 tools/entry_updated.py
else
  echo "· 无完整 git 历史，沿用 data/entry_updated.json"
fi

python3 tools/build_data.py
# --cleanDestinationDir：条目被删掉后，public/ 里对应的旧页一起清掉，不留幽灵页面
hugo --minify --cleanDestinationDir
echo "✓ 输出目录：public/"
