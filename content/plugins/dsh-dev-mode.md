---
title: dsh-dev-mode（开发模式流水线）
description: 给 DSH 装上开发模式：几句大白话讲需求，它走开工体检 → 写计划 → 独立评审 → 后台实现与自测 → 独立测试 → 修复 → 复测 → 交付的多阶段流水线；你说不清要什么时先给三个具体示例让你选，全程最多问一轮。
categories:
- workflow
tags: &id001
- 开发模式
- 编程
- 子代理
- 流水线
weight: 1010
params:
  plugin:
    id: dsh-dev-mode
    name: dsh-dev-mode（开发模式流水线）
    aliases:
    - Developer Mode
    - 白话开发
    category: workflow
    status: community
    repo: https://github.com/lingyingaojue/dsh-dev-mode
    install: dsh plugin --profile web add github:lingyingaojue/dsh-dev-mode
    summary: 给 DSH 装上开发模式：几句大白话讲需求，它走开工体检 → 写计划 → 独立评审 → 后台实现与自测 → 独立测试 → 修复 → 复测 → 交付的多阶段流水线；你说不清要什么时先给三个具体示例让你选，全程最多问一轮。
    features:
    - 七阶段流水线：体检 → 计划 → 评审 → 实现自测 → 独立测试 → 修复 → 复测交付
    - 需求不清先举例：说不清时给三个具体示例让你选，最多问一轮
    - 原生子代理：基于 native-subagent 编排，评审与测试分角色独立执行
    tags: *id001
    flag: 社区项目；要求 DSH 0.2.2+、Windows 10/11；会在工作目录改文件跑命令，建议在空目录或独立项目目录使用
    notes: 仓库 lingyingaojue/dsh-dev-mode——文章在装机章节明确给出 github:lingyingaojue/dsh-dev-mode，与 GitHub 搜索精确命中一致。README 标注 DSH 0.2.2+、平台 Windows 10/11（npm 未发布，按 git 安装）。GitHub 另有 OugeX/dsh-web-dev-mode 等不同项目，本条取文章点名仓库。
    repo_confirmed: true
    gh:
      stars: 4
      forks: 0
      issues: 0
      language: JavaScript
      license: MIT
      pushed_at: '2026-11-14T15:01:52Z'
      archived: false
      slug: lingyingaojue/dsh-dev-mode
      stars_label: '4'
      forks_label: '0'
      pushed_date: '2026-11-14'
      updated_label: 11 天前有提交
      updated_days: 11
      stale: false
    entry_updated: '2026-11-17'
    category_label: 协作与工作流
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-dev-mode/
  generated: true
---

给 DSH 装上开发模式：几句大白话讲需求，它走开工体检 → 写计划 → 独立评审 → 后台实现与自测 → 独立测试 → 修复 → 复测 → 交付的多阶段流水线；你说不清要什么时先给三个具体示例让你选，全程最多问一轮。
