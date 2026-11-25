# 任务进度

## 接力进度块（WorkBuddy 2026-11-25 完成）

- **做了什么**：① 接手时发现 Forge 写入的 `data/plugins.yaml` / `data/sources.yaml` 有结构性损坏——bridge 条目错插在 `- id: dsh-claude-style` 与其字段之间、末尾多一个 YAML 文档分隔符（`---`，致 `yaml.safe_load` 直接报错），新来源 `- id:` 粘连在前一条 `tags:` 行尾且末尾缺换行；已全部修复。② 按官方 README（github.com/Totoro-qaq/dsh-plugin-bridge，MIT/main/0.5.2）把 bridge 条目从英文草稿改写为中文，修正兼容范围口径（原把 bridge 版本 0.5.2 误写成 DSH 版本）与 flag/note 的自相矛盾。③ 数据校验通过：141 插件 / 29 来源、无重复 id、字段完整、refs 0 悬空。④ `entry_updated.py` + `./build.sh` 无 ERROR，sitemap 186、新页面已生成、内链 0 死链、广告位未受影响（首页 1/详情 2/page_level_ads 0）、390px `scrollWidth===innerWidth===390`。⑤ README 统计与第 26 篇记录已回写。
- **现在到哪一步**：全部完成——验收全过，`git add` + `commit`（不 push）已做，`deploy/deploy.sh` 已上线；线上核验通过（首页/bridge 页/claude 页均 200、bridge 安装名正确、claude 页未被拆散、广告位首页 1/详情 2、Auto Ads 0）。工作区干净。
- **下一步**：仅剩用户自行在 GitHub Desktop push 本地 2 个 commit（6d8d4fc 主变更 / b8d26fc 时间戳）。任务已闭环，无需其他动作。
- **谁做的**：WorkBuddy（数据修复 / 校正 / 校验 / 构建 / 验收 / commit），前序数据写入由 Forge 完成。

## 本次工作内容
- 提取公众号文章链接：`https://mp.weixin.qq.com/s/lYkpYW-qCL6w2uGYEsAMcg`
- 补充到 `data/sources.yaml`：添加来源记录 `wx-bridge-2026-11-23`，只作发现来源标记，不新建插件条目
- 补充到 `data/plugins.yaml`：添加插件条目 `dsh-plugin-bridge`，`id: dsh-plugin-bridge`，归入 `integration` 分类，`status: community`，`repo: https://github.com/Totoro-qaq/dsh-plugin-bridge`，`install: dsh plugin --profile web add dsh-plugin-bridge`，`summary`/`features` 等字段按官方 README 提炼，`refs: [wx-bridge-2026-11-23]` 关联回来源台账

## 当前状态
- 数据写入已完成，git diff 显示 `data/plugins.yaml` +25 行，`data/sources.yaml` +9 行
- 由 Forge 完成数据层面的“补充到网站上”

## WorkBuddy 接手说明
WorkBuddy 请按以下顺序执行，`进度.md` 为唯一指引：

1. **读本文件** - 了解当前状态和未完成项
2. **按优先级执行** - 依次进行数据校验、构建产物生成、验收检查（见下文）
3. **干完活后更新本文件** - 按“做了什么 / 现在到哪一步 / 下一步 / 谁做的”格式在文件开头写进度块，跨会话接力靠这个

## 关键约束（WorkBuddy 遵守）
- **不 push**：只做 `git add` + `git commit`，随后由你在 GitHub Desktop 推
- **上线只走 `deploy/deploy.sh`**，不手 `scp`、`rsync` 到 `index/` 根
- **`data/sources.yaml` / `data/plugins.yaml`** 为唯一内容源，改动须跑脚本全覆盖
- **`public/` 不入库**，由 Hugo 生成
- **390px 无横向溢出**是移动端验收的硬门槛

## 可选工作项（WorkBuddy 按需执行）

### 1. 数据校验
- 运行 `python3 tools/entry_updated.py` 检查 `entry_updated.json`
- 确认 `data/plugins.yaml` 中 `dsh-plugin-bridge` 字段完整
- 如有缺失，补全后在 `flag` 里写说明

### 2. 构建产物生成
- 若 PyYAML 可用：运行 `./build.sh`
- 若无 PyYAML：直接 `hugo --minify --cleanDestinationDir --baseURL https://ai.limzero.com/dsh/`
- 本地预览：`mkdir -p /tmp/dsh-preview && ln -sfn "$(pwd)/public" /tmp/dsh-preview/dsh && python3 -m http.server 8765 --bind 127.0.0.1 --directory /tmp/dsh-preview`，打开 http://127.0.0.1:8765/dsh/

### 3. 验收检查
- 移动端 390px：`document.documentElement.scrollWidth === innerWidth`
- 构建日志：`./build.sh 2>&1 | grep -E "ERROR|校验通过|条目 "` 无 ERROR、条目数对得上
- sitemap：`grep -o "<loc>" public/sitemap.xml | wc -l` 应为 186

## 交接记录（工作后由 WorkBuddy 更新）
在本文件开头写进度块：
做了什么 / 现在到哪一步 / 下一步 / 谁做的

**（提示词结束，WorkBuddy 只需看此 `进度.md` 开始工作）**