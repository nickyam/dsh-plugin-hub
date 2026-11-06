---
title: dsh-find-plugin
description: 一个「找插件的插件」——让 Agent 在对话里搜索 GitHub 上的 DSH 插件生态，按星标排序返回结果，每条带一行简介和可直接执行的安装命令。
categories:
- market
tags: &id001
- 命令行
- GitHub
- 发现
weight: 1010
params:
  plugin:
    id: dsh-find-plugin
    name: dsh-find-plugin
    category: market
    status: community
    repo: https://github.com/awesome-dsh-plugin/dsh-find-plugin
    install: dsh plugin --profile web add dsh-find-plugin
    summary: 一个「找插件的插件」——让 Agent 在对话里搜索 GitHub 上的 DSH 插件生态，按星标排序返回结果，每条带一行简介和可直接执行的安装命令。
    features:
    - 会话内搜索 GitHub 上的 DSH 插件生态（限定官方 dsh-plugin topic）
    - 结果按星标排序，每条带一行简介与可执行的安装命令
    - 1 小时按查询缓存 + 离线快照（awesome-dsh-plugin 精选列表兜底）
    - 'lib 已提交仓库，github: 安装无需构建审批即可落地'
    tags: *id001
    notes: 官方唯一的发现机制是 GitHub topic dsh-plugin，第三方目录站均非官方。
    refs:
    - id: tree-top10
      title: 10 Best DeepSeek Harness Plugins for AI Developers in 2026
      url: https://api.treerouter.ai/en/blog/best-deepseek-harness-plugins-2026
      kind_label: 第三方媒体
      publisher: TreeRouter Blog（英文，第三方）
    source_count: 1
    repo_confirmed: true
    category_label: 插件市场与发现
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-find-plugin/
  generated: true
---

一个「找插件的插件」——让 Agent 在对话里搜索 GitHub 上的 DSH 插件生态，按星标排序返回结果，每条带一行简介和可直接执行的安装命令。
