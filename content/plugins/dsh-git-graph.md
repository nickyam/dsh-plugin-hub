---
title: dsh-git-graph
description: 在会话区加一个「Git」页签，把分支栏、提交图、变更文件与差异视图放在同一面板，绑定当前会话的工作目录；不只是看图，还能切分支、暂存、提交、推送与拉取。
categories:
- tool
tags: &id001
- Git
- 界面增强
- 开发工具
weight: 1010
params:
  plugin:
    id: dsh-git-graph
    name: dsh-git-graph
    aliases:
    - Git 面板
    - git-graph
    - enoughpower
    category: tool
    status: community
    repo: https://github.com/enoughpower/dsh-git-graph
    install: dsh plugin --profile web add dsh-git-graph
    summary: 在会话区加一个「Git」页签，把分支栏、提交图、变更文件与差异视图放在同一面板，绑定当前会话的工作目录；不只是看图，还能切分支、暂存、提交、推送与拉取。
    features:
    - 工作区状态：分支信息 + 已暂存 / 未暂存 / 未跟踪三类文件，逐文件标 XY 状态码
    - 分支管理：列出本地与远程分支、切换、新建、删除、重命名、合并（可选 --no-ff）
    - 分支 / 标签统一下拉：按「本地分支 / 远程分支 / 标签」分组，选标签检出为 detached HEAD
    - 差异与提交：diff、stage / unstage / discard / remove、commit（选中文件或全部）、amend
    - 历史与溯源：log、graphLog、fileLog、blame、show / showStat / showFiles / showFileDiff
    - 远程与标签：push / pull / fetch（可 prune）、remotes、tags、conflicts
    - 移动端适配：窄屏自动单列堆叠（历史图 → 变更文件 → 差异），压缩顶栏与字号
    tags: *id001
    flag: 会真的改动仓库，不是只读看板
    notes: 与 WhitePlusMS 的同名项目不是同一个插件——npm 上的 dsh-git-graph（现 0.1.9）归属 enoughpower，可暂存、提交、推送；WhitePlusMS 那份是只读的 Git 图，从 GitHub Release 安装。装之前先认准来源，别把 A 的截图和 B 的安装命令拼一起。顺手提醒：dsh-better-sidebar 已内置只读提交图，只想看历史的话不必再加。所有 /git 操作限定在请求的 path 目录内，走 execFile 参数数组不引 shell，diff 截断 2 MiB。
    repo_confirmed: true
    gh:
      stars: 7
      forks: 3
      issues: 0
      language: JavaScript
      license: MIT
      pushed_at: '2026-10-27T09:57:58Z'
      archived: false
      slug: enoughpower/dsh-git-graph
      stars_label: '7'
      forks_label: '3'
      pushed_date: '2026-10-27'
      updated_label: 29 天前有提交
      updated_days: 29
      stale: false
    entry_updated: '2026-11-19'
    category_label: 工具与能力
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-git-graph/
  generated: true
---

在会话区加一个「Git」页签，把分支栏、提交图、变更文件与差异视图放在同一面板，绑定当前会话的工作目录；不只是看图，还能切分支、暂存、提交、推送与拉取。
