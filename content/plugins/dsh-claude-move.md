---
title: dsh-claude-move
description: 把 Claude Code、Codex、OpenCode 和 Hermes 的历史迁进 DeepSeek Harness——会话可续聊、记忆自动带上、技能与命令照常可用；四来源迁移向导加会话导入器，只复制、不移动、不删除源文件，写入前先过审批。
categories:
- integration
tags: &id001
- 迁移
- Claude Code
weight: 1010
params:
  plugin:
    id: dsh-claude-move
    name: dsh-claude-move
    category: integration
    status: community
    repo: https://github.com/PerryLink/dsh-claude-move
    install: dsh plugin --profile web add github:PerryLink/dsh-claude-move
    summary: 把 Claude Code、Codex、OpenCode 和 Hermes 的历史迁进 DeepSeek Harness——会话可续聊、记忆自动带上、技能与命令照常可用；四来源迁移向导加会话导入器，只复制、不移动、不删除源文件，写入前先过审批。
    features:
    - 四来源迁移向导：将 Claude Code / Codex / OpenCode / Hermes 的会话、记忆、技能、指令与斜杠命令复制为可续聊的 DSH 会话
    - 只读源目录、只写 DSH：源文件全程不移动、改写或删除；导入会话保留在 DSH 数据目录
    - 审批门（allowed-once）+ move.json 幂等台账：可重入、可回退，导入可重跑
    - 实时同步运行中的 Claude Code；导入后无需重启 DSH，刷新页面即可继续
    - 可配置 claudeHome、workspaceMode、scanGit、maxSkills、enableWebPanel 等大量选项，兼容 dsh 0.1.6+（web profile，session V3）
    tags: *id001
    flag: 社区项目，非官方（PerryLink 维护，Apache-2.0）
    notes: README 声明：社区插件，与 DeepSeek 官方无关；唯一仓库为 github.com/PerryLink/dsh-claude-move（Gitee 为镜像）。导入仅读取源目录、不改动 Claude 源数据。
    refs:
    - id: baike-dsh
      title: 百度百科：DeepSeek Harness
      url: https://baike.baidu.com/item/deepseek%20harness/68533699
      kind_label: 百科
      publisher: 百度百科
    source_count: 1
    repo_confirmed: true
    category_label: 集成与迁移
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-claude-move/
  generated: true
---

把 Claude Code、Codex、OpenCode 和 Hermes 的历史迁进 DeepSeek Harness——会话可续聊、记忆自动带上、技能与命令照常可用；四来源迁移向导加会话导入器，只复制、不移动、不删除源文件，写入前先过审批。
