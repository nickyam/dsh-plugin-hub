---
title: dsh-plugin-claude-bridge
description: 把 Claude Code 的记忆、技能与全局配置桥接进 DeepSeek Harness——零迁移、完全兼容：直接读取 Claude Code 标准文件位置，无需迁移脚本、文件拷贝或软链接。
categories:
- integration
tags: &id001
- 迁移
- 桥接
- Claude Code
weight: 1010
params:
  plugin:
    id: dsh-plugin-claude-bridge
    name: dsh-plugin-claude-bridge
    category: integration
    status: community
    repo: https://github.com/YYTbit/dsh-plugin-claude-bridge
    install: dsh plugin --profile your-profile add dsh-plugin-claude-bridge
    summary: 把 Claude Code 的记忆、技能与全局配置桥接进 DeepSeek Harness——零迁移、完全兼容：直接读取 Claude Code 标准文件位置，无需迁移脚本、文件拷贝或软链接。
    features:
    - 读取 ~/.claude/projects//memory/*.md，将记忆按优先级（feedback > project > reference > user）排序后注入为动态 system-prompt 上下文，新记忆即时生效
    - 发现 ~/.claude/skills//SKILL.md，将技能名称与描述加入可用技能目录
    - 将 ~/.claude/CLAUDE.md 的全局指令注入 system-prompt（order 5），保留模型路由规则
    - 开箱即用、零配置；可选 claudeHome、maxMemoryBytes、maxSkills、extraSkillDirs 等参数
    tags: *id001
    flag: 社区项目，非官方
    notes: 桥接只读取 Claude Code 文件、不回写；需先在 Claude Code 中生成过 memory/skills/CLAUDE.md 才能生效。仓库 README 注明 MIT 许可。
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
    url: /plugins/dsh-plugin-claude-bridge/
  generated: true
---

把 Claude Code 的记忆、技能与全局配置桥接进 DeepSeek Harness——零迁移、完全兼容：直接读取 Claude Code 标准文件位置，无需迁移脚本、文件拷贝或软链接。
