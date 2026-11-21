# DSH 插件图谱

把散落各处的 **DeepSeek Harness（DSH）插件**汇总到一个 Hugo 静态站：顺着名字找到插件的官方 GitHub 仓库、读 README，把简介、安装与功能亮点整理成能查的卡片。一切以官方说明为准。自己当速查手册，也能直接分享。

**正式地址：`https://ai.limzero.com/dsh/`**（挂在已备案的 `ai.limzero.com` 主站下的子目录，走阿里云 ECS）

> 非官方站点，与 DeepSeek 及各插件作者无隶属关系。**未对任何插件做安装实测**。**只收需要额外安装、且能核实到官方仓库的插件**，官方开箱即用的内置能力不展示。

**视觉**：用 hallmark 的 **Almanac** 主题（石板蓝纸底、蓝黑墨字、方形直角、双线规、DeepSeek 鲸鱼蓝、等宽数字）做全量 redesign，自建零依赖浅色主题，全站纯静态、无后端无统计。

## 快速开始

```bash
cd dsh-plugin-hub
./build.sh                                     # 校验数据 → 生成页面 → hugo --minify --cleanDestinationDir
```

`hugo.toml` 的 `baseURL` 已经是 `https://ai.limzero.com/dsh/`，全站链接用 `relURL` / `RelPermalink` 生成，**不用改模板就能整体带 `/dsh` 前缀**。

⚠️ 因为是子路径部署，`hugo server` 直接在 `/` 提供页面会和 `/dsh/...` 链接对不上。本地要按子路径预览，用一个带 `dsh/` 目录的临时根：

```bash
mkdir -p /tmp/dsh-preview && ln -sfn "$(pwd)/public" /tmp/dsh-preview/dsh
python3 -m http.server 8765 --bind 127.0.0.1 --directory /tmp/dsh-preview
# 打开 http://127.0.0.1:8765/dsh/
```

依赖：Hugo 0.166+（本机已装）、Python 3 + PyYAML（本机已装）。

## 目录结构

```
data/
  sources.yaml          线索台账：一篇文章一条，只用于内部去重与 refs 完整性校验，不上站
  plugins.yaml          插件主档：一个插件一条，内容以官方仓库 README 为准
  categories.yaml       分类表
  derived.json          【脚本生成】统计 + 各种映射
  repo_stats.json       【脚本生成】GitHub 星标 / Fork / 最近提交快照（fetch_repo_stats.py 写入）
  entry_updated.json    【脚本生成】每个条目最后更新日期（entry_updated.py 从 git 历史推导）
tools/build_data.py     校验 / 去重 / 算仓库确认数 / 生成页面与索引
tools/fetch_repo_stats.py  GitHub API 抓取仓库数据 → repo_stats.json（增量、带缓存）
tools/entry_updated.py   git 历史 → entry_updated.json（详情页「条目更新于」的数据源）
deploy/deploy.sh        部署到 ECS 的 index/dsh/
content/
  plugins/*.md          【脚本生成】133 个插件详情页
  about.md privacy.md guide.md _index.md   手写页面
layouts/                 自建零依赖主题（不拉 submodule）
  sitemap.xml           自写：剔除「挂不满 3 个插件」的标签页 + 输出 lastmod
assets/
  css/main.css js/site.js js/search.js   【Hugo 资源】构建时压缩 + 内容指纹，URL 带 hash
static/
  fonts/*.woff2         自托管 latin 子集（Hanken / Newsreader / Plex Mono），替代 Google Fonts
  favicon.svg og-cover.png apple-touch-icon.png
  search.json           【脚本生成】全站搜索浮层的数据源（含 features / notes / install）
  ads.txt               AdSense 发布商声明（副本，要放到主站根目录才有效）
public/                  hugo 构建产物（不入库）
```

顶层还有 `AGENTS.md`：给 AI 协作者（和隔了几个月回来的自己）的**执行层**说明——文件边界、已踩过的坑、收工自检。

`docs/2026-11-21-optimization-retro.md`：**本轮全站优化的实测复盘**——改前改后数字、390px 溢出探针、无头 Chrome 屏蔽广告截图、内链扫描脚本、AdSense 站点级口径，以及未做完项的判断。做同类体检或想改回去之前先看它。

产品与内容规则以本文为准，那两份文档不重复。

