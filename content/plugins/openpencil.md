---
title: openpencil
description: 把 OpenPencil 这款开源 AI 原生矢量设计工具接入 DSH 的插件：在对话里生成、预览、检查并修改真实 .op 矢量文档，带多画框精确渲染、只读交互画布与侧栏管理编辑器。
categories:
- visual
tags: &id001
- 矢量设计
- 协作
- DSH插件
weight: 1010
params:
  plugin:
    id: openpencil
    name: openpencil
    category: visual
    status: community
    repo: https://github.com/ZSeven-W/openpencil
    install: dsh plugin --profile web add @zseven-w/dsh-openpencil@latest
    summary: 把 OpenPencil 这款开源 AI 原生矢量设计工具接入 DSH 的插件：在对话里生成、预览、检查并修改真实 .op 矢量文档，带多画框精确渲染、只读交互画布与侧栏管理编辑器。
    features:
    - 提示词转画布：自然语言描述 UI，实时流式出现在无限画布；选中元素后用自然语言修改
    - 并发 Agent 团队：编排器把页面拆成空间子任务，多 Agent 并行生成（hero/features/footer 等）
    - 设计即代码：.op 文件为 JSON，可 Git 版本化、diff；可导出 React+Tailwind、HTML+CSS、Vue、Svelte、Flutter、SwiftUI 等
    - 风格指南：内置玻璃拟态、野兽派、复古等 50+ 风格，标签模糊匹配并接入生成流程
    - 多平台代码导出与可嵌入 SDK：导出多种前端框架；op-web-sdk 可在自有应用内嵌只读 .op 查看器
    tags: *id001
    flag: DSH 接入形态为同仓子包 @zseven-w/dsh-openpencil；本体 OpenPencil 是独立 Rust 设计 App
    notes: 仓库 ZSeven-W/openpencil 是 OpenPencil 设计工具本体（Rust 实现，非 DSH 插件）；其 DSH 插件以 @zseven-w/dsh-openpencil 包发布、与本体同仓。安装前以该 npm 包最新版本为准。README 另描述 DSH OpenPencil 作为「对话内 .op 预览 / 画布 / 管理编辑器」的能力。
    refs:
    - id: wx-quanjing
      title: DeepSeek Harness 插件全景推荐：14 大类、36 款值得装的插件
      url: https://mp.weixin.qq.com/s/btWqFHCDWwgAD_uj2n0MDw
      kind_label: 公众号
      publisher: 智宇AI说
    source_count: 1
    repo_confirmed: true
    category_label: 视觉与设计
    status_label: 社区
    weight: 1010
    url: /plugins/openpencil/
  generated: true
---

把 OpenPencil 这款开源 AI 原生矢量设计工具接入 DSH 的插件：在对话里生成、预览、检查并修改真实 .op 矢量文档，带多画框精确渲染、只读交互画布与侧栏管理编辑器。
