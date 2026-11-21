---
title: EverOS
description: EverOS 是面向 Agent 与开发者的本地优先、Markdown 原生长期记忆运行时，将对话、文件与 Agent 轨迹存为可读 Markdown，并同步本地 SQLite 与 LanceDB 索引以实现快速检索与跨应用自我演化；官方提供 DeepSeek Harness 集成插件。
categories:
- memory
tags: &id001
- 长期记忆
- 本地优先
- Markdown
- DSH
weight: 1020
params:
  plugin:
    id: everos
    name: EverOS
    category: memory
    status: community
    repo: https://github.com/EverMind-AI/EverOS
    install: pip install everos
    summary: EverOS 是面向 Agent 与开发者的本地优先、Markdown 原生长期记忆运行时，将对话、文件与 Agent 轨迹存为可读 Markdown，并同步本地 SQLite 与 LanceDB 索引以实现快速检索与跨应用自我演化；官方提供 DeepSeek Harness 集成插件。
    features:
    - Markdown 唯一事实来源：记忆以可读、可编辑、可 diff、可 Git 版本化的 .md 文件存储
    - 本地三层栈：Markdown + SQLite + LanceDB，无需 MongoDB / ES / Redis 等托管服务
    - 用户与 Agent 双轨：用户 episodes / profile 与 agent cases / skills 为独立的一等公民
    - 正交检索：可按 user_id / agent_id / app_id / project_id / session_id 多维检索
    - 离线反思（Reflection）：会话间合并 episode 簇、精炼 profile 与 skill，实现自我演化
    tags: *id001
    notes: 官方 DeepSeek Harness 集成插件维护在独立仓库 EverMind-AI/plugins（dsh 分支），本仓库为 EverOS 核心记忆运行时（pip 安装），DSH 插件不在本仓库根目录。
    repo_confirmed: true
    gh:
      stars: 13939
      forks: 978
      issues: 53
      language: Python
      license: Apache-2.0
      pushed_at: '2026-11-18T16:33:22Z'
      archived: false
      slug: EverMind-AI/EverOS
      stars_label: 13.9k
      forks_label: '978'
      pushed_date: '2026-11-18'
      updated_label: 2 天前有提交
      updated_days: 2
      stale: false
    entry_updated: '2026-11-06'
    category_label: 记忆与知识
    status_label: 社区
    weight: 1020
    url: /plugins/everos/
  generated: true
---

EverOS 是面向 Agent 与开发者的本地优先、Markdown 原生长期记忆运行时，将对话、文件与 Agent 轨迹存为可读 Markdown，并同步本地 SQLite 与 LanceDB 索引以实现快速检索与跨应用自我演化；官方提供 DeepSeek Harness 集成插件。
