---
title: dsh-super-kanban（Super Kanban 任务看板）
description: 从 DSH 多条会话里用 AI 自动提炼并维护任务看板：进展、阻塞、交付物随会话更新，待处理/待验收集中一处点一下跳回会话；支持全局/右侧/悬浮三种形态，可自建项目、时间线日程、带上下文续做和内置快聊，数据存本机无遥测。
categories:
- workflow
tags: &id001
- 看板
- 任务管理
- 多会话
- 验收
weight: 1010
params:
  plugin:
    id: dsh-super-kanban
    name: dsh-super-kanban（Super Kanban 任务看板）
    aliases:
    - Super Kanban
    - 智能任务指挥台
    - dsh-super-kanban
    category: workflow
    status: community
    repo: https://github.com/topmindspace/dsh-super-kanban
    install: dsh plugin --profile desktop add dsh-super-kanban@0.10.5
    summary: 从 DSH 多条会话里用 AI 自动提炼并维护任务看板：进展、阻塞、交付物随会话更新，待处理/待验收集中一处点一下跳回会话；支持全局/右侧/悬浮三种形态，可自建项目、时间线日程、带上下文续做和内置快聊，数据存本机无遥测。
    features:
    - AI 自动整理：增量扫描从会话提炼目标/进展/阻塞/交付物，建或更新任务卡，同一任务可关联多条会话；开自动扫描后会话轮次结束即触发更新
    - 待处理与待验收：集中看运行中/待审批/待回答/待审阅/阻塞/待验收，点卡片跳回会话；一轮结束就把待验收卡钉在悬浮入口上方，点对号才算确认验收
    - 三种形态：同一看板可占满主区域、停靠会话右侧或悬浮在对话上，同一时刻只显示一种；悬浮入口常驻可拖动可隐藏
    - 项目与日程：跨工作区建项目带备注/到期日/归档，时间线按日期回看状态与交付，日程盯截止
    - 带上下文续做：把验收条件、关键决策、未完成事项和产物生成草稿，放进关联会话或同工作区新会话，由你检查再发
    - 内置流式快聊：写提示词/解释/总结/润色/中英翻译，回答可复制、放入会话输入框、存为任务；记录只在当前窗口内存里，刷新即清空
    - 数据存本机、无遥测；默认只扫描最近 30 天有活动的会话，不自动翻全部历史
    tags: *id001
    flag: 文章安装写 @0.10.1，README 与 npm latest 是 0.10.5，本站按 README 用新版
    notes: 官方仓库 topmindspace/dsh-super-kanban，npm 包 dsh-super-kanban（latest 0.10.5，MIT）。安装三途：插件市场加索引源 https://topmindspace.github.io/dsh-super-kanban/index.json、插件页输包名、或 Git/本地目录；命令行安装前需完全退出 DSH，桌面端用 --profile desktop。装后启用插件并刷新 DSH。文章给的 0.10.1 是旧版，README 当前示例 0.10.5，按 README 取新。默认扫描最近 30 天活动会话，需要更久要自己调活跃周期或手动翻历史。封面图是功能示意、非实际界面。
    repo_confirmed: true
    gh:
      stars: 142
      forks: 14
      issues: 0
      language: JavaScript
      license: MIT
      pushed_at: '2026-11-26T05:09:11Z'
      archived: false
      slug: topmindspace/dsh-super-kanban
      stars_label: '142'
      forks_label: '14'
      pushed_date: '2026-11-26'
      updated_label: 昨天有提交
      updated_days: 1
      stale: false
    entry_updated: '2026-11-19'
    category_label: 协作与工作流
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-super-kanban/
  generated: true
lastmod: '2026-11-19'
---

从 DSH 多条会话里用 AI 自动提炼并维护任务看板：进展、阻塞、交付物随会话更新，待处理/待验收集中一处点一下跳回会话；支持全局/右侧/悬浮三种形态，可自建项目、时间线日程、带上下文续做和内置快聊，数据存本机无遥测。
