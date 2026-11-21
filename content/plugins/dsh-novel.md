---
title: dsh-novel（标准小说工作台）
description: 标准化小说创作插件：一个工作区目录就是一本书，人物、世界观、大纲和章节落在同一份 canon（设定正典）里，Agent 通过工具读写、你在 Web UI「内容」页侧栏核对，避免长篇写到后面设定崩、看不见前文。
categories:
- content
tags: &id001
- 小说
- 长文
- 设定管理
- 创作
weight: 1010
params:
  plugin:
    id: dsh-novel
    name: dsh-novel（标准小说工作台）
    aliases:
    - 小说插件
    - DSH Novel
    category: content
    status: community
    repo: https://github.com/ddedook/dsh-novel
    install: dsh plugin --profile web add dsh-novel
    summary: 标准化小说创作插件：一个工作区目录就是一本书，人物、世界观、大纲和章节落在同一份 canon（设定正典）里，Agent 通过工具读写、你在 Web UI「内容」页侧栏核对，避免长篇写到后面设定崩、看不见前文。
    features:
    - 目录即书：一个工作区目录 = 一本小说，人物 / 世界 / 大纲 / 章节统一落在 canon，防止设定穿帮
    - 侧栏核对：在官方 Web UI 会话的「内容」页查看人物档案与章节，Agent 写、你来核对
    - 本地存储：用 PGlite 在工作区内保存数据
    tags: *id001
    flag: 社区项目；数据存本地工作区，注意备份
    notes: 仓库 ddedook/dsh-novel，npm 已发布 dsh-novel（registry 200），README 同时给 dsh plugin add github:ddedook/dsh-novel 与 dsh plugin add dsh-novel 两种方式，本站 install 用 npm 稳定版。文章把小说拆成 dsh-novel（标准化）与 dsh-novel-craft（偏好学习）两条，本站按两个独立仓库分别建条目。GitHub 另有 huangziyuan-general/dsh-novel-forge 等不同实现，本条取文章点名的 dsh-novel 名字精确主仓。
    repo_confirmed: true
    gh:
      stars: 7
      forks: 0
      issues: 0
      language: TypeScript
      license: MIT
      pushed_at: '2026-10-24T13:22:24Z'
      archived: false
      slug: ddedook/dsh-novel
      stars_label: '7'
      forks_label: '0'
      pushed_date: '2026-10-24'
      updated_label: 27 天前有提交
      updated_days: 27
      stale: false
    entry_updated: '2026-11-17'
    category_label: 内容创作与办公
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-novel/
  generated: true
---

标准化小说创作插件：一个工作区目录就是一本书，人物、世界观、大纲和章节落在同一份 canon（设定正典）里，Agent 通过工具读写、你在 Web UI「内容」页侧栏核对，避免长篇写到后面设定崩、看不见前文。
