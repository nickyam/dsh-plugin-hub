---
title: dsh-synapse
description: DSH 的可视化对话工作台，把同一工作区中的会话、追问和分支组织成一张可浏览、可拖拽、可缩放的地图，保留 DSH 原生会话作为唯一事实来源。
categories:
- ui
tags: &id001
- 画布
- 分支
- 非线性
weight: 1010
params:
  plugin:
    id: dsh-synapse
    name: dsh-synapse
    category: ui
    status: community
    repo: https://github.com/liangmianya/dsh-synapse
    install: dsh plugin --profile desktop add dsh-synapse
    summary: DSH 的可视化对话工作台，把同一工作区中的会话、追问和分支组织成一张可浏览、可拖拽、可缩放的地图，保留 DSH 原生会话作为唯一事实来源。
    features:
    - 对话地图：把连续追问、分支和不同会话放到同一张可操作的画布上
    - 保留真实分支：按 DSH 原生 fork 关系连接卡片，不制造另一套会话历史
    - 追问更顺手：选中回答中的文字可直接带入新的追问，常用补充词可编辑
    - 双向同步：在地图或 DSH 原生对话中切换会话，当前上下文保持一致
    - 过程不挡路：工具调用与结果按 callId 折叠进对应回答，只显示「工具 N」
    tags: *id001
    notes: 需 DeepSeek Harness >= 0.1.7-rc.2 与 Node.js >= 22.19.0；桌面 App 装完需重启，装到另一套 profile 时顶部看不到「会话地图」开关（把 --profile 换成另一套再装）。
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
    url: /plugins/dsh-synapse/
  generated: true
---

DSH 的可视化对话工作台，把同一工作区中的会话、追问和分支组织成一张可浏览、可拖拽、可缩放的地图，保留 DSH 原生会话作为唯一事实来源。
