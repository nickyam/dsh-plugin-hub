---
title: dsh-wallpaper-engine（壁纸引擎）
description: 把本机 Wallpaper Engine 的 Scene、Web 与视频壁纸搬进 DSH 对话界面，再配液态玻璃、字体、吉祥物与可分享的外观预设；纯外观插件，不向 agent 注册工具、不注入提示词、不增加 token 开销。
categories:
- ui
tags: &id001
- 壁纸
- 皮肤
- 界面
- 外观
weight: 1010
params:
  plugin:
    id: dsh-wallpaper-engine
    name: dsh-wallpaper-engine（壁纸引擎）
    aliases:
    - dsh-plugin-wallpaper-engine
    - 壁纸引擎
    - DSH Wallpaper Engine
    category: ui
    status: community
    repo: https://github.com/elysia395/dsh-wallpaper-engine
    install: dsh plugin --profile web add dsh-plugin-wallpaper-engine
    summary: 把本机 Wallpaper Engine 的 Scene、Web 与视频壁纸搬进 DSH 对话界面，再配液态玻璃、字体、吉祥物与可分享的外观预设；纯外观插件，不向 agent 注册工具、不注入提示词、不增加 token 开销。
    features:
    - 壁纸进界面：支持 Wallpaper Engine 的 Scene / Web / 视频壁纸，场景壁纸由内置 MIT 引擎 WebWallGL 实时 WebGL 渲染（粒子/着色器等）
    - 外观预设：液态玻璃、字体、吉祥物与可分享的皮肤预设，风格资产与功能插件解耦
    - 零 token 开销：不注册工具、不注入提示文本，只改界面观感
    tags: *id001
    flag: 社区项目；纯外观，不影响模型能力；视频/场景壁纸可能占用一定渲染资源
    notes: 仓库 elysia395/dsh-wallpaper-engine，npm 包名是 dsh-plugin-wallpaper-engine（比仓库名多 plugin- 前缀，别填错）。GitHub 上有多个二次开发分支，本条取 README 完整、标注为正式主仓且 ★ 数最高的 elysia395 仓库。
    repo_confirmed: true
    gh:
      stars: 7450
      forks: 121
      issues: 20
      language: JavaScript
      license: MIT
      pushed_at: '2026-11-18T11:42:00Z'
      archived: false
      slug: elysia395/dsh-wallpaper-engine
      stars_label: '7450'
      forks_label: '121'
      pushed_date: '2026-11-18'
      updated_label: 2 天前有提交
      updated_days: 2
      stale: false
    entry_updated: '2026-11-17'
    category_label: 界面与体验
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-wallpaper-engine/
  generated: true
---

把本机 Wallpaper Engine 的 Scene、Web 与视频壁纸搬进 DSH 对话界面，再配液态玻璃、字体、吉祥物与可分享的外观预设；纯外观插件，不向 agent 注册工具、不注入提示词、不增加 token 开销。
