---
title: dsh-plugin-gate
description: 装插件前先扫本地目录与 npm 包：安装脚本、权限要求、密钥、外连请求，给出 BLOCK / WARN / PASS 判定。
categories:
- security
tags: &id001
- 安装前扫描
- 安全
weight: 200
params:
  plugin:
    id: dsh-plugin-gate
    name: dsh-plugin-gate
    category: security
    status: community
    summary: 装插件前先扫本地目录与 npm 包：安装脚本、权限要求、密钥、外连请求，给出 BLOCK / WARN / PASS 判定。
    tags: *id001
    notes: 第三方教程站也提醒：允许 prepare 脚本等于允许包代码在 Agent 沙箱外的宿主机上运行，只应信任审查过的包并固定 commit。
    mentions:
    - source: tree-top10
      stance: 仅提及
      quote: 译述：执行 dsh plugin add 之前，dsh-plugin-gate 会扫描本地目录和 npm 包，检查安装脚本、权限需求、密钥与对外网络连接，返回 BLOCK、WARN、PASS 三级判定。
      source_title: 10 Best DeepSeek Harness Plugins for AI Developers in 2026
      source_url: https://api.treerouter.ai/en/blog/best-deepseek-harness-plugins-2026
      source_kind_label: 第三方媒体
      source_publisher: TreeRouter Blog（英文，第三方）
    - source: deepseekai-works
      stance: 补充
      quote: 译述：pnpm 10 起默认拦截 prepare 脚本，要在 profile 的 pnpm-workspace.yaml 里显式 allowBuilds；放行等于允许包代码在 Agent 沙箱外的宿主机执行，官方建议只信任审查过的包并用 github:you/hello-plugin#<commit> 固定版本。
      source_title: 'DSH Plugins: What They Are, Where to Find Them, and How to Write One'
      source_url: https://deepseekai.works/plugins
      source_kind_label: 教程 / 指南
      source_publisher: deepseekai.works（第三方教程站）
    source_count: 2
    has_conflict: false
    agreement: 多篇印证
    confidence: 中
    category_label: 安全与治理
    status_label: 社区
    weight: 200
    url: /plugins/dsh-plugin-gate/
  generated: true
---

装插件前先扫本地目录与 npm 包：安装脚本、权限要求、密钥、外连请求，给出 BLOCK / WARN / PASS 判定。
