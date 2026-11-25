---
title: open-design
description: 首个协作式 AI 设计智能体工作区，本地优先、开源：用简要需求驱动 Agent 生成遵循设计系统的原型、演示稿、图表与视频。
categories:
- visual
tags: &id001
- 设计
- 多模态
- 演示文稿
weight: 1030
params:
  plugin:
    id: open-design
    name: open-design
    category: visual
    status: community
    repo: https://github.com/nexu-io/open-design
    install: od agent setup deepseek-harness
    summary: 首个协作式 AI 设计智能体工作区，本地优先、开源：用简要需求驱动 Agent 生成遵循设计系统的原型、演示稿、图表与视频。
    features:
    - 协作式 AI 设计工作区：团队与 Agent 共创，分享作品、交换反馈、迭代
    - agent 原生、模型无关：直接复用 PATH 中已有的 claude / codex / cursor 等作为设计引擎
    - 本地优先 + BYOK（自带密钥），代理含 SSRF 防护
    - 四平面可组合：插件 / 功能技能 / 设计模板 / 设计系统均为可版本化目录
    - 品牌级默认渲染：每次生成读取 DESIGN.md 作为品牌契约，附 151 个设计系统包
    tags: *id001
    notes: 接入 DSH 原生运行时：先装官方 dsh CLI，再运行 `od agent setup deepseek-harness` 安装 / 修复 OD 连接组件；也可用 `od mcp install deepseek-harness` 一键装 MCP。macOS 桌面版因系统 od 命令冲突，建议从 App 内 Settings → MCP server 复制路径。
    repo_confirmed: true
    gh:
      stars: 108341
      forks: 12296
      issues: 1427
      language: TypeScript
      license: Apache-2.0
      pushed_at: '2026-11-19T01:09:09Z'
      archived: false
      slug: nexu-io/open-design
      stars_label: 108.3k
      forks_label: 12.3k
      pushed_date: '2026-11-19'
      updated_label: 6 天前有提交
      updated_days: 6
      stale: false
    entry_updated: '2026-11-06'
    category_label: 视觉与设计
    status_label: 社区
    weight: 1030
    url: /plugins/open-design/
  generated: true
---

首个协作式 AI 设计智能体工作区，本地优先、开源：用简要需求驱动 Agent 生成遵循设计系统的原型、演示稿、图表与视频。