⚠️ `content/plugins/`、`static/search.json`、`data/derived.json`、`data/repo_stats.json`、`data/entry_updated.json` **是产物但要一起提交进 git**——这样线上构建只要 Hugo，不用装 Python/PyYAML。改完 data 必须跑一次生成脚本再提交，否则线上还是旧数据。`build.sh` 带了 `--cleanDestinationDir`，删条目时 `public/` 里的旧页会一起清掉，不留幽灵页面。

**「条目更新于」的口径**：详情页那行日期来自 `data/entry_updated.json`，由 `tools/entry_updated.py` 遍历 `data/plugins.yaml` 的 git 历史算出——只在那一条的可见字段被改动时刷新，`refs`（内部去重台账）改动不算。它表达的是「本站这条记录最后修订于」，不是插件发布日期，也不是构建时间；没动过的条目不会跟着部署变日期。`build.sh` 在有完整 git 历史时会自动重跑该脚本，浅克隆/无 `.git` 时沿用已有产物。

GitHub 星标 / Fork 是快照，不是实时值。想刷新就跑 `python3 tools/fetch_repo_stats.py`（默认只补超过 7 天的，`--all` 全量重刷），再走一遍 `build_data.py && hugo`。有 `GITHUB_TOKEN` 的话几秒跑完；没 token 时匿名 60 次/小时的 core 额度先用，用完自动退到 10 次/分钟的 search 接口，全量约 20 分钟。**别在没网的环境跑构建**——构建只读 `data/repo_stats.json`，不联网。

`static/search.json` 里的 `url` 是站点根相对路径（如 `/plugins/xxx/`）。用 JS 拼链接时先读 `<html data-base>`（值形如 `/dsh/`）再拼，`assets/js/search.js` 就是这么干的。

## 2026-11-21 全站优化（改之前先看这段，别改回去）

| 改动 | 为什么 |
| --- | --- |
| 卡片里的 `flag` 允许换行 + 最多两行 | 原来 `.mini-tag{white-space:nowrap}`，一句长提示把卡片顶到 500~670px，390px 视口整页横向溢出，`overflow-x:clip` 直接把右侧裁掉 |
| 字体自托管到 `static/fonts`，删掉 Google Fonts 外链 | 那条 `<link>` 是渲染阻塞的，大陆被墙；且正文衬线（Newsreader）在国内从来没生效过。只下载 latin 子集，中文走系统栈 |
| `assets/` 资源走 `fingerprint` 指纹 | 版本戳每次构建都变，等于每次部署全量失效缓存；改成内容指纹，没改就不换 URL |
| 全站搜索浮层（`/` 与 `⌘K`），数据读 `search.json` | 以前 `search.json` 生成了没人读，详情页/分类页也没有搜索入口 |
| 首页筛选/搜索/页码写回 `?c=&q=&p=` | 以前刷新即丢，也没法把「桌宠这一类」分享出去 |
| 首页第 24 张之后的卡片直接输出 `hidden` | 以前 133 张全画出来再被 JS 收起，首帧会闪一下 |
| `/plugins/` 改 Hugo 真分页（36/页），`tags` 只给 count≥3 的建索引 | 标签 307 个里 247 个只挂 1 个插件；sitemap 从 458 条降到 175 条 |
| 卡片徽章换掉「官方仓库已确认 / 社区」 | 133/133 都是已确认、129/133 都是社区，零信息量；换成「N 天前有提交 / 久未更新」 |
| 详情页加复制安装命令、GitHub 按钮、相关条目（按共享标签）、整理时间 | 最有用的动作原来都埋在表格里 |

广告：AdSense 的 Anchor / Vignette / In-Form 格式**只能在 AdSense 后台关**（代码关不掉）。窄屏实测顶部锚定广告会盖住 sticky header，建议后台只留一种页内格式，本站不再做代码层补救。

## 收录范围（硬规则）

**两条硬规则，缺一不可：**

1. **这个插件要不要你自己动手装一次？** 要，才收录。
2. **能不能找到可公开访问、能读到 README 的官方仓库？** 找不到就不建条目。宁可少收，也不留「仓库待确认」的占位卡 —— 2026-11-08 已把 4 个无法核实仓库的旧条目（`dsh-websearch` / `dsh-vision` / `dsh-plan-execute` / `dsh-lazyfish`）整体删掉。

