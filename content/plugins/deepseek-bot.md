---
title: DS Bot
description: DS Bot 是 DeepSeek Harness（DSH）的 Bot 插件，把 DSH 变成可创建和协作的 Bot：支持主 Bot、Bot 间消息与群聊，并内置记忆、共享能力库（MCP / Skill）与按时间 / 模型维度的用量统计。
categories:
- workflow
tags: &id001
- 多智能体
- Bot
- 长生命周期
weight: 1030
params:
  plugin:
    id: deepseek-bot
    name: DS Bot
    aliases:
    - DeepSeek-Bot
    - ds-bot
    - DSBot
    category: workflow
    status: community
    repo: https://github.com/Fei-Craft/DS-Bot
    install: 'npx @deepseek-ai/dsh@0.2.1-rc.5 plugin --profile web add ds-bot

      npx @deepseek-ai/dsh@0.2.1-rc.5 web

      '
    summary: DS Bot 是 DeepSeek Harness（DSH）的 Bot 插件，把 DSH 变成可创建和协作的 Bot：支持主 Bot、Bot 间消息与群聊，并内置记忆、共享能力库（MCP / Skill）与按时间 / 模型维度的用量统计。
    features:
    - 主 Bot 与工作小组：内置可管理其他 Bot 与群聊的「主 Bot」，一句话即可搭建 Bot 团队与群聊
    - Bot 记忆：每个 Bot 记住用户偏好并在后续工作中复用，可在详情页管理
    - 群聊目标驱动：群聊可由 admin 拆解任务、分阶段推进并基于证据检查
    - 共享能力库（Capabilities）：在设置里为 Bot 挂载 MCP server、Skill 与 pack
    - 办公文件处理：创建 / 编辑 .docx / .pptx / .xlsx，检查缺陷、做定向编辑与幻灯片重排
    tags: *id001
    notes: 仓库已由 DeepSeek-Bot 更名为 DS Bot，作者账号也从 Fei2411 迁到 Fei-Craft（当前地址 Fei-Craft/DS-Bot），旧地址靠 301 仍能跳到同一项目；DSH 插件包名为 ds-bot。与 dsh-agent-teams 是同类不同定位：后者偏任务分工，前者偏 Bot 的持久性与社交性（群聊）。
    repo_confirmed: true
    gh:
      stars: 9009
      forks: 913
      issues: 392
      language: JavaScript
      license: Apache-2.0
      pushed_at: '2026-11-26T18:50:45Z'
      archived: false
      slug: Fei-Craft/DS-Bot
      stars_label: '9009'
      forks_label: '913'
      pushed_date: '2026-11-26'
      stale: false
    entry_updated: '2026-11-27'
    category_label: 协作与工作流
    status_label: 社区
    weight: 1030
    url: /plugins/deepseek-bot/
  generated: true
lastmod: '2026-11-27'
---

DS Bot 是 DeepSeek Harness（DSH）的 Bot 插件，把 DSH 变成可创建和协作的 Bot：支持主 Bot、Bot 间消息与群聊，并内置记忆、共享能力库（MCP / Skill）与按时间 / 模型维度的用量统计。
