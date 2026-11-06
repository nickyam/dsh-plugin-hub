---
title: ModSearch
description: DSH 里最强的免费联网搜索插件：网页搜索、X（推特）搜索、单页抓取，默认走 Firecrawl Keyless（每月 1000 免费额度，免注册免 API Key），为多模型补上原生缺失的联网能力，返回结构化 JSON 证据。
categories:
- tool
tags: &id001
- 搜索
- 免费
- 省成本
weight: 1020
params:
  plugin:
    id: modsearch
    name: ModSearch
    aliases:
    - modsearch
    category: tool
    status: community
    repo: https://github.com/liustack/modsearch
    install: npx -y @deepseek-ai/dsh plugin --profile web add @liustack/modsearch@5.10.11
    summary: DSH 里最强的免费联网搜索插件：网页搜索、X（推特）搜索、单页抓取，默认走 Firecrawl Keyless（每月 1000 免费额度，免注册免 API Key），为多模型补上原生缺失的联网能力，返回结构化 JSON 证据。
    features:
    - 免费开箱：默认 Firecrawl Keyless，1000 免费额度/月，无账号无 Key 无卡
    - 多引擎自动故障转移：Firecrawl / Keenable / You.com / Tavily / Exa / Grok(X) / 本地
    - 可配多 Key 轮转；支持 Antigravity CLI、自托管端点
    - X（Twitter）搜索（需 Grok Build）；搜索、抓取、引用一体
    tags: *id001
    notes: 与 dsh-websearch 属同类不同实现，本站不合并；官方自带网页搜索属开箱即用能力，不在收录范围。桌面端在 Plugins → Add plugin 输入 @liustack/modsearch。Key 存于 ~/.modsearch/config.json（权限 0600，显示时脱敏）。
    refs:
    - id: wx-dabaihua
      title: DeepSeek Harness 是个啥？大白话讲透 + 10 分钟上手 + 好用插件清单
      url: http://mp.weixin.qq.com/s?__biz=MzkwMDMzMzE0Mg==&mid=2247488511&idx=1&sn=b8f08d42ca17c2895080d4180cd3d6c9
      kind_label: 公众号
      publisher: 微信公众号（原文署名待补）
    - id: wx-quanjing
      title: DeepSeek Harness 插件全景推荐：14 大类、36 款值得装的插件
      url: https://mp.weixin.qq.com/s/btWqFHCDWwgAD_uj2n0MDw
      kind_label: 公众号
      publisher: 智宇AI说
    source_count: 2
    repo_confirmed: true
    category_label: 工具与能力
    status_label: 社区
    weight: 1020
    url: /plugins/modsearch/
  generated: true
---

DSH 里最强的免费联网搜索插件：网页搜索、X（推特）搜索、单页抓取，默认走 Firecrawl Keyless（每月 1000 免费额度，免注册免 API Key），为多模型补上原生缺失的联网能力，返回结构化 JSON 证据。