官网开箱自带的 Subagents、Terminal、Agent loop、网页搜索、Standard / Code / Minimal / Creator 四种运行模式，以及界面里标为 Experimental 的内置项，**一律不建条目**：不用装、也没法单独装，混进「值得装什么」的清单只会添乱。官网仍作为外链挂在页脚供查阅，不进来源台账；台账只保留有插件实际引用的线索来源。

`tools/build_data.py` 会直接拦下误加回来的 `status: builtin` / `category: builtin` 条目，别绕过它。

## 加一篇公众号文章（内部线索，不上站）

> 🔴 2026-11-18 用户决定：**站点取消「来源」板块** —— 没有来源列表页、插件页不列参考来源、卡片不标「参考 N 篇」、导航与页脚也不出现来源入口。`data/sources.yaml` 与插件的 `refs` 只作仓库内部记录（判断「这篇录过没」、避免重复劳动），`build_data.py` 仍校验 refs 完整性，但**不写进任何产物**，`derived.json` 与 `search.json` 里也不许出现来源标题 / 链接 / 计数。

1. `data/sources.yaml` 追加一条，`id` 短横线小写，链接贴进 `url`：
   ```yaml
   - id: wx-plugin-2026-11-06
     title: "文章标题"
     kind: wechat
     publisher: "公众号名"
     url: "https://mp.weixin.qq.com/s/..."
     date_note: "2026-11-06"     # 原文没写就填「待补」
     note: "这篇补了 XX 类插件，与之前某篇有重叠。"
     tags: [插件清单]
   ```
2. `data/plugins.yaml`：文章提到的插件**已有条目就只在 `refs` 追加一个来源 id**，没有才新建。别名（中文名 / 包名 / 旧名）全塞进 `aliases`，以后才能自动对上；**官方内置能力不要新建条目**。然后**顺着名字去 GitHub 找官方仓库**，补上 `repo` / `install` / `summary` / `features`（按 README 写，不抄文章）。**反复搜不到可信仓库就跳过，不要建条目**：
   ```yaml
   - id: dsh-market
     name: dsh-market
     aliases: [插件市场, dshmarket]
     category: market
     status: community
     repo: "https://github.com/dsh-market/dsh-market"
     install: "dsh plugin add https://github.com/dsh-market/dsh-market"
     summary: "一句话说明（按 README 整理）"
     features:
       - "浏览、搜索、一键安装 DSH 插件"
     refs:
       - wx-plugin-2026-11-06
   ```
3. 跑 `./build.sh`。仓库确认数、首页统计、搜索索引全部自动重算。

脚本会拦下：重复 id、引用了不存在的来源、分类 / status 不合法、**缺少 repo**、以及官方内置条目；别名撞车只给提示不阻断（那往往正是要人工合并的信号）。

**事实纪律**：正文一律以官方仓库 README 为准，不照搬文章原文；仓库地址必须核实到能读到 README 的官方仓库，否则不收录；README 没写的安装命令、发布日期、署名，一律留空或标「待补」；星标数 / 仓库数这类口径不统一的数字不进插件卡。

## 谷歌广告

- 🔴 **2026-11-21 用户决定本站关闭广告**：`hugo.toml → [params.adsense] enabled = false`，页面不再注入 `adsbygoogle.js`，dsh 站完全无广告。这是本站独立开关，不影响 WordPress 总站 limzero.com 的广告。要恢复改回 `true` 再构建部署。`client` 仍保留 `ca-pub-7114121088728794` 备查。若主站仍投 Auto Ads 而只想豁免 /dsh/，走 AdSense 后台「页面排除」加 `limzero.com/dsh/*`。
- （历史说明）原先是 **Auto Ads**（全站自动插位），不用单独建广告单元、不用填假的 `data-ad-slot`。
- 🔴 **`ads.txt` 只有在域名根目录才有效**：AdSense 会读 `https://ai.limzero.com/ads.txt`，**不会**读 `https://ai.limzero.com/dsh/ads.txt`。`static/ads.txt` 是本仓库留的副本，内容必须同步到主站根目录（主站目前还没有这个文件）。上线后用 `curl https://ai.limzero.com/ads.txt` 确认返回那一行 `google.com, pub-7114121088728794, DIRECT, f08c47fec0942fa0`，AdSense 重新抓取可能要几天。
- AdSense 后台按域名管理站点，`ai.limzero.com` 若已在站点列表且审核通过，`/dsh` 通常不用重复添加；以后台实际显示为准。
- 页面里那些虚线框只是广告位示意，实际广告由 Google 自动插入。

