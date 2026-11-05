---
title: Agent loop（Agent 循环）
description: 官方内置的 Agent 循环，负责让任务一轮接一轮跑下去而不是聊完一句就散场。
categories:
- builtin
tags: &id001
- 官方内置
- 运行时
weight: 210
params:
  plugin:
    id: plugin-agent-loop
    name: Agent loop（Agent 循环）
    aliases:
    - Agent 循环
    category: builtin
    status: builtin
    summary: 官方内置的 Agent 循环，负责让任务一轮接一轮跑下去而不是聊完一句就散场。
    tags: *id001
    mentions:
    - source: wx-dabaihua
      stance: 印证
      quote: 中间这层「调度工具、管理任务、执行闭环」的系统，就叫 Harness……官方预置了子智能体、网页搜索、Agent 循环、终端四个插件。
      source_title: DeepSeek Harness 是个啥？大白话讲透 + 10 分钟上手 + 好用插件清单
      source_url: http://mp.weixin.qq.com/s?__biz=MzkwMDMzMzE0Mg==&mid=2247488511&idx=1&sn=b8f08d42ca17c2895080d4180cd3d6c9
      source_kind_label: 公众号
      source_publisher: 微信公众号（原文署名待补）
    - source: official-harness
      stance: 印证
      quote: 译述：官网 Plugins 面板列出 Agent loop；架构文档说明连 agent loop 本身也是可替换的插件，而非特权内核功能。
      source_title: DeepSeek Harness 官网：Everything is a plugin
      source_url: https://www.deepseek.com/en/harness/
      source_kind_label: 官方文档
      source_publisher: DeepSeek 官方
    source_count: 2
    has_conflict: false
    agreement: 多篇印证
    confidence: 中
    category_label: 官方内置能力
    status_label: 官方内置
    weight: 210
    url: /plugins/plugin-agent-loop/
  generated: true
---

官方内置的 Agent 循环，负责让任务一轮接一轮跑下去而不是聊完一句就散场。
