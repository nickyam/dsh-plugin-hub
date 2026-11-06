---
title: dsh-diff-approval
description: 待处理改动审查插件：自动跟踪每次成功的 edit / write / str_replace_editor 改动，在侧边栏汇成待处理列表，可逐块、逐文件保留或回退，支持撤销/重做，并一键导入工作区版本控制的本地改动。
categories:
- workflow
tags: &id001
- 代码审阅
- 回滚
- 可追溯
weight: 1010
params:
  plugin:
    id: dsh-diff-approval
    name: dsh-diff-approval
    category: workflow
    status: community
    repo: https://github.com/9087/dsh-diff-approval
    install: dsh plugin --profile web add dsh-diff-approval
    summary: 待处理改动审查插件：自动跟踪每次成功的 edit / write / str_replace_editor 改动，在侧边栏汇成待处理列表，可逐块、逐文件保留或回退，支持撤销/重做，并一键导入工作区版本控制的本地改动。
    features:
    - 差异视图：语法高亮的整文件 diff，带 +/− 计数、滚动条总览尺与文件内搜索
    - 块导航与保留/回退：Ctrl+↑/↓ 跳转改动块，悬停可单独 Keep / Revert 某块
    - 选区框与整文件/批量决策：拖选一段行批量处理，文件可逐个或「全部保留/回退」
    - 撤销/重做：每次 keep、revert、import、comment 都可撤销
    - 导入版本控制改动：一键导入工作区 Git / SVN / Perforce 的本地未提交改动
    - 持久化：待处理状态按工作区存盘，重启后仍在
    tags: *id001
    notes: 纯前端审查，不修改你的文件；待处理状态存于 <dshHome>/diff-approval/workspaces/ 并跨重启保留。从 GitHub 源码安装可能需按提示配置 allowBuilds 构建授权。
    refs:
    - id: tree-top10
      title: 10 Best DeepSeek Harness Plugins for AI Developers in 2026
      url: https://api.treerouter.ai/en/blog/best-deepseek-harness-plugins-2026
      kind_label: 第三方媒体
      publisher: TreeRouter Blog（英文，第三方）
    source_count: 1
    repo_confirmed: true
    category_label: 协作与工作流
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-diff-approval/
  generated: true
---

待处理改动审查插件：自动跟踪每次成功的 edit / write / str_replace_editor 改动，在侧边栏汇成待处理列表，可逐块、逐文件保留或回退，支持撤销/重做，并一键导入工作区版本控制的本地改动。
