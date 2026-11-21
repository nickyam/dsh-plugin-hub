# 2026-11-21 全站优化复盘（可复用）

三份文档的分工：

| 文档 | 回答什么 |
| --- | --- |
| `README.md` | 这个站是什么、收录规则、部署参数、为什么这么设计 |
| `AGENTS.md` | AI 接手时的文件边界、铁律、已踩的坑 |
| **本文** | **当时量到了什么、用什么方法量的、为什么这么决策、还差什么** |

下次要对同类站点做「全站体检」，或者有人问「某某要不要改回去」，先看这里。

---

## 一、接手时的基线

| 项 | 值 |
| --- | --- |
| 内容 | 133 个插件 / 13 个分类 / **307 个标签，其中 247 个只挂 1 个插件** |
| 索引 | sitemap 458 条 URL，307 条是薄标签页；只有 `<loc>`，无 `lastmod` |
| 首页 | raw ~170KB / gzip ~37KB，其中卡片块 ~115KB；133 张卡全渲染，JS 再隐藏 109 张 |
| 搜索 | `search.json` 99KB / gzip 29KB **生成了但没有代码读取**；搜索只覆盖 name/alias/summary/tags，搜不到 features |
| 字体 | Google Fonts 一条阻塞渲染的 `<link>`，3 个家族 8 个字重，大陆被墙 → 正文衬线从未生效 |
| 广告 | 纯 Auto Ads，无手动位；452px 实测顶部锚定广告完整盖住 sticky header |
| SEO | 0 个 OG 标签，`static/` 无图；无 `SoftwareApplication` 等结构化数据 |
| 内容完整度 | 133/133 都是「官方仓库已确认」、129/133 都是「社区」——两个常驻徽章零信息量；7 条无 install 只显示「README 未给安装命令」 |

## 二、改完后的基线（2026-11-21 晚实测）

| 项 | 改前 → 改后 |
| --- | --- |
| 390px `documentElement.scrollWidth` | **646（分类页 707）→ 390**，与视口等宽 |
| `/plugins/` 列表页 | **164KB → 53KB**，36 条/页，多出 `page/2..4` 可索引页 |
| sitemap | **458 → 175 条**，175 个 `lastmod`；薄标签页 `noindex,follow` |
| 首页卡片首帧 | 133 张全画 → 第 25 张起 HTML 里就带 `hidden` |
| 首页 gzip | 37KB → **39KB**（基本没变，收益不在这里） |
| `search.json` | 99KB → **202KB / gzip 77KB**（补了 features/notes/install；首次打开搜索才下载，不占首屏） |
| 字体 | 4 个 latin 子集 woff2 自托管，共 **112KB**，同源、7 天 immutable |
| HTML 总数 | 464（含 3 个分页 + guide + 404） |
| 详情页正文 | 中位 1112 字 / 最少 787 / 最多 1720 |
| 内链 | 扫描 13680 个 `href` → **0 死链** |

**一个诚实的结论**：首页体积几乎没降。真正的收益是移动端不再被裁、大陆首屏不再等字体、列表页可索引、搜索从摆设变成可用。

---

## 三、测量方法（复制即用）

### 1. 横向溢出：iframe 固定宽度探针

🔴 **不要直接用 `--window-size=390` 判断移动端**：无头 Chrome 的窗口尺寸和 CSS 视口不总一致（窗口装饰 / dpr），会得出错误结论。用 iframe 把宽度钉死。

把探针放进本地构建目录（例 `/tmp/dshlocal/probe.html`），起 `python3 -m http.server 8899 --bind 127.0.0.1`：

```html
<!doctype html><meta charset=utf-8>
<style>body{margin:0;font:13px monospace}iframe{border:0;width:390px;height:1300px}</style>
<pre id=out>loading</pre><iframe id=f src="/"></iframe>
<script>
const f = document.getElementById('f');
f.addEventListener('load', () => setTimeout(() => {
  const d = f.contentDocument, w = f.contentWindow;
  const n = d.querySelector('.stats-note');
  document.getElementById('out').textContent = [
    'vw=' + w.innerWidth + ' docW=' + d.documentElement.scrollWidth,
    'headerH=' + Math.round(d.querySelector('.site-header').getBoundingClientRect().height),
    'h1=' + d.querySelector('h1').textContent.trim().slice(0, 20),
    'noteLines=' + (n ? Math.round(n.getBoundingClientRect().height /
        parseFloat(w.getComputedStyle(n).lineHeight)) : '-')
  ].join('\n');
}, 900));
</script>
```

