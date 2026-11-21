---
title: dsh-memory-palace（记忆宫殿）
description: 把 WorkBuddy 那套「记忆就是一个你能直接编辑的 Markdown 文件」搬进 DSH：用户级偏好与项目级约定分层存、跨会话常驻注入，AI 每轮自己整理今日日志，你随时能打开文件改它。
categories:
- memory
tags: &id001
- 跨会话记忆
- Markdown
- WorkBuddy 同构
weight: 1010
params:
  plugin:
    id: dsh-memory-palace
    name: dsh-memory-palace（记忆宫殿）
    aliases:
    - 记忆宫殿
    - memory palace
    - 文件式记忆
    category: memory
    status: community
    repo: https://github.com/lovezi0/dsh-memory-palace
    install: dsh plugin --profile web add github:lovezi0/dsh-memory-palace
    summary: 把 WorkBuddy 那套「记忆就是一个你能直接编辑的 Markdown 文件」搬进 DSH：用户级偏好与项目级约定分层存、跨会话常驻注入，AI 每轮自己整理今日日志，你随时能打开文件改它。
    features:
    - 双层记忆：用户级 ~/.deepseek-harness/MEMORY.md 管跨项目偏好，项目级管项目约定，互不干扰
    - 桥接 WorkBuddy / CodeBuddy：项目里已有 .workbuddy/memory 或 .codebuddy/memory 就直接读写那一套，不用维护两份
    - 记忆工具：memory_note / memory_note_user 章节化写入并去重、memory_read 按 scope 读、memory_delete 两阶段确认后删、memory_update_section 整节精确替换防 stale
    - 会话命令 /memory_reorganize（中文可打 /记忆重整）：全量重整项目记忆，双门禁（超注入预算 + 过冷却期）加原生确认，原文件自动整档备份
    - 注入策略：长期记忆与今日日志按「会话起始快照」注入，按文件身份各只注入一次，不破前缀缓存、压缩后自动重注最新版
    - 写入分工：记忆子代理每轮整理今日日志（章节化、标删），长期 MEMORY.md 留给主 AI 主动维护
    - 设置页集成：全部配置在 DSH 设置面板里按板块折叠调整，不必改配置文件
    - 自定义指令：不适合写进记忆的放 profile 里的 .memory-palace/user-commands.md，经系统提示词注入
    tags: *id001
    flag: 写的是你自己的文件，改之前先备份
    notes: 'CLI 推荐直接 github: 装（lib/ 构建产物随仓库分发，装即用）；锁版本加 #v1.8.6 这类 tag，改源码则 clone 后 npm run build 再本地 add。日志由子代理维护、永不过期不删，当证据层留着。兼容 DSH 0.2.2-rc.1 与桌面版。如果你本来就在用 WorkBuddy 的记忆目录，它会优先写那一份——等于两边共享同一套 MEMORY.md。'
    repo_confirmed: true
    gh:
      stars: 29
      forks: 3
      issues: 0
      language: JavaScript
      license: MIT
      pushed_at: '2026-11-17T14:18:38Z'
      archived: false
      slug: lovezi0/dsh-memory-palace
      stars_label: '29'
      forks_label: '3'
      pushed_date: '2026-11-17'
      updated_label: 3 天前有提交
      updated_days: 3
      stale: false
    category_label: 记忆与知识
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-memory-palace/
  generated: true
---

把 WorkBuddy 那套「记忆就是一个你能直接编辑的 Markdown 文件」搬进 DSH：用户级偏好与项目级约定分层存、跨会话常驻注入，AI 每轮自己整理今日日志，你随时能打开文件改它。
