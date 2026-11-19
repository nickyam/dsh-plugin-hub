---
title: dsh-free-search
description: 给 DSH 接一批免 Key 的搜索 provider，替换默认那条要走 DeepSeek 官方 Key、用第三方模型也会隐形扣费的搜索通道；多引擎可切换、失败自动回退，还顺带接管网页抓取。
categories:
- tool
tags: &id001
- 搜索
- 免费
- 多引擎
weight: 1010
params:
  plugin:
    id: dsh-free-search
    name: dsh-free-search
    aliases:
    - 免费搜索
    - free-search
    - 多引擎搜索
    category: tool
    status: community
    repo: https://github.com/DDDMUC/dsh-free-search
    install: git clone https://github.com/DDDMUC/dsh-free-search.git && dsh plugin --profile web add ./dsh-free-search
    summary: 给 DSH 接一批免 Key 的搜索 provider，替换默认那条要走 DeepSeek 官方 Key、用第三方模型也会隐形扣费的搜索通道；多引擎可切换、失败自动回退，还顺带接管网页抓取。
    features:
    - 42 个引擎：DuckDuckGo、Bing、SearXNG、AnySearch、Exa、Tavily、Brave、智谱、秘塔、Kimi、元宝等，默认回退链覆盖 30 个
    - 失败分类冷却：额度 / 鉴权失败冷却本会话，反爬短退避，超时与 5xx 重试一次，多 Key 轮流并单独冷却
    - HTML SERP 引擎（默认关闭）：百度、360、搜狗、微信文章、头条，免 Key 但抓页面，撞反爬按 bot-wall 让整个家族冷却 10 分钟
    - Multi 模式：按查询语言并发对应语言池全部引擎，按 eTLD+1 合并去重，Fast / Balanced / Deep 三档
    - web_fetch 接管：直连 → 浏览器渲染 → exa / firecrawl → crawl4ai 质量链，拒私网、回环与云元数据地址
    - 平台与垂直直查：GitHub / V2EX / B站 / Reddit / HN / SO / npm / 掘金等平台搜索，41 个免 Key 垂直源（arXiv、Crossref、PubMed、NVD、SEC EDGAR、CoinGecko…）
    - research 一次成稿：多引擎并发 → 候选重排 → 分层抓取 → 段落选窗，带证据质量闸门
    - 网页设置页 + /free-search-engine 弹出切换；提示注入防护，网页文本包在 untrusted-web-content 边界内
    tags: *id001
    flag: 有 free 字样不代表每个后端都永久免费
    notes: 装的是宿主版本区间不是「越新越好」——engines.dsh 写死 >=0.2.1-rc.2 <0.4.0-0，0.1.x 与 0.4+ 会被插件管理器拒绝。README 只给 git clone 的本地路径装法（npm 上也有 dsh-free-search，现 0.9.70，作者 dddmuc）。它会自动接管 web.searchProvider 与 web.fetchProvider，可能把 provider 选择写进 profile，停用或卸载前要按文档把搜索与抓取配置恢复，否则配置仍指向已不存在的 provider。同时装多个搜索 / 抓取插件会互斥，设置页诊断会给警告。
    repo_confirmed: true
    gh:
      stars: 1404
      forks: 74
      issues: 9
      language: JavaScript
      license: MIT
      pushed_at: '2026-11-18T16:42:55Z'
      archived: false
      slug: DDDMUC/dsh-free-search
      stars_label: '1404'
      forks_label: '74'
      pushed_date: '2026-11-18'
    category_label: 工具与能力
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-free-search/
  generated: true
---

给 DSH 接一批免 Key 的搜索 provider，替换默认那条要走 DeepSeek 官方 Key、用第三方模型也会隐形扣费的搜索通道；多引擎可切换、失败自动回退，还顺带接管网页抓取。