## 部署

正式部署走 ECS（和 `ai.limzero.com` 主站同一台）：

```bash
bash deploy/deploy.sh              # 构建 + rsync 到 index/dsh/ + 线上校验
bash deploy/deploy.sh --sync-only  # 产物已构建，只同步
```

| 项 | 值 |
| --- | --- |
| 宿主机目录 | `/opt/1panel/apps/openresty/openresty/www/sites/ai.limzero.com/index/dsh` |
| 容器内目录 | `/www/sites/ai.limzero.com/index/dsh` |
| SSH | `~/.ssh/id_aliyun` → `root@121.40.250.144` |
| 构建 | `hugo --minify --cleanDestinationDir --baseURL https://ai.limzero.com/dsh/` |

脚本只同步 `index/dsh/` 一个子目录，`--delete` 的作用范围仅限它，不会碰主站文件；还会检查产物里的资源链接是否带 `/dsh/` 前缀，防止 `baseURL` 写错把整站链接发到主站根。vhost 需要有 `try_files $uri $uri/index.html $uri/ =404`，`/dsh/plugins/xxx/` 才能落到 `index.html`。

### 🔴 上线前必做（都在主站侧，需改 `ai-limzero-hub` 仓库）

1. **主站部署脚本加保护规则**：`ai-limzero-hub/deploy/deploy.sh` 的 rsync 带 `--delete --delete-excluded`，会把不在主站 `public/` 里的 `dsh/` 整个删掉。在它的 filter 参数最前面加 `--filter='P dsh/'`（保护规则），主站再部署才不会清掉本站。
2. **主站根目录放 `ads.txt`**：把 `static/ads.txt` 那一行加到 `ai-limzero-hub/static/ads.txt`。
3. **主站 `robots.txt` 声明本站 sitemap**：加一行 `Sitemap: https://ai.limzero.com/dsh/sitemap.xml`。`robots.txt` 同样只在主机根目录生效，`/dsh/robots.txt` 爬虫不读。改完要重新部署主站才生效。

以上三步做完，再去 AdSense 后台确认站点与 `ads.txt` 状态。

**Cloudflare Pages 只作备选/预览**：构建命令 `hugo --minify`、输出目录 `public`、`HUGO_VERSION=0.166.0`。因为生成产物已入库，构建环境不需要 Python。但 `baseURL` 已固定为正式域名，CF 预览域名上的 canonical / sitemap 仍指向 `ai.limzero.com/dsh`，别拿它当正式站。

按约定：AI 只做 `git add` + `git commit`，**不 push**，由你在 GitHub Desktop 手推。

## 目前的数据

136 个插件 / 27 条来源，**全部已确认官方仓库**；13 个分类均有条目。

已录入两篇公众号清单文作为「发现来源」：第 1 篇偏入门与自用清单，第 2 篇（智宇AI说，14 大类）带来 46 条插件引用——其中 7 条并入已有插件的参考来源（如 `modsearch`、`dsh-market`、小鲸鱼挂件），39 条是全新条目。该文的仓库地址抽查 24 个（23 个 200 / 1 个 301），Stars 数字与标题「36 款」按纪律不采信。每个插件的内容都以对应官方仓库 README 为准，公众号文章只作发现来源与对照。后续又录入第 3 篇（运维网工，单插件 dsh-devops 深度文）、第 4 篇（飞叔，官方点名的 4 个插件盘点）、第 5 篇（近 30 天下载 TOP10 榜）、第 6 篇（狐小墨，7 款推荐清单）、第 7 篇（老马 PaperToday，agentero-dsh 实测）、第 8 篇（繁星，deepseek-bot 介绍）、第 9 篇（世相智能体，10 款亲测清单）、第 10 篇（维客笔记，dsh-rewind 菜单回退）与第 11 篇（有料黑科技，dsh-deepseek-web-login 实操踩坑）、第 12 篇（狐小墨进阶篇，再添 10 件新装备）、第 13 篇（晓白AI纪元，17 插件四路盘点）、第 14 篇（甲维斯机，5 款省 Token 插件实测）、第 15 篇（数字山水间，十大插件榜单刷新）、第 16 篇（小成同学，DSH 社区 7 个优选插件）、第 17 篇（猿码，18 个插件四组清单）、第 18 篇（AisketchLab，按干活顺序的 15 个），均只作发现来源。

