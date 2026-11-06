---
title: dsh-fabric
description: DSH 的「万物皆插件」运行时原语：用一套声明式 DSL 把所有可扩展接缝（工具、技能、提示段、事件监听、LLM 适配器、子代理、Web 路由等）收敛成可编程、可查询、可撤销的扩展能力，让「插件扩展插件」成为可能。
categories:
- tool
tags: &id001
- 运行时
- 扩展
- DSL
weight: 1010
params:
  plugin:
    id: dsh-fabric
    name: dsh-fabric
    category: tool
    status: community
    repo: https://github.com/hellosky983/dsh-fabric
    install: dsh plugin --profile web add github:hellosky983/dsh-fabric
    summary: DSH 的「万物皆插件」运行时原语：用一套声明式 DSL 把所有可扩展接缝（工具、技能、提示段、事件监听、LLM 适配器、子代理、Web 路由等）收敛成可编程、可查询、可撤销的扩展能力，让「插件扩展插件」成为可能。
    features:
    - 声明式 DSL 统一所有可扩展接缝（Service / Tool / Skill / Command / Prompt Section / Event Listener / LLM Adapter / Subagent Provider / Web Route / Settings Namespace / Projection）
    - fabric Service + 两个模型工具：fabric_extend 即时注册纯声明式扩展，fabric_inspect 实时盘点当前运行时挂了哪些能力
    - 插件开发者可用 ctx.get('fabric').register({...}) 注册任意带代码的扩展，统一追踪、统一清理
    - 对话中即可注册技能、提示段、变量，无需改文件
    - 能力图谱 UI 给出实时 census，扩展可查询、可撤销
    tags: *id001
    notes: 百科文章曾把它类比成《我的世界》的 Fabric Mod 加载器（社区把 DSH 生态比作 MC Mod 生态的注脚）；实际仓库是一个严肃的「运行时扩展」原语插件，并非游戏梗。本站按实际仓库 README 收录。
    refs:
    - id: baike-dsh
      title: 百度百科：DeepSeek Harness
      url: https://baike.baidu.com/item/deepseek%20harness/68533699
      kind_label: 百科
      publisher: 百度百科
    source_count: 1
    repo_confirmed: true
    category_label: 工具与能力
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-fabric/
  generated: true
---

DSH 的「万物皆插件」运行时原语：用一套声明式 DSL 把所有可扩展接缝（工具、技能、提示段、事件监听、LLM 适配器、子代理、Web 路由等）收敛成可编程、可查询、可撤销的扩展能力，让「插件扩展插件」成为可能。
