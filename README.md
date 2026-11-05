# DSH 插件图谱

把散落在公众号、官方文档、百科与目录站里的 **DeepSeek Harness（DSH）插件**说法汇总到一个 Hugo 静态站：同一个插件去重合并，多篇说法一致的标「印证」，打架的单独列进「口径核对」。自己当速查手册，也能直接分享。

> 非官方站点，与 DeepSeek 及各插件作者无隶属关系。数据来自 8 个真实公开来源（含 2 篇公众号文章），**未对任何插件做安装实测**。**只收需要额外安装的插件**，官方开箱即用的内置能力不展示。

## 快速开始

```bash
cd dsh-plugin-hub
./build.sh                                     # 校验数据 → 生成页面 → hugo --minify --cleanDestinationDir
hugo server -D                                 # 本地预览 http://localhost:1313
```

依赖：Hugo 0.166+（本机已装）、Python 3 + PyYAML（本机已装）。

## 目录结构

```
data/
  sources.yaml          来源台账：一篇文章一条
  plugins.yaml          插件主档：一个插件一条 + mentions 证据链
  discrepancies.yaml    口径核对：说法打架的并列摆出来
  categories.yaml       分类表
  derived.json          【脚本生成】统计 + 各种映射
tools/build_data.py     校验 / 去重 / 算印证 / 生成页面与索引
content/
  plugins/*.md          【脚本生成】78 个插件详情页
  sources/*.md          【脚本生成】8 个来源页
  about.md privacy.md notes.md _index.md   手写页面
layouts/                 自建零依赖主题（不拉 submodule）
static/
  css/main.css js/site.js favicon.svg
  search.json           【脚本生成】前端本地搜索索引
  ads.txt               AdSense 发布商声明
public/                  hugo 构建产物（不入库）
```

⚠️ `content/plugins/`、`content/sources/`、`static/search.json`、`data/derived.json` **是产物但要一起提交进 git**——这样线上构建只要 Hugo，不用装 Python/PyYAML。改完 data 必须跑一次生成脚本再提交，否则线上还是旧数据。`build.sh` 带了 `--cleanDestinationDir`，删条目时 `public/` 里的旧页会一起清掉，不留幽灵页面。

## 收录范围（硬规则）

**判断标准只有一条：这个插件要不要你自己动手装一次？** 要，才收录。

官网开箱自带的 Subagents、Terminal、Agent loop、网页搜索、Standard / Code / Minimal / Creator 四种运行模式，以及界面里标为 Experimental 的内置项，**一律不建条目**：不用装、也没法单独装，混进「值得装什么」的清单只会添乱。官网与架构类来源仍留在来源台账里，但只作核对二手文章说法的基准，差异记在口径核对页，不另开插件卡。

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
2. `data/plugins.yaml`：文章提到的插件**已有条目就只在 `mentions` 追加一条**，没有才新建。别名（中文名 / 包名 / 旧名）全塞进 `aliases`，以后才能自动对上；**官方内置能力不要新建条目**：
   ```yaml
   - id: dsh-market
     name: dsh-market
     aliases: [插件市场, dshmarket]
     category: market
     status: community
     summary: "一句话说明"
     mentions:
       - source: wx-plugin-2026-11-06
         stance: 印证            # 印证 / 补充 / 仅提及 / 有出入
         quote: "文章里的原话（英文来源写「译述：…」）"
   ```
3. 跑 `./build.sh`。印证数、冲突徽章、首页统计、搜索索引全部自动重算。说法冲突时把 `stance` 写成 `有出入`，并去 `data/discrepancies.yaml` 加一条。

脚本会拦下：重复 id、引用了不存在的来源、分类 / status / stance 不合法、引文为空、以及官方内置条目；别名撞车只给提示不阻断（那往往正是要人工合并的信号）。

**事实纪律**：原文没写的仓库地址、安装命令、发布日期、署名，一律留空或标「待补」；星标数 / 仓库数这类口径不统一的数字不进插件卡；英文引文标「译述」并保留原文链接。

## 谷歌广告

- `hugo.toml` 里 `[params.adsense]` 用了你现有账号的 `ca-pub-7114121088728794`，方式是 **Auto Ads**（全站自动插位），不用单独建广告单元、不用填假的 `data-ad-slot`。想本地彻底关掉把 `enabled` 改 `false`。
- `static/ads.txt` 已按标准格式写好；若换新发布商账号，同步改 `client` 与 `ads.txt`，并以后台给出的那一行为准。
- 上线前必做：① `hugo.toml` 的 `baseURL` 改成真实域名（现在是占位的 `https://example.com/`）；② 在 AdSense 后台把新域名加进「站点」并等审核通过；③ 已备好「关于」「广告与隐私」页，审核通常需要这类页面和一定量原创内容。
- 页面里那些虚线框只是广告位示意，实际广告由 Google 自动插入。

## 部署

Cloudflare Pages（推荐，和你其它静态站一套）：

| 项 | 值 |
| --- | --- |
| 构建命令 | `hugo --minify` |
| 输出目录 | `public` |
| 环境变量 | `HUGO_VERSION = 0.166.0` |

因为生成产物已入库，构建环境不需要 Python。也可以把 `public/` 直接 rsync 到 ECS 的站点目录（沿用你现有的 OpenResty 路径约定）。部署前记得先跑 `./build.sh` 再提交。

按约定：AI 只做 `git add` + `git commit`，**不 push**，由你在 GitHub Desktop 手推。

## 目前的数据

78 个插件 / 8 条来源 / 90 条证据，其中 9 条多篇印证、1 条插件内口径冲突、6 条待核对分歧，13 个分类均有条目。

已录入两篇公众号清单文：第 1 篇偏入门与自用清单，第 2 篇（智宇AI说，14 大类）带来 46 条插件引用——其中 7 条并入已有插件的证据链（如 `modsearch`、`dsh-market`、小鲸鱼挂件从「单篇提及」升为「多篇印证」），39 条是全新条目。该文的仓库地址抽查 24 个（23 个 200 / 1 个 301），Stars 数字与标题「36 款」按纪律不采信，详见口径核对页。

官方开箱即用的 9 个内置能力条目与「官方内置能力」分类已整体移除；原先误挂在内置条目上的一条 `dsh-agent-teams` 引文已迁回社区插件主档，官网来源仅保留作核对基准。

其余来源是官网、百科、目录站与第三方教程。**你继续把公众号文章链接发过来，印证数才会真正长起来**，这也是这个站越用越值钱的地方。
