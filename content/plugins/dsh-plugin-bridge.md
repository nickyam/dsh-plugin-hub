---
title: dsh-plugin-bridge（跨预设会话交接）
description: 任务做到一半要换工具预设时，把会话状态迁移到干净的新预设——五段固定交接（目标 / 当前状态 / 关键决策与约定 / 关键文件 / 下一步）先预览、可编辑、人工确认后才执行，原会话不被改写。只搬决策、路径与现状，不带旧工具装配的调用痕迹；无法保证目标在启动前暂停时失败即关闭、不发模型请求。
categories:
- integration
tags: &id001
- 会话交接
- 跨预设
- 上下文迁移
- 工作流
weight: 1010
params:
  plugin:
    id: dsh-plugin-bridge
    name: dsh-plugin-bridge（跨预设会话交接）
    aliases:
    - 会话桥
    - 跨预设迁移
    - 会话交接
    category: integration
    status: community
    repo: https://github.com/Totoro-qaq/dsh-plugin-bridge
    install: dsh plugin --profile web add dsh-plugin-bridge
    summary: 任务做到一半要换工具预设时，把会话状态迁移到干净的新预设——五段固定交接（目标 / 当前状态 / 关键决策与约定 / 关键文件 / 下一步）先预览、可编辑、人工确认后才执行，原会话不被改写。只搬决策、路径与现状，不带旧工具装配的调用痕迹；无法保证目标在启动前暂停时失败即关闭、不发模型请求。
    features:
    - 五段固定交接：目标、当前状态、关键决策与约定、关键文件、下一步；0.3.10 起在窄屏也能保持确认按钮可达
    - 先预览后执行：/bridge <预设> 只生成草稿，不建目标会话、不改源会话，可编辑 Text/Markdown 再确认
    - 只搬状态不带工具痕迹：决策 / 路径 / 现状 / 下一步迁到干净预设，旧装配不兼容的调用留在源会话
    - 失败即关闭：目标会话在启动前暂停目标，若无法保证则清空 / 取消目标且不发任何模型请求
    - 三种入口：会话 ⋯ 菜单「交接会话」、可配快捷键、自然语言准备（bridge_prepare），保留 /bridge 命令；0.4.0 起支持在计划审查卡片上「在新会话中批准」
    tags: *id001
    flag: 官方 npm 包 dsh-plugin-bridge（MIT，Node >=22，latest 0.5.2）；兼容范围是安装准入区间而非逐版本实测承诺，README 明确 admission 不等于 acceptance
    notes: 官方仓库 github.com/Totoro-qaq/dsh-plugin-bridge（默认分支 main，npm 包 dsh-plugin-bridge，MIT，Node >=22，latest 0.5.2）。文章《dsh-plugin-bridge：会话换工具组，状态不丢》只给包名与「会话换工具组、状态不丢、五段固定交接」，与 README 核心定位吻合，据此收录；仓库与 README 按包名检索核实。安装命令按 README 用 dsh plugin --profile web add dsh-plugin-bridge。兼容范围按 README 校正：Bridge 0.5.2 的安装准入区间覆盖已发布的 DSH 0.2.2 线（含 0.2.2-rc.1），0.5.0 候选在隔离的 DSH 0.2.1-rc.2 Web 与原生 macOS Desktop 上做过验收；这是准入区间不是逐版本实测承诺，README 明确 admission 不等于 acceptance。前序草稿把 0.5.2 误写成 DSH 版本号、并用英文描述，本站按官方 README 改为中文并修正。常用命令：/bridge 列目标预设、/bridge code 预览、/bridge code --go 迁移后等待、--go --continue 确认下一步继续；卸载 dsh plugin --profile web remove dsh-plugin-bridge 后重启 dsh web。作者自建的第三方 Discover 索引源（Totoro-qaq/dsh-plugin-index）不是官方认证，要在每个 profile 单独添加。与站内 dsh-context（上下文可视化）、dsh-synapse（会话地图）定位不同：本条做的是跨预设状态迁移，未合并。
    repo_confirmed: true
    gh:
      stars: 168
      forks: 11
      issues: 6
      language: JavaScript
      license: MIT
      pushed_at: '2026-11-06T12:04:18Z'
      archived: false
      slug: Totoro-qaq/dsh-plugin-bridge
      stars_label: '168'
      forks_label: '11'
      pushed_date: '2026-11-06'
      stale: false
    entry_updated: '2026-11-25'
    category_label: 集成与迁移
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-plugin-bridge/
  generated: true
lastmod: '2026-11-25'
---

任务做到一半要换工具预设时，把会话状态迁移到干净的新预设——五段固定交接（目标 / 当前状态 / 关键决策与约定 / 关键文件 / 下一步）先预览、可编辑、人工确认后才执行，原会话不被改写。只搬决策、路径与现状，不带旧工具装配的调用痕迹；无法保证目标在启动前暂停时失败即关闭、不发模型请求。
