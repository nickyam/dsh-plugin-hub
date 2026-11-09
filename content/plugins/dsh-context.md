---
title: dsh-context
description: 一站式 DeepSeek Harness 上下文可视化插件，提供 Context 面板、浏览器、侧栏与命令，透视上下文的组成、演进、压缩与多 Agent 协作。
categories:
- workflow
tags: &id001
- 上下文
- 可观测
- 诊断
weight: 1020
params:
  plugin:
    id: dsh-context
    name: dsh-context
    category: workflow
    status: community
    repo: https://github.com/bowenliang123/dsh-context
    install: dsh plugin --profile web add dsh-context
    summary: 一站式 DeepSeek Harness 上下文可视化插件，提供 Context 面板、浏览器、侧栏与命令，透视上下文的组成、演进、压缩与多 Agent 协作。
    features:
    - 上下文洞察页面：跨会话总览的一级侧边栏面板，含 KPI 栏、活动热力图、汇总组成环形图与会话卡片
    - Context 标签页：上下文统计、组成、逐请求趋势、事件、文件活动与命令执行的仪表板
    - Fleet 标签页：Agent 家族专页，当前 Agent、父级与每个子 Agent 实时卡片呈现
    - Context 面板：右侧边栏标签页，聊天旁打开并含 Agent 网络
    - /context 命令：斜杠命令显示当前上下文组成与近期演变
    tags: *id001
    notes: 需 @deepseek-ai/dsh 0.2.0-rc.2 及以上（各版本支持见 docs/compatibility.md）；数值采用 dsh 自身 Token 计量投影，与内置计量器一致。UI 支持简中 / 英 / 日等多语言（切换需 dsh 0.2.2+）。
    refs:
    - id: wx-quanjing
      title: DeepSeek Harness 插件全景推荐：14 大类、36 款值得装的插件
      url: https://mp.weixin.qq.com/s/btWqFHCDWwgAD_uj2n0MDw
      kind_label: 公众号
      publisher: 智宇AI说
    - id: wx-feishu
      title: 3.5 万个插件里，DeepSeek 官方为什么只挑了这 4 个?
      url: https://mp.weixin.qq.com/s/pdJ8cQW1Ua_jhtRR7wR8iQ
      kind_label: 公众号
      publisher: 飞叔（公众号：飞叔 AI赋能推客）
    source_count: 2
    repo_confirmed: true
    category_label: 协作与工作流
    status_label: 社区
    weight: 1020
    url: /plugins/dsh-context/
  generated: true
---

一站式 DeepSeek Harness 上下文可视化插件，提供 Context 面板、浏览器、侧栏与命令，透视上下文的组成、演进、压缩与多 Agent 协作。
