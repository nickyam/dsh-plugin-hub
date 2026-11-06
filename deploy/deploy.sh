#!/usr/bin/env bash
# ============================================================
# deploy.sh —— 把 DSH 插件图谱部署到 https://ai.limzero.com/dsh/
#
# 用法：
#   本地构建 + 同步：  bash deploy/deploy.sh
#   仅同步（已构建）：  bash deploy/deploy.sh --sync-only
#
# 【目录约定（1Panel 静态站 ai.limzero.com）】
#   宿主机：/opt/1panel/apps/openresty/openresty/www/sites/ai.limzero.com/index/dsh
#   容器内：/www/sites/ai.limzero.com/index/dsh
#   🔴 只同步 dsh/ 这一个子目录，--delete 的作用范围仅限它，不会碰主站文件。
#
# 🔴 上线前必须先在主站侧做三件事（否则会被清掉 / 广告不生效）：
#   1. ai-limzero-hub/deploy/deploy.sh 的 rsync 加 --filter='P dsh/'
#      该脚本带 --delete-excluded，不加保护规则会把整个 dsh/ 删掉。
#   2. https://ai.limzero.com/ads.txt 必须可访问（AdSense 只读域名根目录，
#      /dsh/ads.txt 无效）。内容 = 本仓库 static/ads.txt 那一行。
#   3. https://ai.limzero.com/robots.txt 加一行
#      Sitemap: https://ai.limzero.com/dsh/sitemap.xml
#      （robots.txt 同样只在主机根目录生效）
#
# 前提：证书 / DNS / vhost 已按主站配置就绪；80 端口被合规劫持，只走 HTTPS。
#       vhost 需有 try_files $uri $uri/index.html $uri/ =404，子目录下的
#       /dsh/plugins/xxx/ 才能正确落到 index.html。
# ============================================================
set -euo pipefail

DOMAIN="ai.limzero.com"
SUBDIR="dsh"
BASE_URL="https://${DOMAIN}/${SUBDIR}/"
SSH_KEY="${SSH_KEY:-$HOME/.ssh/id_aliyun}"
REMOTE_HOST="${REMOTE_HOST:-root@121.40.250.144}"
DEPLOY_DIR="/opt/1panel/apps/openresty/openresty/www/sites/${DOMAIN}/index/${SUBDIR}"

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PUBLIC_DIR="${REPO_ROOT}/public"

log() { printf '\033[36m[deploy]\033[0m %s\n' "$*"; }
die() { printf '\033[31m[deploy] ERROR:\033[0m %s\n' "$*" >&2; exit 1; }

# ---------- 1. 本地构建 ----------
if [ "${1:-}" != "--sync-only" ]; then
  log "校验数据并生成页面（tools/build_data.py）..."
  (cd "${REPO_ROOT}" && python3 tools/build_data.py)

  log "Hugo 构建（baseURL=${BASE_URL}）..."
  (cd "${REPO_ROOT}" && hugo --minify --cleanDestinationDir --baseURL "${BASE_URL}")
fi

[ -f "${PUBLIC_DIR}/index.html" ] || die "构建产物缺失：${PUBLIC_DIR}/index.html"
# 子路径部署最容易出的错：baseURL 没带 /dsh，产物里全是根路径链接
grep -q "/${SUBDIR}/css/main.css" "${PUBLIC_DIR}/index.html" \
  || die "产物里没有 /${SUBDIR}/ 前缀的资源链接，baseURL 可能不对"
log "构建完成：$(find "${PUBLIC_DIR}" -name '*.html' | wc -l | tr -d ' ') 个 HTML"

# ---------- 2. rsync 同步（仅限 dsh/ 子目录） ----------
log "同步到 ${REMOTE_HOST}:${DEPLOY_DIR}"
ssh -i "${SSH_KEY}" -o StrictHostKeyChecking=no "${REMOTE_HOST}" "mkdir -p '${DEPLOY_DIR}'"

rsync -az --delete --delete-excluded \
  -e "ssh -i ${SSH_KEY} -o StrictHostKeyChecking=no" \
  --exclude '.DS_Store' \
  --exclude '*.log' \
  "${PUBLIC_DIR}/" \
  "${REMOTE_HOST}:${DEPLOY_DIR}/"

# ---------- 3. 线上校验 ----------
log "校验线上首页..."
IP=$(ssh -i "${SSH_KEY}" -o StrictHostKeyChecking=no "${REMOTE_HOST}" \
  'curl -sS --max-time 5 ifconfig.me' 2>/dev/null | tr -d '[:space:]')
CODE=$(curl -sS -o /dev/null -w '%{http_code}' --max-time 15 \
  --resolve "${DOMAIN}:443:${IP}" "${BASE_URL}" 2>/dev/null || echo "000")
if [ "${CODE}" = "200" ]; then
  log "✅ ${BASE_URL} 返回 200"
else
  log "⚠️  ${BASE_URL} 返回 ${CODE}"
fi

log "别忘了核对：https://${DOMAIN}/ads.txt 可访问、主站 robots.txt 已声明 /${SUBDIR}/sitemap.xml"