第 3 篇（运维网工，2026-11-03）不是清单文，而是 `dsh-devops` 的单插件深度介绍，正文与该仓库中文 README 高度重叠；本站据此去 GitHub 核对了仓库、package.json、LICENSE 与安装路径，新增 1 个插件条目，文章仍只作发现来源。

第 5 篇（小白分享1234，2026-11-01）是近 30 天下载量 TOP10 榜。文中下载量、星标与版本号均为文章口径且与仓库实时数据有出入，一律不采信；本站顺着名字逐个核对官方仓库 README，新增 5 个条目（`dsh-skills-manager`、`dsh-client-ui-skill-explorer`、`dsh-cost-meter`、`dsh-codex-ui`、`dsh-remote-bridge`）。榜单第 9 名 `dsh-remote-web-ui` 文章已注明弃用、由 `dsh-remote-bridge` 接替，本站只收接替者。

第 6 篇（狐小墨，2026-10-31）是 7 款推荐清单，其中 6 款此前已收录、本条只为它们补新的发现线索；唯一新条目 `billion-context` 是跨 20+ 编程助手的通用上下文压缩代理（DSH 只是其一），本站按其官方仓库 README 收录并注明。文中的星标、下载量与「省 5 倍 token」均为文章或安装界面口径，不采信为独立结论。

第 7、8 篇均为单插件介绍（`agentero-dsh` / `deepseek-bot`），两款此前已收录、仓库地址一致，本条只作新的发现线索，内容仍以官方仓库 README 为准；文中的实测数字与评价性说法不采信为收录口径。

第 9 篇（世相智能体，2026-11-06）是 10 款亲测清单，新增 `dsh-browser`（真实浏览器）与 `dsh-image-gen`（对话生图）两条，其余 8 款只补发现线索；文章写的 dsh-browser 旧版 github tag 安装命令不采用，按官方 README 用最新 scoped 包名。另有读者发来一篇 AnySearch 深度搜索插件的文章，但该服务查不到可信官方仓库 / npm 包（文章只说「在插件市场搜索安装」），按「查不到仓库就不建条目」的规则未收录。

第 10 篇（维客笔记，2026-10-20）新增 `dsh-rewind`（对话回退）一条：仓库 SiriLee/dsh-rewind 核实为真，npm 包名是 `dsh-rewind-plugin`（README 明确警告 `dsh-rewind` 属于他人），文章只写「粘贴仓库链接安装」未给 npm 名，本站按官方 README 写。第 11 篇（有料黑科技，2026-10-30）是已收录 `dsh-deepseek-web-login` 的实操踩坑文，本条只补发现线索并按官方 README 补账号库 / 防风控两组能力；文中 40 万字符、并发 2 次等风控阀门属文章实测口径，不采信为结论。

第 12 篇（狐小墨，2026-11-04）是 7 款推荐的进阶篇，新增 6 条：`dsh-vision-router`（视觉路由）、`dsh-nacos-bridge`（Nacos 接口桥）、`dsh-im`（9 渠道 IM）、`dsh-pocket`（手机同屏）、`dsh-wallpaper-engine`（壁纸引擎）、`dsh-openviking`（用户画像与记忆），`dsh-our-free-model` 与 `dsh-web` 两条此前已收录只补线索。文中 `hindsight` 名字泛化、GitHub 上多个 2~9 星同名仓库且外链经微信跳转无法确认指向，`WeKnora` 本身是腾讯开源知识库系统（Tencent/WeKnora）而非独立 DSH 插件、对接仓库均为 0 星且功能分散——两者都按「查不到可信仓库就不建条目」未收。

