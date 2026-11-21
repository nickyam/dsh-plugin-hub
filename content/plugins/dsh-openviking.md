---
title: dsh-openviking（用户画像与记忆）
description: 把火山引擎开源的 OpenViking 接进 DSH：user + agent 双空间的检索、资源管理、自动召回与会话记忆，每轮执行前可先翻一遍你的画像（如「中文、简洁」），越用越懂你；需本地跑一个 OpenViking 服务（默认 http://localhost:1933）。
categories:
- memory
tags: &id001
- OpenViking
- 用户画像
- 会话记忆
- 自动召回
weight: 1020
params:
  plugin:
    id: dsh-openviking
    name: dsh-openviking（用户画像与记忆）
    aliases:
    - OpenViking
    - dsh-openviking
    - 用户画像
    - 会话记忆
    category: memory
    status: community
    repo: https://github.com/Rxiain/dsh-openviking
    install: dsh plugin --profile web add github:Rxiain/dsh-openviking
    summary: 把火山引擎开源的 OpenViking 接进 DSH：user + agent 双空间的检索、资源管理、自动召回与会话记忆，每轮执行前可先翻一遍你的画像（如「中文、简洁」），越用越懂你；需本地跑一个 OpenViking 服务（默认 http://localhost:1933）。
    features:
    - 双空间记忆：user / agent 双空间的语义搜索（memsearch，含 deep 模式带会话上下文）、快速查找（memfind）、读取 viking:// URI（memread）与浏览文件系统（membrowse）
    - 自动召回：通过上下文注入通道在每轮前自动召回相关记忆与已索引仓库上下文，带总 token 预算、去重与长度上限
    - 流程经验召回：对审计/修复/迁移等流程类问题启用 procedure lane，按方法论 / playbook / workflow / runbook 等标记筛选流程分支
    - 记忆沉淀：memcommit 提交会话提取持久记忆，memlearn 主动写/合并记忆或铸 skill playbook（脱敏+查重+即时注入）；观察者队列自动做嵌入、摘要与内容重组
    - 安装方式：DSH 0.1.7+ 可在插件管理页直接装；CLI 可用 sh install.sh 或 dsh plugin --profile <name> add github:Rxiain/dsh-openviking
    tags: *id001
    flag: 社区项目；依赖本地 OpenViking 服务（默认 localhost:1933），不是装了就能用；Node ^22.19.0 || >=24，DSH >=0.1.7-rc.2
    notes: 仓库 Rxiain/dsh-openviking，底层对接火山引擎开源的 OpenViking（github.com/volcengine/OpenViking），本插件是 DSH 侧对接层；GitHub 上另有 dsh-openviking-expand / dsh-memory-openviking 等近似项目，本条取 README 完整、★ 数最高的 Rxiain 主仓。文章把它描述为「用户画像」，README 里对应 user 空间记忆 + 自动召回，本站按 README 写。
    repo_confirmed: true
    gh:
      stars: 22
      forks: 4
      issues: 1
      language: JavaScript
      license: MIT
      pushed_at: '2026-09-29T14:14:43Z'
      archived: false
      slug: Rxiain/dsh-openviking
      stars_label: '22'
      forks_label: '4'
      pushed_date: '2026-09-29'
      updated_label: 1 个月前有提交
      updated_days: 53
      stale: false
    entry_updated: '2026-11-17'
    category_label: 记忆与知识
    status_label: 社区
    weight: 1020
    url: /plugins/dsh-openviking/
  generated: true
---

把火山引擎开源的 OpenViking 接进 DSH：user + agent 双空间的检索、资源管理、自动召回与会话记忆，每轮执行前可先翻一遍你的画像（如「中文、简洁」），越用越懂你；需本地跑一个 OpenViking 服务（默认 http://localhost:1933）。
