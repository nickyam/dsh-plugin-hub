---
title: dsh-TUI
description: DSH 的交互式终端 UI，内置像素鲸鱼头部、实时工作状态、流式思考、双击 Esc 时间回溯、上下文进度条与 TPS 仪表盘；零核心改动，仅消费 DSH 公共导出。
categories:
- ui
tags: &id001
- 终端
- TUI
- 轻量
weight: 1010
params:
  plugin:
    id: dsh-tui
    name: dsh-TUI
    category: ui
    status: community
    repo: https://github.com/ccch1mneyyy/dsh-TUI
    install: dsh plugin --profile dsh-tui add @deepseek-harness-tui/dsh-tui
    summary: DSH 的交互式终端 UI，内置像素鲸鱼头部、实时工作状态、流式思考、双击 Esc 时间回溯、上下文进度条与 TPS 仪表盘；零核心改动，仅消费 DSH 公共导出。
    features:
    - 像素鲸鱼宠物：三次开场动画，点击唤醒，首次任务后冻结
    - 终端原生 UI：流式 Markdown、工具卡片、/ 与 @ 补全、#L12-14 行号范围、历史搜索与中英文界面切换
    - 侧边面板：终端够宽时 Ctrl+B 分屏出面板列，八个内置面板默认启用
    - 实时状态展示：活动动画、上下文占用条、TPS、缓存命中率、推理强度、令牌消耗与会话成本估算
    tags: *id001
    notes: 安装即启用，卸载不留补丁；README 提及其正从挂载插件演进为带独立入口的 app，需匹配当前验证线版本的 DSH。
    refs:
    - id: wx-quanjing
      title: DeepSeek Harness 插件全景推荐：14 大类、36 款值得装的插件
      url: https://mp.weixin.qq.com/s/btWqFHCDWwgAD_uj2n0MDw
      kind_label: 公众号
      publisher: 智宇AI说
    source_count: 1
    repo_confirmed: true
    category_label: 界面与体验
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-tui/
  generated: true
---

DSH 的交互式终端 UI，内置像素鲸鱼头部、实时工作状态、流式思考、双击 Esc 时间回溯、上下文进度条与 TPS 仪表盘；零核心改动，仅消费 DSH 公共导出。
