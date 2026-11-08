# DSH 插件图谱

把散落在公众号、官方文档、百科与目录站里的 **DeepSeek Harness（DSH）插件**汇总到一个 Hugo 静态站：顺着文章发现插件，再回到它的官方 GitHub 仓库读 README，把简介、安装与功能亮点整理成能查的卡片。文章只作「发现来源 / 参考」，正文以官方说明为准。自己当速查手册，也能直接分享。

**正式地址：`https://ai.limzero.com/dsh/`**（挂在已备案的 `ai.limzero.com` 主站下的子目录，走阿里云 ECS）

> 非官方站点，与 DeepSeek 及各插件作者无隶属关系。数据来自 9 个真实公开来源（含 3 篇公众号文章），**未对任何插件做安装实测**。**只收需要额外安装的插件**，官方开箱即用的内置能力不展示。

**视觉**：用 hallmark 的 **Almanac** 主题（石板蓝纸底、蓝黑墨字、方形直角、双线规、克制品红、等宽数字）做全量 redesign，自建零依赖浅色主题，全站纯静态、无后端无统计。

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
  sources.yaml          来源台账：一篇文章一条（发现来源 / 参考）
  plugins.yaml          插件主档：一个插件一条，内容以官方仓库 README 为准
  categories.yaml       分类表
  derived.json          【脚本生成】统计 + 各种映射
tools/build_data.py     校验 / 去重 / 算仓库确认数 / 生成页面与索引
deploy/deploy.sh        部署到 ECS 的 index/dsh/
content/
  plugins/*.md          【脚本生成】79 个插件详情页
  sources/*.md          【脚本生成】9 个来源页
  about.md privacy.md _index.md   手写页面
layouts/                 自建零依赖主题（不拉 submodule）
static/
  css/main.css js/site.js favicon.svg
  search.json           【脚本生成】前端本地搜索索引
  ads.txt               AdSense 发布商声明（副本，要放到主站根目录才有效）
public/                  hugo 构建产物（不入库）
```

⚠️ `content/plugins/`、`content/sources/`、`static/search.json`、`data/derived.json` **是产物但要一起提交进 git**——这样线上构建只要 Hugo，不用装 Python/PyYAML。改完 data 必须跑一次生成脚本再提交，否则线上还是旧数据。`build.sh` 带了 `--cleanDestinationDir`，删条目时 `public/` 里的旧页会一起清掉，不留幽灵页面。

`static/search.json` 里的 `url` 是站点根相对路径（如 `/plugins/xxx/`）。将来若用 JS 拼链接，先读 `<html data-base>`（值形如 `/dsh/`）再拼，别直接拿它当完整 URL。

## 收录范围（硬规则）

**判断标准只有一条：这个插件要不要你自己动手装一次？** 要，才收录。

官网开箱自带的 Subagents、Terminal、Agent loop、网页搜索、Standard / Code / Minimal / Creator 四种运行模式，以及界面里标为 Experimental 的内置项，**一律不建条目**：不用装、也没法单独装，混进「值得装什么」的清单只会添乱。官网与架构类来源仍留在来源台账里，只作为发现线索。

`tools/build_data.py` 会直接拦下误加回来的 `status: builtin` / `category: builtin` 条目，别绕过它。

## 加一篇公众号文章

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
2. `data/plugins.yaml`：文章提到的插件**已有条目就只在 `refs` 追加一个来源 id**，没有才新建。别名（中文名 / 包名 / 旧名）全塞进 `aliases`，以后才能自动对上；**官方内置能力不要新建条目**。然后**顺着名字去 GitHub 找官方仓库**，补上 `repo` / `install` / `summary` / `features`（按 README 写，不抄文章）：
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

脚本会拦下：重复 id、引用了不存在的来源、分类 / status 不合法、以及官方内置条目；别名撞车只给提示不阻断（那往往正是要人工合并的信号）。

**事实纪律**：正文一律以官方仓库 README 为准，不照搬文章原文；原文没写的仓库地址、安装命令、发布日期、署名，一律留空或标「待补」；星标数 / 仓库数这类口径不统一的数字不进插件卡。

## 谷歌广告

- `hugo.toml` 里 `[params.adsense]` 用了你现有账号的 `ca-pub-7114121088728794`，方式是 **Auto Ads**（全站自动插位），不用单独建广告单元、不用填假的 `data-ad-slot`。想本地彻底关掉把 `enabled` 改 `false`。
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

79 个插件 / 9 条来源，已确认官方仓库的数量见首页统计；13 个分类均有条目。

已录入两篇公众号清单文作为「发现来源」：第 1 篇偏入门与自用清单，第 2 篇（智宇AI说，14 大类）带来 46 条插件引用——其中 7 条并入已有插件的参考来源（如 `modsearch`、`dsh-market`、小鲸鱼挂件），39 条是全新条目。该文的仓库地址抽查 24 个（23 个 200 / 1 个 301），Stars 数字与标题「36 款」按纪律不采信。每个插件的内容都以对应官方仓库 README 为准，公众号文章只作发现来源与对照。

第 3 篇（运维网工，2026-11-03）不是清单文，而是 `dsh-devops` 的单插件深度介绍，正文与该仓库中文 README 高度重叠；本站据此去 GitHub 核对了仓库、package.json、LICENSE 与安装路径，新增 1 个插件条目，文章仍只作发现来源。

官方开箱即用的 9 个内置能力条目与「官方内置能力」分类已整体移除；原先误挂在内置条目上的一条 `dsh-agent-teams` 引文已迁回社区插件主档。

其余来源是官网、百科、目录站与第三方教程。**你继续把公众号文章链接发过来，我顺着它发现插件、再去官方仓库补全内容**，这个站越用越完整。
