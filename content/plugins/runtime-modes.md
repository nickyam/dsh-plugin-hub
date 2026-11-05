---
title: 四种运行模式
description: Standard（全工具集）、Code（用模型生成的 TypeScript 程序编排多步工具调用）、Minimal（只留两个工具做评测）、Creator（检查运行时、试挂载插件、编排新预设）。
categories:
- builtin
tags: &id001
- 官方内置
- 模式
- 架构
weight: 330
params:
  plugin:
    id: runtime-modes
    name: 四种运行模式
    aliases:
    - Standard / Code / Minimal / Creator
    - 标准 / 极简 / PTC / 创造
    category: builtin
    status: builtin
    summary: Standard（全工具集）、Code（用模型生成的 TypeScript 程序编排多步工具调用）、Minimal（只留两个工具做评测）、Creator（检查运行时、试挂载插件、编排新预设）。
    repo: https://github.com/deepseek-ai/deepseek-harness
    tags: *id001
    flag: PTC / Code 命名待核对
    notes: 不是单个插件，而是官方内置的可运行组合，收录在此便于和公众号里的说法对照。详细差异见「口径核对」页。
    mentions:
    - source: official-harness
      stance: 印证
      quote: 译述：Standard mode 包含完整工具集；Code mode 通过 Code Mode SDK 把工具暴露给模型，可在一段 TypeScript 程序里组合多步调用；Minimal mode 只保留持久 bash 与 str_replace_editor；Creator mode 支持运行时检查、内存里试插件、编排自定义预设。
      source_title: DeepSeek Harness 官网：Everything is a plugin
      source_url: https://www.deepseek.com/en/harness/
      source_kind_label: 官方文档
      source_publisher: DeepSeek 官方
    - source: wx-dabaihua
      stance: 有出入
      quote: 它预设了四种模式：标准模式干日常活，极简模式省 token，PTC 模式适合程序化批量处理，创造模式让 AI 自己组队、自己造插件。
      source_title: DeepSeek Harness 是个啥？大白话讲透 + 10 分钟上手 + 好用插件清单
      source_url: http://mp.weixin.qq.com/s?__biz=MzkwMDMzMzE0Mg==&mid=2247488511&idx=1&sn=b8f08d42ca17c2895080d4180cd3d6c9
      source_kind_label: 公众号
      source_publisher: 微信公众号（原文署名待补）
    - source: dsh-plugin-net
      stance: 补充
      quote: 译述：profile 是一种可运行的组合（如 web / headless），从空的插件树开始，按序叠加 bundle patch、profile patch、机器级 patch 与命令行 patch；后一层可覆盖前一层，卸载插件会撤销它注册的效果。
      source_title: What is a DSH plugin?（Plugin / Bundle / Profile 的区别）
      source_url: https://dsh-plugin.net/guides/what-is-dshplugin
      source_kind_label: 教程 / 指南
      source_publisher: dsh-plugin.net（社区，非官方）
    source_count: 3
    has_conflict: true
    agreement: 口径有出入
    confidence: 高
    category_label: 官方内置能力
    status_label: 官方内置
    weight: 330
    url: /plugins/runtime-modes/
  generated: true
---

Standard（全工具集）、Code（用模型生成的 TypeScript 程序编排多步工具调用）、Minimal（只留两个工具做评测）、Creator（检查运行时、试挂载插件、编排新预设）。
