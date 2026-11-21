---
title: dsh-overall-mcp（全局 MCP 与 Skill）
description: 在 DSH 侧栏挂一块「全局 MCP & Skill」：把散落在 Claude Desktop、Claude Code、Cursor、Codex CLI 里的 MCP 配置一次扫出来登记，再从六个上游目录装新的，最后用调用记录回答那个老问题——明明配了，为什么它没用。
categories:
- integration
tags: &id001
- MCP
- 统一管理
- 调用记录
weight: 1010
params:
  plugin:
    id: dsh-overall-mcp
    name: dsh-overall-mcp（全局 MCP 与 Skill）
    aliases:
    - 全局 MCP
    - overall mcp
    - MCP 面板
    category: integration
    status: community
    repo: https://github.com/YunzhouLi-hub/dsh-overall-mcp
    install: dsh plugin --profile web add github:YunzhouLi-hub/dsh-overall-mcp
    summary: 在 DSH 侧栏挂一块「全局 MCP & Skill」：把散落在 Claude Desktop、Claude Code、Cursor、Codex CLI 里的 MCP 配置一次扫出来登记，再从六个上游目录装新的，最后用调用记录回答那个老问题——明明配了，为什么它没用。
    features:
    - MCP · 已注册：扫宿主机 MCP 配置，看连接状态，启用 / 停用 / 配置 / 检查 / 移除，可按来源筛选与批量操作
    - MCP · 市场：聚合官方 Registry、Smithery、Docker MCP、GitHub MCP、Awesome 远程与 Awesome 清单，去重后搜索、分类、收藏、安装
    - Skill · 已注册：扫 $DSH_HOME/skills、~/.agents/skills、~/.claude/skills、~/.codex/skills，看说明、来源、文件与目录
    - Skill · 市场：ClawHub、Anthropic 官方技能、腾讯 SkillHub 官方、SkillHub、GitHub，带本地索引、分类、来源筛选与热门排序
    - 调用记录：MCP 看工具请求、响应、结果、耗时与连接失败；Skill 看工具装载与斜杠命令引用，时间窗可选 1 小时 / 24 小时 / 7 天
    - 注册条目按 20 / 50 / 100 分页，Skill 还能按使用次数或最近使用排序
    tags: *id001
    flag: 本机扫到的 Skill 不等于当前会话已加载
    notes: 两件事得分清：本机发现的 Skill 只是「存在」，不等于这个会话加载了它；接 MCP 之前要看它的启动命令和权限，因为插件以当前 DSH 进程的权限运行，安装动作会真的去跑 npx / uvx / docker。从 GitHub 装要过 pnpm 的构建白名单，会提示 allowBuilds，按打印出的键名补进 profile 的 pnpm-workspace.yaml 再重试，最好锁 commit。市场页会访问外部服务、受各源配额限制，没配 GitHub token 时预算较低；填进面板的 token 只对 GitHub 主机生效。星标很少，属于「功能写得很全但还没被广泛用」的那类，装前看源码。
    repo_confirmed: true
    gh:
      stars: 25
      forks: 3
      issues: 2
      language: JavaScript
      license: MIT
      pushed_at: '2026-11-16T04:11:56Z'
      archived: false
      slug: YunzhouLi-hub/dsh-overall-mcp
      stars_label: '25'
      forks_label: '3'
      pushed_date: '2026-11-16'
      updated_label: 5 天前有提交
      updated_days: 5
      stale: false
    category_label: 集成与迁移
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-overall-mcp/
  generated: true
---

在 DSH 侧栏挂一块「全局 MCP & Skill」：把散落在 Claude Desktop、Claude Code、Cursor、Codex CLI 里的 MCP 配置一次扫出来登记，再从六个上游目录装新的，最后用调用记录回答那个老问题——明明配了，为什么它没用。
