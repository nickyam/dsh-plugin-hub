---
title: dsh-plugin-gate
description: DSH 的安装安全门与数据保护守卫：在 dsh plugin add 之前用 60 条静态规则扫描插件源码（恶意脚本/凭证窃取/混淆/网络回连），并用 gate_guard 在执行 rm -rf 类危险命令前拦截或要求确认。
categories:
- security
tags: &id001
- 安装前扫描
- 安全
weight: 1020
params:
  plugin:
    id: dsh-plugin-gate
    name: dsh-plugin-gate
    category: security
    status: community
    repo: https://github.com/863683348/dsh-plugin-gate
    install: dsh plugin --profile web add dsh-plugin-gate
    summary: DSH 的安装安全门与数据保护守卫：在 dsh plugin add 之前用 60 条静态规则扫描插件源码（恶意脚本/凭证窃取/混淆/网络回连），并用 gate_guard 在执行 rm -rf 类危险命令前拦截或要求确认。
    features:
    - 60 条静态签名规则：覆盖安装脚本、混淆、权限读取、网络回连、硬编码密钥与供应链（Google OSV）
    - gate_scan：只读扫描本地目录或 npm tarball，绝不执行被扫代码、绝不写文件
    - gate_guard：执行 rm -rf 类危险命令前评估，按工作区边界与关键文件返回 BLOCK / WARN / PASS
    - gate_diff / gate_report：与基线对比新/已解决/变更的风险点，可导出 Markdown / JSON 报告
    - 上下文感知降级：注释与文档中的示例代码降为低危，密钥与 webhook 即便在注释中也仍标记
    tags: *id001
    notes: 网关只读、绝不执行被扫代码、绝不写文件；它是启发式签名扫描，可能漏检新型恶意代码或误报无辜代码，BLOCK/WARN 需自行复核。仅作安装前与危险命令前的额外护栏。
    refs:
    - id: tree-top10
      title: 10 Best DeepSeek Harness Plugins for AI Developers in 2026
      url: https://api.treerouter.ai/en/blog/best-deepseek-harness-plugins-2026
      kind_label: 第三方媒体
      publisher: TreeRouter Blog（英文，第三方）
    - id: deepseekai-works
      title: 'DSH Plugins: What They Are, Where to Find Them, and How to Write One'
      url: https://deepseekai.works/plugins
      kind_label: 教程 / 指南
      publisher: deepseekai.works（第三方教程站）
    source_count: 2
    repo_confirmed: true
    category_label: 安全与治理
    status_label: 社区
    weight: 1020
    url: /plugins/dsh-plugin-gate/
  generated: true
---

DSH 的安装安全门与数据保护守卫：在 dsh plugin add 之前用 60 条静态规则扫描插件源码（恶意脚本/凭证窃取/混淆/网络回连），并用 gate_guard 在执行 rm -rf 类危险命令前拦截或要求确认。
