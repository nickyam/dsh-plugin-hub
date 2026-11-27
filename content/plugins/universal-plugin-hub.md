---
title: Universal Plugin Hub
description: 把 Claude Code 与 Codex 的插件生态接进 DSH：浏览官方 Claude 目录、添加 Claude / Codex 市场或任意 Git 仓库当插件源，再把插件、Skills 与 MCP 服务放在同一个界面里管。
categories:
- market
tags: &id001
- 插件市场
- 跨生态
- MCP
- 技能管理
weight: 1020
params:
  plugin:
    id: universal-plugin-hub
    name: Universal Plugin Hub
    aliases:
    - 统一插件中枢
    - plugin-hub
    - 跨生态插件
    category: market
    status: community
    repo: https://github.com/Ultmebius/universal-plugin-hub
    install: dsh plugin add universal-plugin-hub
    summary: 把 Claude Code 与 Codex 的插件生态接进 DSH：浏览官方 Claude 目录、添加 Claude / Codex 市场或任意 Git 仓库当插件源，再把插件、Skills 与 MCP 服务放在同一个界面里管。
    features:
    - 能力转换：插件的 Skills 同步进 DSH 原生技能目录（输入框 / 菜单可用），Commands 转成 DSH skill，Agents 定义变成可调用的子代理入口，Hooks 走 DSH 的 hooks 桥
    - MCP 统一管理：插件声明的连接器与你自己的 MCP 服务并列，可配地址、鉴权、请求头与环境变量，逐个工具开关
    - 插件源：内置 anthropics/claude-plugins-official 官方目录，可加遵循 Claude / Codex 市场规范的仓库（.claude-plugin/marketplace.json、.agents/plugins/marketplace.json）或含独立插件的 Git 仓库
    - 上传与导入：zip / tgz / tar.gz / 单个 SKILL.md，或本地目录与 Git URL，单次上限 22 MB
    - 本地技能扫描：默认读 ~/.agents/skills，不递归子目录，可逐个启用 / 停用（停用会从 / 菜单消失、文件原样保留）
    - 输入框打 @ 选启用中的插件：这一轮只装载真正要用的技能、子命令与 MCP 工具，而不是全量加载
    - LSP：插件声明的语言服务器在可执行文件存在时注册，缺失会明确报出而不是静默跳过
    tags: *id001
    flag: 装 Claude / Codex 插件前先看清它声明了什么权限
    notes: 支持 DSH Desktop 与 CLI web profile；桌面端在 Settings → Plugins → Add plugin 里填包名或仓库 URL。同一插件同时带 Claude 与 Codex 描述符时以 Claude 为准。数据落在 ~/.dsh/agent-skills/universal-plugin-hub/（installed/ 装好的插件、market/ 源缓存、state.json 源登记），运行时补丁走 profiles/<profile>/cordis.patch.yml；卸载插件时它带进来的技能、MCP、Hooks、LSP 注册会一并移除。星标只有十几个，不能当「用的人多」的证据，但功能边界写得很清楚。
    repo_confirmed: true
    gh:
      stars: 15
      forks: 1
      issues: 0
      language: JavaScript
      license: MIT
      pushed_at: '2026-11-22T06:29:52Z'
      archived: false
      slug: Ultmebius/universal-plugin-hub
      stars_label: '15'
      forks_label: '1'
      pushed_date: '2026-11-22'
      updated_label: 5 天前有提交
      updated_days: 5
      stale: false
    entry_updated: '2026-11-19'
    category_label: 插件市场与发现
    status_label: 社区
    weight: 1020
    url: /plugins/universal-plugin-hub/
  generated: true
lastmod: '2026-11-19'
---

把 Claude Code 与 Codex 的插件生态接进 DSH：浏览官方 Claude 目录、添加 Claude / Codex 市场或任意 Git 仓库当插件源，再把插件、Skills 与 MCP 服务放在同一个界面里管。