第 13 篇（晓白AI纪元，2026-10-27）按创作/科研/办公/地基四路盘 17 个插件（另 3 个编号是变现思路不是插件，未建条目）。本次新增 11 条：`dsh-wechat-article`、`dsh-novel`、`dsh-novel-craft`、`dsh-plugin-academic-paper`、`dsh-deep-research`、`dsh-dev-mode`、`dsh-computer-use-win`、`dsh-topic-audit`、`dsh-skill-zh-distribute`、`dsh-mic-input`、`dsh-autoresearch`；`dsh-agent-teams`、`dsh-browser`、`dsh-market`、`dsh-better-sidebar`、`dsh-find-plugin`、`dsh-web` 已收录只补线索。几个按仓库事实做的校正：文章写 `dsh-computer-use`「只有 Windows 版」，故收 Yu-tao-Li 的 Windows 仓（Anionex 的 macOS 版不收）；`dsh-dev-mode` 用文章明确给出的 lingyingaojue 仓库；`dsh-deep-research` 取官方 org `dsh-external` 仓（搜索首位的 omdsh-dev 是镜像）；`dsh-wechat-article` 与 `dsh-topic-audit` 无已发布 npm 包，按 git 形式写安装。`dsh-automation` 因 README 声明 2026-10-08 停止维护且 DSH 已有官方定时能力，按弃用未收。

第 14 篇（甲维斯机，2026-11-05）是省 Token 插件横向实测，新增 `dsh-plugin-save-token`（结构感知可逆压缩）与 `dsh-flash-presets`（V4.1 Flash 预设）两条，`dsh-ops` 已收录只补线索。文中实测的省 4.5%~36.4% 与费用数字属单次口径不采信；PTC 是 DSH 官方自带模式按内置不收；Condense 插件只给名字与功能、GitHub/npm 均无精确匹配的可信仓库，按「查不到仓库就不建条目」未收；flash-presets 安装固定到已发布的 0.3.1（README 警告别装 0.2.5）。

第 15 篇（数字山水间，2026-11-09）是 10 月 18 日那版「十大神器」榜单的刷新，口径为 npm 官方源 + npmmirror 镜像的累计下载合计（截至 2026-11-03，取自 dsh.so 的跟踪集合）。榜单里 10 个插件本站早已全部覆盖，本次没有新增条目，只给 `billion-context`、`dsh-market`、`dsh-better-sidebar`、`dsh-pet`、`dsh-context`、`modlens`、`dsh-cost-meter`、`dsh-skills-manager`、`dsh-codex-ui` 九条补了发现线索。第 5 名 `dsh-skins`（原文称原名 dsh-client-ui-skin-center）未收：npm 上的裸包 `dsh-skins` 由 loong-feng 维护、只有一个 0.2.0 版本，元数据没有 repository 字段，README 与安装步骤（手动复制文件进 profiles 目录再改 `cordis.patch.yml`）也没有任何仓库地址；GitHub 上同名仓库分属不同作者（leo-aba/dsh-skins、Moeblack/dsh-skins、zhu1090093659/dsh-web-ui 的 packages/dsh-skins），内容与该包「ACG 主题族 + 3 套皮肤 + 字体页签」的描述并不对应，按「查不到可信仓库就不建条目」未收。文中下载量与「涨了 / 掉队」的名次判断是文章口径与它的统计切片，不采信也不进插件卡；掉出前十的五个 client-ui / 远程连接类包（task-board、remote-web-ui、git-graph、skill-explorer、ssh）属官方客户端能力或被官方收敛，不因此增删条目。

第 16 篇（小成同学，2026-10-26）是近半年里少见地逐条复核官方 README 的清单文，新增 3 条：`dsh-git-graph`（enoughpower，npm 上那个可写版本）、`dsh-git-graph-readonly`（WhitePlusMS，Release 安装的只读版本）、`dsh-free-search`（DDDMUC，42 引擎多路搜索）。`dsh-market`、`billion-context`、`dsh-codex-ui`、`dsh-better-sidebar`、`dsh-ops` 五条早已收录，只补线索。文中最有价值的是它自己做的区分：两个同名 dsh-git-graph 不是同一个插件；`dsh-codex-ui` 的 npm 全名是 `@michengai/dsh-codex-ui`，漏掉作用域装不上；better-sidebar 的 v0.28.0 要 DSH 0.2.1-rc.1+、0.2.0-rc.2 得用 0.26.1。文中「7 个搜索引擎」「少用 5 倍 Token」「177 万下载」「永不失败」等宣传口径一律不采信——尤其引擎数是 42 不是 7，按当前 README 写。

