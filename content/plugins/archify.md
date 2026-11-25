---
title: archify
description: 把想法、计划或代码库变成交互式图表的 agent skill；针对 DSH 提供社区维护的插件集成（@tt-a1i/archify-dsh），可在 DSH 对话里调用 archify 技能生成架构图、流程图、系统拓扑图。
categories:
- visual
tags: &id001
- 架构图
- 流程图
- 可视化
weight: 1030
params:
  plugin:
    id: archify
    name: archify
    category: visual
    status: community
    repo: https://github.com/tt-a1i/archify
    install: dsh plugin --profile web add @tt-a1i/archify-dsh@1.2.0
    summary: 把想法、计划或代码库变成交互式图表的 agent skill；针对 DSH 提供社区维护的插件集成（@tt-a1i/archify-dsh），可在 DSH 对话里调用 archify 技能生成架构图、流程图、系统拓扑图。
    features:
    - 多种交互式图表：支持架构图、工作流、序列图、数据流、ERD、类图等 10 种，从文字描述或真实代码库生成可探索的独立 HTML
    - 类型化 JSON IR 与原子校验：每种渲染模式有 schema 与可复现源，失败返回带稳定规则代码与修复建议的机器可读 JSON 收据
    - 真实交互与溯源：支持聚焦节点、上下游追踪、精确路由高亮；可选源证据模式把节点标记到公开提交代码行，不捏造拓扑
    - 默认可移植易分享：输出单 HTML 文件，可导出 PNG/WebP/JPG 长图、PDF 或分享卡
    - 广泛 Agent 兼容：原生支持 Claude Code / Codex / Cursor / OpenCode，并通过插件扩展至 DSH 等环境
    tags: *id001
    flag: 社区集成，非 DeepSeek 官方产品；实际 DSH 包名 @tt-a1i/archify-dsh
    notes: README 声明该 DSH 集成是 Community integration，无遥测，需 Node ^22.19.0 || >=24.0.0。移除命令：dsh plugin --profile web remove @tt-a1i/archify-dsh。安装命令按官方 README 精确锁定版本：2026-11-23 核查时 wx-xingyun 文章写 1.1.0（绑定 Archify Skill 3.2.0、宿主 0.2.1-rc.2），但 npm latest 与官方集成 README 已升到 1.2.0（绑定 Archify Skill 3.3.0、精确宿主 0.2.2-rc.5），按本站『安装命令以 README 为准』更新为 1.2.0。每个用到 Archify 的 profile 都要单独跑这条精确版本命令；升级宿主或主仓库不会自动更新已装插件。旧版本 1.0.0（2026-10-04，宿主 0.1.2-rc.1）、1.1.0 仍留在各自 release tag 供旧宿主使用。
    repo_confirmed: true
    gh:
      stars: 97754
      forks: 6676
      issues: 369
      language: JavaScript
      license: Apache-2.0
      pushed_at: '2026-11-19T00:44:55Z'
      archived: false
      slug: tt-a1i/archify
      stars_label: 97.8k
      forks_label: '6676'
      pushed_date: '2026-11-19'
      updated_label: 6 天前有提交
      updated_days: 6
      stale: false
    entry_updated: '2026-11-24'
    category_label: 视觉与设计
    status_label: 社区
    weight: 1030
    url: /plugins/archify/
  generated: true
---

把想法、计划或代码库变成交互式图表的 agent skill；针对 DSH 提供社区维护的插件集成（@tt-a1i/archify-dsh），可在 DSH 对话里调用 archify 技能生成架构图、流程图、系统拓扑图。
