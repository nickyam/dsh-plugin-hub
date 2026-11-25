# AGENTS.md

给 AI 协作者（以及隔了三个月回来的自己）的执行说明。

**产品定位、收录硬规则、部署细节、为什么这么设计，全在 `README.md`。这里不重复，只写三件事：动手前该知道的边界、已经踩过的坑、收工前怎么验。两边冲突时以 `README.md` 为准。**

`docs/2026-11-21-optimization-retro.md` 是**测量方法与口径复盘**：改前改后的实测数字、390px 溢出探针、无头 Chrome 屏蔽广告截图、内链扫描脚本、AdSense 站点级规则。要做「全站体检」或判断某处要不要改回去，先读它。

## 环境

- `hugo v0.166.0+extended`（CI / CF Pages 也锁这版，别升）
- `python3` + `PyYAML`（`tools/build_data.py` 依赖）
- 构建**不需要联网**：只读 `data/repo_stats.json` 与 `data/entry_updated.json` 两个快照

## 命令

```bash
./build.sh                                  # entry_updated → build_data → hugo
bash deploy/deploy.sh                       # 构建 + rsync + 线上校验（本机唯一上线路径）
bash deploy/deploy.sh --sync-only           # 产物已构建，只同步
python3 tools/fetch_repo_stats.py [--all]   # 刷 GitHub 快照，需联网
```

本地预览见 README「快速开始」（`baseURL "/"` + 子目录挂载，别直接开 `public/index.html`）。

## 文件边界

| 文件 | 规则 |
| --- | --- |
| `data/plugins.yaml` / `categories.yaml` / `sources.yaml` | **唯一内容源**，手写 |
| `content/plugins/*.md`、`static/search.json`、`data/derived.json`、`data/entry_updated.json`、`data/repo_stats.json` | 脚本产物：**要提交进 git，但绝不许手改**，下次 `build.sh` 全覆盖 |
| `assets/**`、`layouts/**`、`content/{about,privacy,guide,_index}.md`、`hugo.toml`、`build.sh`、`deploy/**` | 手写源 |
| `public/` | 不入库，不要 `git add` |

## 铁律

1. **不 push**。只 `git add` + `git commit`，用户自己在 GitHub Desktop 推。
2. **上线只走 `deploy/deploy.sh`**，不手 `scp`、不 `rsync` 到 `index/` 根。
3. 归类、改名、改简介 → 只改 `data/*.yaml`，永远不碰产物。
4. 主色 `#3C5DFF`（DeepSeek 鲸鱼蓝），别改回更早的紫色。
5. **来源信息已整体下线**（2026-11-18）：`derived.json`、`search.json`、任何页面都不许出现来源标题 / 链接 / 篇数。`refs` 只作内部去重台账。
6. 收录两条硬规则（见 README）：要自己装一次、要能读到官方仓库 README。**找不到仓库就不建条目**，不留占位卡。

## 已踩过的坑

| 症状 | 原因 |
| --- | --- |
| 只改了 `refs`，详情页「条目更新于」却跳到今天 | `entry_updated.py` 切出的块以 `- id:` 开头，`yaml.safe_load` 得到的是**只含一个 dict 的 list**，不解包 `data = data[0]` 则 `refs` 过滤静默失效 |
| 抓线上 `title="…"` 校验失败，但页面明明有 | `hugo --minify` 会把**不含空格的属性值去掉引号**（`title=本站这条…`），别拿带引号的字符串当判据 |
| 分类页 H1 显示成 `Tool` 而不是「工具」 | Hugo 把 taxonomy term 首字母大写了，查映射要用 `.Data.Term`（模板里）或 `Data.Terms` 原始键 |
| 部署 abort：产物里没有 `/dsh/` 前缀 | `baseURL` 漏了 `/dsh/`；`deploy.sh` 的守卫匹配的是指纹文件名 `css/main\.` |
| 主站部署时 `/dsh/` 整个消失 | 主站 `deploy.sh` 的 rsync 带 `--delete --delete-excluded`，必须给 `--filter='P dsh/'` |
| 薄标签页进 sitemap 拖累收录 | `layouts/sitemap.xml` 是自写的：`count<3` 的标签不建索引、页面 `noindex,follow`，别改回 Hugo 默认 |
| 390px 下整页右侧被裁掉、还滚不动 | `html,body{overflow-x:clip}` 只兜底不治病：卡片里 `flag` 之类长文案必须允许换行 |

## 收工前

```bash
./build.sh 2>&1 | grep -E "ERROR|校验通过|条目 "          # 构建无 Error、条目数对得上
grep -o "<loc>" public/sitemap.xml | wc -l               # 当前 185（141 plugins + 26 tags + 14 categories + 4 静态页）；暴涨=薄标签页又进索引
grep -o 'css/main\.min\.[a-f0-9]*\.css' public/index.html | head -1   # 指纹文件名（每次构建只变 hash 不变格式）
```

> `sitemap.xml` 与 HTML 都是压缩成单行的，`grep -c` 只会返回 1，必须用 `grep -o … | wc -l`。

再加两项手测（脚本没法替）：

- **390px 无横向溢出**：`document.documentElement.scrollWidth === innerWidth`（`overflow-x:clip` 会把溢出藏起来，肉眼看不出来，必须量）
- **全站内链 0 死链**：遍历 `public/**/*.html` 里的 `href`，去掉 `/dsh/` 前缀后逐个查文件是否存在（外链、`mailto:`、`#` 锚点跳过）
