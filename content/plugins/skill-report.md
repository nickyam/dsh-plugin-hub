---
title: 技能调用报告
description: DSH 面板插件：统计每轮对话实际用到了哪些 skill，并让你在应用内直接安装、更新、停用、删除 skill。
categories:
- tool
tags: &id001
- 可观测
- Skill
weight: 1010
params:
  plugin:
    id: skill-report
    name: 技能调用报告
    category: tool
    status: community
    repo: https://github.com/VDERR/dsh-echocat-skill-panel
    install: dsh plugin --profile web add dsh-echocat-skill-panel
    summary: DSH 面板插件：统计每轮对话实际用到了哪些 skill，并让你在应用内直接安装、更新、停用、删除 skill。
    features:
    - 输入框上方横栏 + 左栏图标 + 中栏面板，共用一份数据，展示每轮用到 / 未用 / 调用次数统计
    - 判定不依赖模型自觉：从会话事件流推导本轮调了哪些 skill（模型自动、手动 /name、或没用）
    - 面板内直接安装 / 更新 / 停用 / 删除 skill（同名先备份再替换，删除进备份目录不硬删）
    - 安装来源写入 skill 的 .echocat.json（地址 / 分支 / commit / 内容指纹），支持更新检查
    - 一键「引用」把 /name 追加进输入框；中文显示名写 meta.yaml
    tags: *id001
    notes: 本条目对应仓库 dsh-echocat-skill-panel（依 README 整理；原文章仅以「技能调用报告」中文名提及）。README 提醒装完需重启 DSH Desktop Beta——host 半端在 boot 时快照进内存。
    refs:
    - id: wx-dabaihua
      title: DeepSeek Harness 是个啥？大白话讲透 + 10 分钟上手 + 好用插件清单
      url: http://mp.weixin.qq.com/s?__biz=MzkwMDMzMzE0Mg==&mid=2247488511&idx=1&sn=b8f08d42ca17c2895080d4180cd3d6c9
      kind_label: 公众号
      publisher: 微信公众号（原文署名待补）
    source_count: 1
    repo_confirmed: true
    category_label: 工具与能力
    status_label: 社区
    weight: 1010
    url: /plugins/skill-report/
  generated: true
---

DSH 面板插件：统计每轮对话实际用到了哪些 skill，并让你在应用内直接安装、更新、停用、删除 skill。
