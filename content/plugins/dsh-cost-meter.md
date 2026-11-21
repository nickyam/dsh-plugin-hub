---
title: dsh-cost-meter（费用统计）
description: DSH 的统一成本账本：按会话、模型、调用与轮次追踪费用和 Token，集中查看账户余额、订阅额度与预算，并把 API 按量费用与 Plan 折算分开统计，支持多厂商价目表与峰谷提醒。
categories:
- billing
tags: &id001
- 成本
- 用量
- 多厂商
- 预算
weight: 1030
params:
  plugin:
    id: dsh-cost-meter
    name: dsh-cost-meter（费用统计）
    aliases:
    - 费用统计
    - Cost Meter
    category: billing
    status: community
    repo: https://github.com/Han-1413141/dsh-cost-meter
    install: dsh plugin --profile web add dsh-cost-meter
    summary: DSH 的统一成本账本：按会话、模型、调用与轮次追踪费用和 Token，集中查看账户余额、订阅额度与预算，并把 API 按量费用与 Plan 折算分开统计，支持多厂商价目表与峰谷提醒。
    features:
    - 会话与调用成本：输入框、顶栏与每轮显示费用，可查费率、Token、记录的输入与工具结果，含主 / 子 Agent 成本归属
    - 统计与导出：按日期、Provider、模型筛选，查看趋势、排行、缓存命中率与 Token 热力图，导出会话并单独看本地模型的 API 等价成本
    - 额度与余额：Codex / ChatGPT、OpenCode Go、MiniMax、Claude、GLM、Kimi、千问、MiMo、OpenDesign 等 Plan，CLIProxyAPI 多账户额度与自定义 HTTP 余额源
    - 多厂商价目表：自动匹配模型、可编辑费率与倍率、峰谷分档，同步 DeepSeek 官价与 OpenRouter 目录，API 费用与 Plan 折算分开
    - 预算与告警：日 / 月 / 累计 / 自定义日期预算，峰谷时段与倒计时，切换前弹窗与系统通知
    - 显示与历史：可配侧栏卡片、输入框条目、额度条与轮次费用，中英界面与深色 / 移动布局，历史导入与保留期控制
    tags: *id001
    flag: 社区项目（MIT，非 DeepSeek 官方）
    notes: 仓库 Han-1413141/dsh-cost-meter（master 分支），npm 包 dsh-cost-meter，README 版本 1.9.70（文章写 1.9.47，以仓库为准）。环境要求 Node.js >= 20、DSH 0.2.0+ 且宿主可用 pnpm；装完需重启 dsh web。桌面端用其内置 CLI 与 desktop profile。文章（wx-top10-30d）称其「内置 170+ 模型价目表、可查十二家 Coding Plan 额度」，README 印证支持多厂商 Plan 与自定义余额源，具体家数以仓库为准。
    repo_confirmed: true
    gh:
      stars: 721
      forks: 63
      issues: 7
      language: JavaScript
      license: MIT
      pushed_at: '2026-11-18T16:25:30Z'
      archived: false
      slug: Han-1413141/dsh-cost-meter
      stars_label: '721'
      forks_label: '63'
      pushed_date: '2026-11-18'
      updated_label: 2 天前有提交
      updated_days: 2
      stale: false
    entry_updated: '2026-11-17'
    category_label: 模型与计费
    status_label: 社区
    weight: 1030
    url: /plugins/dsh-cost-meter/
  generated: true
---

DSH 的统一成本账本：按会话、模型、调用与轮次追踪费用和 Token，集中查看账户余额、订阅额度与预算，并把 API 按量费用与 Plan 折算分开统计，支持多厂商价目表与峰谷提醒。
