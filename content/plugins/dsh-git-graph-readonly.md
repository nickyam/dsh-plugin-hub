---
title: dsh-git-graph（只读版）
description: DSH Web 原生右侧栏里的只读 Git 可视化：浏览提交拓扑、分支、标签、文件改动与历史版本源码，不需要 API Key，也不往会话里塞消息。刻意只读——不 stage、不 commit、不 push。
categories:
- tool
tags: &id001
- Git
- 只读
- 界面增强
weight: 1010
params:
  plugin:
    id: dsh-git-graph-readonly
    name: dsh-git-graph（只读版）
    aliases:
    - WhitePlusMS
    - 只读 Git 图
    category: tool
    status: community
    repo: https://github.com/WhitePlusMS/dsh-git-graph
    install: dsh plugin --profile web add https://github.com/WhitePlusMS/dsh-git-graph/releases/latest/download/dsh-git-graph.tgz
    summary: DSH Web 原生右侧栏里的只读 Git 可视化：浏览提交拓扑、分支、标签、文件改动与历史版本源码，不需要 API Key，也不往会话里塞消息。刻意只读——不 stage、不 commit、不 push。
    features:
    - 提交图：拓扑、分支、标签、HEAD、搜索与历史过滤，保持节点对齐
    - 分支导航：在下拉里搜本地 / 远程分支，聚焦单个分支并定位最新提交，但不改工作区
    - 子模块：在主仓库与直接子模块之间切换，图、提交详情与文件差异跟随选择
    - 提交详情：作者 / 提交者时间、父提交、引用、签名状态，引用做成可换行 chip
    - 文件改动：文件树 / 列表两种视图、单文件 diff、未提交改动；选两个提交可逐文件对比
    - 历史源码：按路径、提交哈希、行号与大小读取并复制旧版 / 新版文件全文
    - 外观：中英双语、明暗主题、分栏可拖、日期格式、行样式与配色预设，按仓库分别保存
    tags: *id001
    flag: 与 npm 上的 dsh-git-graph 是两个不同项目
    notes: 安装走 GitHub Release 的 tgz，不走 npm——npm 上那个 dsh-git-graph 属于另一位作者（enoughpower），是可写版本。要求 DSH 0.2.2-rc.1、Node.js 24.9+、宿主装 git 与 pnpm；0.6.1 起还对表过 0.2.1-rc.5 + Cordis 4.0.5，版本跨度大，装前先看 release 说明。默认搜索有 2000 提交的预算，超出会在界面上标注。
    repo_confirmed: true
    gh:
      stars: 6
      forks: 0
      issues: 0
      language: TypeScript
      license: MIT
      pushed_at: '2026-11-15T12:08:52Z'
      archived: false
      slug: WhitePlusMS/dsh-git-graph
      stars_label: '6'
      forks_label: '0'
      pushed_date: '2026-11-15'
    category_label: 工具与能力
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-git-graph-readonly/
  generated: true
---

DSH Web 原生右侧栏里的只读 Git 可视化：浏览提交拓扑、分支、标签、文件改动与历史版本源码，不需要 API Key，也不往会话里塞消息。刻意只读——不 stage、不 commit、不 push。
