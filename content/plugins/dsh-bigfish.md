---
title: dsh-bigfish（大肥鱼桌宠）
description: 蹲在 DSH Web 右下角的一只可拖动大肥鱼，会跟着任务状态换动作：你交任务它就收工准备，它读文件搜索执行工具时气泡里能看到工具状态，等你确认时举牌，任务结束开心收工。角色能换，台词能改，动作能自己加。
categories:
- fun
tags: &id001
- 桌宠
- 状态可视化
- 角色包
weight: 1010
params:
  plugin:
    id: dsh-bigfish
    name: dsh-bigfish（大肥鱼桌宠）
    aliases:
    - 大肥鱼桌宠
    - bigfish
    - 桌宠
    category: fun
    status: community
    repo: https://github.com/gosomea/dsh-bigfish
    install: dsh plugin --profile web add dsh-bigfish
    summary: 蹲在 DSH Web 右下角的一只可拖动大肥鱼，会跟着任务状态换动作：你交任务它就收工准备，它读文件搜索执行工具时气泡里能看到工具状态，等你确认时举牌，任务结束开心收工。角色能换，台词能改，动作能自己加。
    features:
    - 101 类动作：原有 29 类加新增 72 段，配 13 种举牌小剧场、共 432 个新绘制姿态
    - 跟着真实状态走：交任务、读文件、跑工具、等确认、结束各有对应演出，气泡里显示工具状态与可自定义台词
    - 多会话不打架：同时跑几个会话时只跟随你当前打开的那个，后台完成不会抢前台状态，刷新历史不重播庆祝
    - 角色包可换：导入 .dshpet 或兼容 ZIP，自带「完整设置 → 角色库」预览所有动作
    - 自己做角色：附带 dsh-bigfish-pet-maker Skill，npx --yes dsh-bigfish install-skill 之后让 agent 生成新角色
    - 节奏可调：持续活动或 1–600 秒休息间隔，举牌可选多举 / 均衡 / 不举，展示时长 5–30 秒
    - 兼容性退让：遇到不认识的 DSH 会话接口就停在空闲状态，在气泡和设置里说明检测到的东西与升级建议，不猜任务状态
    tags: *id001
    flag: 与 dsh-pet 是两个项目，别装重了
    notes: 和本站已收的 dsh-pet（PC2005-cloud）不是一回事：dsh-pet 明确说「不轮询、不插桩、不感知任何东西」，只负责陪；dsh-bigfish 主打跟着任务状态演出，两只要一起装就得接受右下角有俩。Node 要 ^22.19.0 || >=24.0.0，只用 Web 界面。稳定版 0.6.0，另有 0.7 Web 预览版（散步与回家、互动玩具、三套小窝）。发布首日装到旧版是 pnpm 11 的 24 小时发布冷却，不是装错。作者在 macOS Apple Silicon + Node 24.19.0 上跑过 151 项单测、34 项 Chromium 回归与 DSH 0.2.0-rc.2 的 15 组隔离原生流程。
    repo_confirmed: true
    gh:
      stars: 31
      forks: 3
      issues: 0
      language: TypeScript
      license: NOASSERTION
      pushed_at: '2026-11-12T02:55:24Z'
      archived: false
      slug: gosomea/dsh-bigfish
      stars_label: '31'
      forks_label: '3'
      pushed_date: '2026-11-12'
      updated_label: 15 天前有提交
      updated_days: 15
      stale: false
    entry_updated: '2026-11-19'
    category_label: 娱乐与彩蛋
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-bigfish/
  generated: true
lastmod: '2026-11-19'
---

蹲在 DSH Web 右下角的一只可拖动大肥鱼，会跟着任务状态换动作：你交任务它就收工准备，它读文件搜索执行工具时气泡里能看到工具状态，等你确认时举牌，任务结束开心收工。角色能换，台词能改，动作能自己加。
