---
title: archify
description: 把想法、计划或代码库变成交互式图表的 agent skill；针对 DSH 提供社区维护的插件集成（@tt-a1i/archify-dsh），可在 DSH 对话里调用 archify 技能生成架构图、流程图、系统拓扑图。
categories:
- visual
tags: &id001
- 架构图
- 流程图
- 可视化
weight: 1010
params:
  plugin:
    id: archify
    name: archify
    category: visual
    status: community
    repo: https://github.com/tt-a1i/archify
    install: dsh plugin --profile web add @tt-a1i/archify-dsh@1.0.0
    summary: 把想法、计划或代码库变成交互式图表的 agent skill；针对 DSH 提供社区维护的插件集成（@tt-a1i/archify-dsh），可在 DSH 对话里调用 archify 技能生成架构图、流程图、系统拓扑图。
    features:
    - 多种交互式图表：支持架构图、工作流、序列图、数据流、ERD、类图等 10 种，从文字描述或真实代码库生成可探索的独立 HTML
    - 类型化 JSON IR 与原子校验：每种渲染模式有 schema 与可复现源，失败返回带稳定规则代码与修复建议的机器可读 JSON 收据
    - 真实交互与溯源：支持聚焦节点、上下游追踪、精确路由高亮；可选源证据模式把节点标记到公开提交代码行，不捏造拓扑
    - 默认可移植易分享：输出单 HTML 文件，可导出 PNG/WebP/JPG 长图、PDF 或分享卡
    - 广泛 Agent 兼容：原生支持 Claude Code / Codex / Cursor / OpenCode，并通过插件扩展至 DSH 等环境
    tags: *id001
    flag: 社区集成，非 DeepSeek 官方产品；实际 DSH 包名 @tt-a1i/archify-dsh
    notes: README 声明该 DSH 集成是 Community integration，无遥测，需 Node ^22.19.0 || >=24.0.0。移除命令：dsh plugin --profile web remove @tt-a1i/archify-dsh。
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
    url: /plugins/archify/
  generated: true
---

把想法、计划或代码库变成交互式图表的 agent skill；针对 DSH 提供社区维护的插件集成（@tt-a1i/archify-dsh），可在 DSH 对话里调用 archify 技能生成架构图、流程图、系统拓扑图。