```bash
CH="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
env -u HTTP_PROXY -u HTTPS_PROXY -u http_proxy -u https_proxy -u ALL_PROXY -u all_proxy \
  "$CH" --headless=new --disable-gpu --no-sandbox --no-proxy-server \
  --window-size=1000,1500 --virtual-time-budget=8000 --dump-dom \
  "http://127.0.0.1:8899/probe.html" 2>/dev/null \
| python3 -c "import sys,re,html;d=sys.stdin.read();m=re.search(r'<pre id=\"out\">(.*?)</pre>',d,re.S);print(html.unescape(m.group(1)) if m else 'NO OUT')"
```

要点：`overflow-x:clip` 会把溢出**藏起来，肉眼看不出来**，必须量 `scrollWidth`。修 `flag` 换行前是 646/707，修完才是 390。

### 2. 截图时屏蔽广告域

```bash
BLK="MAP pagead2.googlesyndication.com 127.0.0.1, MAP googleads.g.doubleclick.net 127.0.0.1, MAP tpc.googlesyndication.com 127.0.0.1, MAP adservice.google.com 127.0.0.1, MAP securepubads.g.doubleclick.net 127.0.0.1, MAP fundingchoicesmessages.google.com 127.0.0.1"
env -u HTTP_PROXY -u HTTPS_PROXY -u http_proxy -u https_proxy -u ALL_PROXY -u all_proxy \
  "$CH" --headless=new --disable-gpu --hide-scrollbars --no-sandbox --no-proxy-server \
  --window-size=1440,1400 --virtual-time-budget=6000 \
  --host-resolver-rules="$BLK" --screenshot=/tmp/shot.png "https://ai.limzero.com/dsh/" 2>/dev/null
```

### 3. 出网

本机 Bash 会被注入 WorkBuddy 代理，偶发 TLS 握手失败；所有 curl / Chrome 命令**先去掉代理再跑**（上面已带 `env -u ...`）。直连通常正常。回退才用系统代理。

### 4. 产物自检

```bash
./build.sh 2>&1 | grep -E "ERROR|校验通过|条目 "
grep -o "<loc>" public/sitemap.xml | wc -l          # 175
grep -o 'css/main\.min\.[a-f0-9]*\.css' public/index.html | head -1
```

🔴 sitemap 和 HTML 都被压成**单行**，`grep -c "<loc>"` 恒返回 1，必须 `grep -o … | wc -l`。

内链扫描（要兼容 `--minify` 产生的**无引号** `href=/dsh/guide/`）：

```python
import re, os, urllib.parse, glob
bad, total = [], 0
for f in glob.glob('public/**/*.html', recursive=True):
    h = open(f, encoding='utf-8').read()
    for m in re.finditer(r'href=(?:"([^"]+)"|([^\s>]+))', h):
        href = m.group(1) or m.group(2); total += 1
        if href.startswith(('http', 'mailto:', '#', 'data:', '//')): continue
        p = urllib.parse.unquote(href.split('#')[0].split('?')[0]).replace('/dsh/', '/')
        if not p: continue
        t = 'public' + (p + 'index.html' if p.endswith('/') else p)
        if not os.path.exists(t): bad.append((f, href))
print('扫描 href:', total, '死链:', len(bad)); print(*bad[:8], sep='\n')
```

---

## 四、口径与决策（别改回去）