第 17 篇（猿码，2026-11-16）是四组分类的 18 款清单，价值主要在开头那三条筛选标准（看得出还在维护、权限边界清楚、有「确认后落盘」这一环），与本站收录口径基本同向。18 条里 8 条已收录（`dsh-market`、`dsh-wechat`、`dsh-context`、`dsh-cost-meter`、`dsh-univer-office`、`dsh-genui`、`oh-story-dsh`、`dsh-pet`），新增 10 条：`universal-plugin-hub`、`dsh-go`、`dsh-qqbot`、`dsh-reasoning-only-guard`、`dsh-memory-palace`、`dsh-easyrewrite`、`dsh-ego-browser`、`dsh-bili-scroll`、`dsh-bili-humanism`、`dsh-nekowhale-stickers`。三处按 README 修正或注明：`dsh-Go` 是 Android 客户端不是插件，收进「移动端与远程」并把安装栏写成 APK 侧载；`dsh-bili-scroll` 的 npm 包停在 0.1.7（作者称发布账号在申诉，新版只从 Release 发），照 `add dsh-bili-scroll` 会拿到缺参数的旧版，安装栏改写成 Release tgz 直链；`dsh-qqbot` 是 tencent-connect 组织的官方包、装到 `qqbot` profile，与社区几个同名 dsh-qqbot 不是一回事。文中「投了约 32 万 Token 整理表情包」属作者口径，不采信。

第 18 篇（AisketchLab，2026-11-14）是 15 款清单，按「打开就有文件与浏览器 → 资料查得到、长任务能接着干 → 离开电脑也知道进度 → 情报和桌宠」四组排，文末自己声明「清单依据项目公开文档整理，未逐个安装实测」。7 条此前已收录（`dsh-market`、`dsh-better-sidebar`、`dsh-context`、`dsh-browser`、`billion-context`、`universal-plugin-hub`、`dsh-bili-scroll`），新增 7 条：`dsh-windows-mcp`、`dsh-knowledge`、`cc-safety-net`、`dsh-overall-mcp`、`dsh-notifier`、`dsh-remote-control`、`dsh-bigfish`。`dsh-automation` 维持不收（早前已判定停维、且 DSH 有官方定时能力）。三处同名歧义按 README 特征认定：`dsh-knowledge` 有 lemoncat7、XZX888、slder 等多个近名包，按文中「关键词 + 向量检索、本地向量模型 / 重排 / OCR」锁定 Soren-ABT 那份；`dsh-remote-control` 另有 icrefin 的同名实现走 relay，按「明文 ws:// + 令牌即控制权」锁定 stjq12；`dsh-notifier` 与 dsh-notify-im、dsh-gateway-notify、dsh-plugin-notify 属同类近名包，按包名与 8 通道适配器锁定 THEWOLFWALKER。

第 24 篇（挖挖说AI，2026-11-20「装上这 10 个插件」）是 10 款入门清单，只给包名 / 安装界面关键词，无仓库地址。7 款已收录只补线索（Dream Skin / DSH-IM / DSH Market / GenUI / Balance Whale 小鲸鱼 / Agent Teams / Better Sidebar）；新增 3 条：`dsh-dream-skin`（包名 dsh-dream-skin，官方仓库已从封禁的 GitHub 迁至 gitcode.com/LLLAAAAA/dsh-dream-skin，8 套 Mirage 主题 + 壁纸 + 强调色，与文章描述吻合）、`dsh-connect-workbuddy`（dingminhua，本机 WorkBuddy 登录态接进 DSH 模型选择器）、`dsh-imagegen`（文章称 VisioWork，包名 dsh-imagegen 对应 dickpy/dsh-imagegen，文生图 / 图生图 + 提示词反推 + 可配渠道模型）。三处同名歧义按仓库特征认定：Dream Skin 另有独立桌面软件 xxloocee/Dream-Skin 与另一同名 GitHub 插件，前者非 DSH 插件、后者无主题包系统，均不收，只取 GitCode 那份；`dsh-imagegen` 与已收录的 `dsh-image-gen`（shanliuling，对话生图）是不同插件，按「选图生提示词 + 无限画布」锁定 dickpy 版、未合并。「语音输入」文章自述是 DSH 自带插件，按内置能力不建条目。文章评价性口吻与手机 ClawBot 演示不采信。

官方开箱即用的 9 个内置能力条目与「官方内置能力」分类已整体移除；原先误挂在内置条目上的一条 `dsh-agent-teams` 引文已迁回社区插件主档。

其余来源是百科、第三方媒体与开发教程；官网、目录站等无插件引用的空来源已于 2026-11-08 移除。**你继续把公众号文章链接发过来，我顺着它发现插件、再去官方仓库补全内容**，这个站越用越完整。
