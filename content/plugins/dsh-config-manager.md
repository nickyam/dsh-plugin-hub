---
title: dsh-config-manager（配置管理器）
description: DSH配置管理器，管设置、模型与 Provider 配置、已安装插件及插件配置、MCP Servers、Skills、Agent Presets、工作区与 AGENTS.md。装完重启 DSH，设置页会出现「备份与迁移」入口。导出 ZIP 后可上传至 GitHub/网盘做跨机迁移。
categories:
- tool
tags: &id001
- 配置
- 迁移
- 备份
weight: 1000
params:
  plugin:
    id: dsh-config-manager
    name: dsh-config-manager（配置管理器）
    category: tool
    status: community
    repo: npm package
    install: dsh plugin --profile web add dsh-config-manager@latest
    summary: DSH配置管理器，管设置、模型与 Provider 配置、已安装插件及插件配置、MCP Servers、Skills、Agent Presets、工作区与 AGENTS.md。装完重启 DSH，设置页会出现「备份与迁移」入口。导出 ZIP 后可上传至 GitHub/网盘做跨机迁移。
    features:
    - 管设置、模型与 Provider 配置
    - 已安装插件及插件配置
    - MCP Servers、Skills、Agent Presets
    - 工作区与 AGENTS.md
    - ZIP 导出 + 加密备份
    tags: *id001
    flag: npm install -g dsh-config-manager@latest --omit=peer；pnpm minimumReleaseAge 策略；@latest 可能装到旧版；profile 本身不随备份迁移
    repo_confirmed: true
    gh: null
    entry_updated: '2026-11-26'
    category_label: 工具与能力
    status_label: 社区
    weight: 1000
    url: /plugins/dsh-config-manager/
  generated: true
---

DSH配置管理器，管设置、模型与 Provider 配置、已安装插件及插件配置、MCP Servers、Skills、Agent Presets、工作区与 AGENTS.md。装完重启 DSH，设置页会出现「备份与迁移」入口。导出 ZIP 后可上传至 GitHub/网盘做跨机迁移。