- **「条目更新于」= 这条记录在 `data/plugins.yaml` 的 git 历史里，可见字段最后一次被改动的日期。** 内部 `refs` 改动不算。它不是插件发布日期，也不是构建时间 `generated_at`——后者只用于构建日志和 derived 统计。
- 详情页把「条目更新于」和「仓库最近提交」**并排**展示，是在回答两个不同问题：「我们刚补了资料」还是「作者刚发了新版」。后者是 GitHub 快照，可能滞后一天。
- **星标中位数 ≠ 合计**：中位数 = 把所有插件按星标排序取正中间那个；合计会被 DSH 本体这类超大仓库一次拉高。分母用 `gh_synced`（真有 GitHub 数据的条数），不是插件总数。
- **标签 count<3 不出页、不给 chip 链接**，`/tags/` 总览 `noindex,follow`，sitemap 由 `layouts/sitemap.xml` 自写。307 个标签里 247 个只挂 1 个插件，全是薄内容。
- **来源信息 2026-11-18 起全站下线**：`refs` / `sources.yaml` 只作内部去重台账，不得出现在 `derived.json`、`search.json` 或任何页面。
- `overflow-x:clip` 是兜底不是修复；正文里长文案必须自己能换行。
- 字体只下 **latin 子集**（112KB / 4 个 woff2），中文一律走系统栈；Newsreader 只用于西文标题/数字气质，不指望它排中文。
- 资源走 `assets/` + Hugo `fingerprint`，版本由内容决定；不要改回 `?v={{ now.Unix }}`（每次构建都换 URL，7 天 immutable 白设）。

### AdSense 是站点级，不是子目录级

`/dsh/` 跟 `ai.limzero.com` 是**同域子目录**，AdSense 按 `limzero.com` 一个 site 管理：

- 后台关 Anchor / Vignette / In-Feed → dsh **自动跟着好**，不用改代码、不用重部署（配置服务端下发，脚本每次加载读取）。
- 若主站要保留锚定广告赚 RPM → 在 Auto Ads 的**页面排除**里加 `limzero.com/dsh/*`，只豁免子站。
- 代码层兜底：`hugo.toml → [params.adsense] enabled = false`，dsh 彻底无广告（收益本来就极低）。

AdSense 那三个格式**代码关不掉**，不要再在模板里找地方插 `data-ad-format`。

---

## 五、遗留项与为什么不急着做

| 项 | 状态 | 判断 |
| --- | --- | --- |
| ~~AdSense 自动格式盖 header~~ | ✅ 2026-11-21 已解决 | 先全关（commit 1371b9d），同日改为**固定位手动广告**：`adsense.enabled=false`（不开 Auto Ads，锚定/插页格式不会下发）+ `[params.adsense.fixed] enabled=true`，只在文档流里放 4 类响应式固定单元（首页侧栏 / 详情页正文+侧栏 / 列表页上方），不 sticky、不悬浮，窄屏盖 header 的问题从根上消失。见下方「广告方案调整」。 |
| 广告方案调整（关 Auto Ads → 固定位） | ✅ 2026-11-21 已上线 | 用户随后要求「在合适位置加几个固定广告」。设计：Auto Ads 仍关，新增 `partials/ad.html` 统一渲染手动单元，落点 4 类（薄标签页与 about/privacy 不投）；slot 沿用主站三个真实 ID，模板与 client 不变。脚本加载保留、逐单元 push，`enable_page_level_ads` 全站为 0。 |
| 「最近收录」入口 | 未做 | 缺 `added_at` 字段；可从 git 历史推导（同 `entry_updated.py` 的做法），回访用户才能看出站还在更新 |
| 易混条目 / 替代关系 | 未做 | 缺 `confusable` 字段，要人工判定关系；「名字对不上」是首页开篇痛点，属于内容活不是代码活 |
| HTML 显式 `Cache-Control` | 未做 | 线上只有 `ETag` / `Last-Modified`；要改 1Panel 里 vhost 并 reload OpenResty，动服务器配置需用户确认 |
| 站内搜索浮层手机端入口 | 已修 | 原来 `.header-search` 在 `display:none`，现在详情页/分类页也能唤起 |

---

## 六、提交与上线记录

| commit | 内容 |
| --- | --- |
| `2b363f4` | P0/P1/P2 主体：溢出、字体、指纹、搜索、URL 状态、分页、SEO 结构化、薄标签治理、guide |
| `0444caa` | derived.json 构建时间戳对齐 |
| `4e2e70f` | 真实「条目更新于」+ 星标中位数说明 |
| `3913936` | 产物对齐（GitHub 提交天数自然漂移） |
| `ba87726` | 本复盘对应的 AGENTS.md 与文档指针 |

上线唯一路径 `bash deploy/deploy.sh`（构建 + rsync 到 `index/dsh/` + 线上 200 校验）。截至 2026-11-21 22:11，这些提交已由用户推到 `origin/main`；AI 侧仍遵守**只 add/commit、不 push**。
