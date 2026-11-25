---
title: dsh-windows-mcp（Windows 桌面自动化）
description: 把 CursorTouch/Windows-MCP 挂到 DSH 自带的 MCP 客户端桥上，让 agent 能截屏、读界面元素、点按输入、读写剪贴板与注册表——那些只有图形界面、没有命令行入口的老软件，也能被它操作。
categories:
- tool
tags: &id001
- Windows
- 桌面自动化
- MCP
weight: 1010
params:
  plugin:
    id: dsh-windows-mcp
    name: dsh-windows-mcp（Windows 桌面自动化）
    aliases:
    - windows-mcp
    - 电脑操作
    - 桌面自动化
    category: tool
    status: community
    repo: https://github.com/helloHub1212/dsh-windows-mcp
    install: dsh plugin --profile add github:helloHub1212/dsh-windows-mcp
    summary: 把 CursorTouch/Windows-MCP 挂到 DSH 自带的 MCP 客户端桥上，让 agent 能截屏、读界面元素、点按输入、读写剪贴板与注册表——那些只有图形界面、没有命令行入口的老软件，也能被它操作。
    features:
    - 18 个桌面工具：屏幕截图、UI 树快照、鼠标键盘输入、剪贴板、进程与注册表，注册成 mcp__windows__* 供模型调用
    - 挂官方桥，不重写协议：插件本身只是一个 carrier bundle（只有补丁、没有自己的服务），能力全来自宿主自带的 @deepseek-ai/dsh-mcp-client
    - Computer Use 默认关闭：出厂是禁用状态，要自己到插件面板里打开，避免装完就给它操作屏幕的权限
    - 依赖在应用内装：设置 → 桌面控制的 Dependency 卡片会显示 installed / 未安装 / 找不到 uv 三种状态，点一下装 Windows-MCP，桥接行写进 cordis.patch.yml（写前带时间戳备份、放在幂等标记里）
    - 版本可控：同页能查上游版本、一键升级与回滚，每个版本装在自己的工具根目录，切换只改桥接行、不用重装
    - 诊断工具：windows_mcp_doctor 走一遍环境与桥接检查
    tags: *id001
    flag: 只支持 Windows 10/11，且要 DSH Desktop 0.2.0-rc.2+
    notes: 三个硬前提：Windows 10/11、带内置 @deepseek-ai/dsh-mcp-client 桥的 DSH Desktop 0.2.0-rc.2 或更新、PATH 里能找到 uv（找不到时它还会去 %USERPROFILE%\.local\bin 捞一次；仅装依赖用得上，DSH 本身启动不依赖）。想让 agent 真的「看见」截图，得用支持图片输入的模型。Electron 版独占 desktop 配置，命令行会对它拒绝所有命令（包括只读的），桌面端只能从图形界面装。作者在 Windows 11 + DSH Desktop 0.2.0-rc.2 上验过：桥接对外公布 18 个工具（上游 21 个减去排除的 3 个），启动约 1.5 秒就绪。
    repo_confirmed: true
    gh:
      stars: 1736
      forks: 8
      issues: 0
      language: JavaScript
      license: MIT
      pushed_at: '2026-11-15T12:12:09Z'
      archived: false
      slug: helloHub1212/dsh-windows-mcp
      stars_label: '1736'
      forks_label: '8'
      pushed_date: '2026-11-15'
      updated_label: 10 天前有提交
      updated_days: 10
      stale: false
    entry_updated: '2026-11-19'
    category_label: 工具与能力
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-windows-mcp/
  generated: true
---

把 CursorTouch/Windows-MCP 挂到 DSH 自带的 MCP 客户端桥上，让 agent 能截屏、读界面元素、点按输入、读写剪贴板与注册表——那些只有图形界面、没有命令行入口的老软件，也能被它操作。
