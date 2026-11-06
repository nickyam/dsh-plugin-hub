---
title: deepseek-harness-desktop（Tauri）
description: 基于 Tauri 2 的轻量桌面版，在桌面上运行 DeepSeek Harness，无需手动安装 Node.js / pnpm / Docker，零环境配置，预置插件。
categories:
- ui
tags: &id001
- 桌面端
- 轻量
- Tauri
weight: 1010
params:
  plugin:
    id: dsh-desktop-tauri
    name: deepseek-harness-desktop（Tauri）
    category: ui
    status: community
    repo: https://github.com/dsh-tauri/deepseek-harness-desktop
    install: brew install dsh-tauri/desktop/deepseek-harness
    summary: 基于 Tauri 2 的轻量桌面版，在桌面上运行 DeepSeek Harness，无需手动安装 Node.js / pnpm / Docker，零环境配置，预置插件。
    features:
    - 原生桌面：Tauri 2 + React 19 + Hero 3，内嵌本地 Harness 界面
    - 远程连接：移动端扫码连接电脑上的 DSH，支持局域网与 Cloudflare 公网隧道
    - 运行时管理：安装依赖、选择内核版本，提供桌面端与内核更新入口
    - 插件管理：12 个内置插件，支持本地路径安装、社区插件安装、升级、卸载与错误查看
    - 个性化：8 种配色、界面缩放、终端模式与可调不透明度 / 磨砂模糊
    tags: *id001
    notes: License 为 MIT 附加非商用条款；本地运行不等于完全离线（模型服务、插件安装、更新与桌宠预设素材仍可能联网）。
    refs:
    - id: wx-quanjing
      title: DeepSeek Harness 插件全景推荐：14 大类、36 款值得装的插件
      url: https://mp.weixin.qq.com/s/btWqFHCDWwgAD_uj2n0MDw
      kind_label: 公众号
      publisher: 智宇AI说
    source_count: 1
    repo_confirmed: true
    category_label: 界面与体验
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-desktop-tauri/
  generated: true
---

基于 Tauri 2 的轻量桌面版，在桌面上运行 DeepSeek Harness，无需手动安装 Node.js / pnpm / Docker，零环境配置，预置插件。
