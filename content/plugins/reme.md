---
title: ReMe
description: ReMe 是本地优先、自我演化的个人知识库（记忆管理工具包），把对话与资源转成可读、可编辑、可检索、互联的 Markdown 记忆，供 DeepSeek Harness 等 Agent 共享同一工作区进行检索、维护与演化。
categories:
- memory
tags: &id001
- 记忆
- 开发工具包
- Markdown
- DSH
weight: 1010
params:
  plugin:
    id: reme
    name: ReMe
    category: memory
    status: community
    repo: https://github.com/agentscope-ai/ReMe
    install: dsh plugin --profile web add @agentscope-ai/reme-dsh-plugin
    summary: ReMe 是本地优先、自我演化的个人知识库（记忆管理工具包），把对话与资源转成可读、可编辑、可检索、互联的 Markdown 记忆，供 DeepSeek Harness 等 Agent 共享同一工作区进行检索、维护与演化。
    features:
    - 记忆即文件：以带 frontmatter 与 wikilink 的普通 Markdown 存持久记忆，用户与 Agent 可读写、同步、备份
    - 自我演化知识库：对话与资源逐步沉淀为日记得体与长期知识，保留来源并随时间长精炼
    - 精准上下文感知召回：BM25 + 可选向量 + wikilink 扩展，按行级段落与关系检索，无需载入整个知识库
    - 跨 Agent 共享工作区：个人助手、编码 Agent 等可通过原生集成、SKILL.md、CLI、HTTP、MCP 或 Python API 共享
    - 主动能力（Proactive）：安全读取兴趣主题并融入宿主 Agent 决策流（如 Auto Dream）
    tags: *id001
    notes: DSH 插件包为 @agentscope-ai/reme-dsh-plugin；核心记忆服务通过 `pip install reme-ai` 安装后 `reme start` 启动（默认 127.0.0.1:2333）。
    repo_confirmed: true
    gh:
      stars: 3820
      forks: 355
      issues: 54
      language: Python
      license: Apache-2.0
      pushed_at: '2026-11-18T17:46:48Z'
      archived: false
      slug: agentscope-ai/ReMe
      stars_label: '3820'
      forks_label: '355'
      pushed_date: '2026-11-18'
      updated_label: 6 天前有提交
      updated_days: 6
      stale: false
    entry_updated: '2026-11-06'
    category_label: 记忆与知识
    status_label: 社区
    weight: 1010
    url: /plugins/reme/
  generated: true
---

ReMe 是本地优先、自我演化的个人知识库（记忆管理工具包），把对话与资源转成可读、可编辑、可检索、互联的 Markdown 记忆，供 DeepSeek Harness 等 Agent 共享同一工作区进行检索、维护与演化。
