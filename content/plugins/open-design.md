---
title: open-design
description: 首个协作式 AI 设计智能体工作区，本地优先、开源：用简要需求驱动 Agent 生成遵循设计系统的原型、演示稿、图表与视频。
categories:
- visual
tags: &id001
- 设计
- 多模态
- 演示文稿
weight: 1020
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
    refs:
    - id: tree-top10
      title: 10 Best DeepSeek Harness Plugins for AI Developers in 2026
      url: https://api.treerouter.ai/en/blog/best-deepseek-harness-plugins-2026
      kind_label: 第三方媒体
      publisher: TreeRouter Blog（英文，第三方）
    - id: wx-quanjing
      title: DeepSeek Harness 插件全景推荐：14 大类、36 款值得装的插件
      url: https://mp.weixin.qq.com/s/btWqFHCDWwgAD_uj2n0MDw
      kind_label: 公众号
      publisher: 智宇AI说
    source_count: 2
    repo_confirmed: true
    category_label: 视觉与设计
    status_label: 社区
    weight: 1020
    url: /plugins/open-design/
  generated: true
---

首个协作式 AI 设计智能体工作区，本地优先、开源：用简要需求驱动 Agent 生成遵循设计系统的原型、演示稿、图表与视频。
