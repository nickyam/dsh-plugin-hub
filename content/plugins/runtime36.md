---
title: runtime36
description: 把 Obsidian / Markdown 笔记库作为 Agent 的持久知识库：每日封存与蒸馏，用简短名词精准定位经验页面，让 Agent 跨会话记住已做的决策与沉淀的方法。
categories:
- memory
tags: &id001
- 记忆
- Obsidian
- 知识库
weight: 1010
params:
  plugin:
    id: runtime36
    name: runtime36
    category: memory
    status: community
    repo: https://github.com/398894496-arch/runtime36
    install: dsh plugin --profile web add github:398894496-arch/runtime36
    summary: 把 Obsidian / Markdown 笔记库作为 Agent 的持久知识库：每日封存与蒸馏，用简短名词精准定位经验页面，让 Agent 跨会话记住已做的决策与沉淀的方法。
    features:
    - 每日封存与蒸馏：自动按日记录工作，再把日志蒸馏成可复用的方法，绝不自动覆盖原始日志
    - 两步晋升：五天关卡通过后当天写入暂定方法，下次类似任务询问采纳，采纳后才转活跃
    - 锁定式检索：简短名词直接映射到目标页面（双 SHA-256），无向量库、无邻居引用
    - 分层协议：L1 日志 / L2 蒸馏 / L3 晋升 / L4 锁定，支持 Cursor、Codex、Claude Code 与 DSH
    - 三层验证：实现、对比（lock vs neighbor）、作者自报严格分离
    tags: *id001
    notes: 上游仓库现已将项目重命名为 KRouter，README 主推通过 bootstrap 脚本安装（而非 dsh plugin add），并强调面向 Claude Code / Codex / Cursor 的 MCP 记忆；核心仍是把 Obsidian/Markdown 笔记库作为 Agent 持久记忆。安装前请先读仓库 README 确认当前 DSH 安装方式。
    refs:
    - id: tree-top10
      title: 10 Best DeepSeek Harness Plugins for AI Developers in 2026
      url: https://api.treerouter.ai/en/blog/best-deepseek-harness-plugins-2026
      kind_label: 第三方媒体
      publisher: TreeRouter Blog（英文，第三方）
    source_count: 1
    repo_confirmed: true
    category_label: 记忆与知识
    status_label: 社区
    weight: 1010
    url: /plugins/runtime36/
  generated: true
---

把 Obsidian / Markdown 笔记库作为 Agent 的持久知识库：每日封存与蒸馏，用简短名词精准定位经验页面，让 Agent 跨会话记住已做的决策与沉淀的方法。
