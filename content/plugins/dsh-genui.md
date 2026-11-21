---
title: dsh-genui
description: 面向 DSH 的生成式 UI 插件，将助手回复转化为安全、完全交互式的 UI 界面，在模型文本回复旁内联渲染图表、表单、测验、Mermaid 图与 3D 场景等组件。
categories:
- ui
tags: &id001
- GenUI
- 内联渲染
- 可视化
weight: 1030
params:
  plugin:
    id: dsh-genui
    name: dsh-genui
    category: ui
    status: community
    repo: https://github.com/omdsh-dev/dsh-genui
    install: dsh plugin --profile web add @changfenhuang/dsh-genui
    summary: 面向 DSH 的生成式 UI 插件，将助手回复转化为安全、完全交互式的 UI 界面，在模型文本回复旁内联渲染图表、表单、测验、Mermaid 图与 3D 场景等组件。
    features:
    - 流式与实时挂载：组件随 token 到达即增量挂载，无需等待完整回复
    - 30+ 组件生态：统计卡片、高级表格、ECharts 图表、数学函数绘图（带实时参数滑杆）、Mermaid 与轻量 3D 模型
    - 本地优先零延迟交互：排序、筛选、滑杆重绘等状态转换完全在客户端执行，不往返模型
    - 双向动作事件循环：带 action 负载的交互元素可将用户事件回传模型，触发后续推理
    tags: *id001
    notes: npm 包名现为 @changfenhuang/dsh-genui，旧包 @omdsh-dev/dsh-genui 已弃用，需先移除再重装新包。
    repo_confirmed: true
    gh:
      stars: 1024
      forks: 101
      issues: 10
      language: TypeScript
      license: MIT
      pushed_at: '2026-11-18T10:45:24Z'
      archived: false
      slug: omdsh-dev/dsh-genui
      stars_label: '1024'
      forks_label: '101'
      pushed_date: '2026-11-18'
      updated_label: 2 天前有提交
      updated_days: 2
      stale: false
    category_label: 界面与体验
    status_label: 社区
    weight: 1030
    url: /plugins/dsh-genui/
  generated: true
---

面向 DSH 的生成式 UI 插件，将助手回复转化为安全、完全交互式的 UI 界面，在模型文本回复旁内联渲染图表、表单、测验、Mermaid 图与 3D 场景等组件。
