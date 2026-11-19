---
title: '@busabase/dsh-plugin'
description: 把 DSH 连接到 Busabase，让 Agent 读取可信知识、处理结构化数据，并把每次提议的写入提交人工审查（changeRequest），在不静默改写真源的同时赋予持久上下文。
categories:
- memory
tags: &id001
- 知识库
- 数据库
weight: 1010
params:
  plugin:
    id: dsh-basabase
    name: '@busabase/dsh-plugin'
    category: memory
    status: community
    repo: https://github.com/busabase/busabase-dsh-plugin
    install: npx @deepseek-ai/dsh plugin --profile web add @busabase/dsh-plugin
    summary: 把 DSH 连接到 Busabase，让 Agent 读取可信知识、处理结构化数据，并把每次提议的写入提交人工审查（changeRequest），在不静默改写真源的同时赋予持久上下文。
    features:
    - 可信知识：搜索已批准的 Docs / Files / Bases / Records / 评论等对象，给 Agent 可靠信息源
    - 结构化工作：把自然语言请求转成提议的 Bases、Forms、AirApps 与记录
    - 实用结果：把 Busabase 实体渲染成带实时 Inspector 的对话卡片，而非原始 JSON
    - 人工控制：把 Agent 写入权限锁在 changeRequest 级别，每次审查与合并都留给人类
    tags: *id001
    notes: 原列表写作 @basabase/dsh-plugin，实际 npm 包 / 仓库为 busabase（busabase/busabase-dsh-plugin、@busabase/dsh-plugin），已按官方名称修正。Local 模式零配置默认，Cloud 模式走浏览器 OAuth。
    repo_confirmed: true
    gh:
      stars: 11
      forks: 0
      issues: 0
      language: TypeScript
      license: MIT
      pushed_at: '2026-10-31T19:54:51Z'
      archived: false
      slug: busabase/busabase-dsh-plugin
      stars_label: '11'
      forks_label: '0'
      pushed_date: '2026-10-31'
    category_label: 记忆与知识
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-basabase/
  generated: true
---

把 DSH 连接到 Busabase，让 Agent 读取可信知识、处理结构化数据，并把每次提议的写入提交人工审查（changeRequest），在不静默改写真源的同时赋予持久上下文。
