---
title: DSH Codex UI
description: 一套 Codex 风格的 DSH 界面增强，由六个可独立启停的子插件组成：输入历史召回、全屏双岛设置、物理毛玻璃换肤、模块化侧栏、智能会话标题与桌面窗口菜单；2.0 起全面改用官方插槽与原语，降低宿主升级带来的破坏风险。
categories:
- ui
tags: &id001
- 界面
- 主题
- 侧栏
- Codex
weight: 1030
params:
  plugin:
    id: dsh-codex-ui
    name: DSH Codex UI
    aliases:
    - '@michengai/dsh-codex-ui'
    - Codex 风格界面
    - Codex UI 2.0
    category: ui
    status: community
    repo: https://github.com/MichengAI/dsh-codex-ui
    install: dsh plugin --profile web add @michengai/dsh-codex-ui
    summary: 一套 Codex 风格的 DSH 界面增强，由六个可独立启停的子插件组成：输入历史召回、全屏双岛设置、物理毛玻璃换肤、模块化侧栏、智能会话标题与桌面窗口菜单；2.0 起全面改用官方插槽与原语，降低宿主升级带来的破坏风险。
    features:
    - 输入框增强：行内意图预测与续写（Tab 采纳、Alt+↓/↑ 候选）、终端风格历史（↑/↓ 召回）、自适应宽度手柄
    - 设置皮肤：全屏悬浮双岛工作台、Ambient Ground 漫反射底板、分类导航与原生搜索
    - 主题换肤：内置 14 款主题（含 Codex、Claude、Dracula、Cyberpunk、Solarized、Gruvbox、Catppuccin 系列），平铺 / 云母双排版、三档材质与地面光斑
    - 模块化侧栏：工作区分区、手风琴折叠抽屉、拖拽排序、会话未读标记；折叠态 100% 对齐宿主官方 56px 导轨
    - 智能会话标题：首条消息语义提炼，支持推理模型 4096 tokens 上下文
    - 生态管理：官方与第三方插件集中看护、版本检测与一键批量升级
    tags: *id001
    flag: 社区项目（Apache-2.0，非 DeepSeek 官方）
    notes: 仓库 MichengAI/dsh-codex-ui（main 分支），npm 包 @michengai/dsh-codex-ui，README 版本 v2.0（文章写 2.0.9，npm 仓库实时版本以 registry 为准）。环境要求 Node.js 22+。2.0 彻底重写：放弃 1.x 直接改宿主 DOM、高权重 CSS 覆盖的做法，改用官方 Slots 插槽与 @deepseek-ai/dsh-client-ui-primitives 原语，升级 DSH 更不易崩。文章（wx-top10-30d）称「1.x 暴力覆盖、2.0 推倒重写」，与 README 的技术决策一节一致。
    repo_confirmed: true
    gh:
      stars: 303
      forks: 26
      issues: 0
      language: TypeScript
      license: Apache-2.0
      pushed_at: '2026-11-17T09:59:08Z'
      archived: false
      slug: MichengAI/dsh-codex-ui
      stars_label: '303'
      forks_label: '26'
      pushed_date: '2026-11-17'
    category_label: 界面与体验
    status_label: 社区
    weight: 1030
    url: /plugins/dsh-codex-ui/
  generated: true
---

一套 Codex 风格的 DSH 界面增强，由六个可独立启停的子插件组成：输入历史召回、全屏双岛设置、物理毛玻璃换肤、模块化侧栏、智能会话标题与桌面窗口菜单；2.0 起全面改用官方插槽与原语，降低宿主升级带来的破坏风险。
