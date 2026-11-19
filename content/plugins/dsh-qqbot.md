---
title: dsh-qqbot（QQ 通道）
description: 腾讯 QQ 开放平台团队（tencent-connect）维护的 QQ 通道插件：在 QQ 私聊与群里直接和 DSH 的 agent 对话，也能在手机给本机 Agent 派活。凭据走扫码绑定，绑过一次不用再扫。
categories:
- integration
tags: &id001
- QQ
- 消息通道
- 手机派活
weight: 1010
params:
  plugin:
    id: dsh-qqbot
    name: dsh-qqbot（QQ 通道）
    aliases:
    - QQ 机器人
    - qqbot
    - 腾讯 QQ
    category: integration
    status: official
    repo: https://github.com/tencent-connect/dsh-qqbot
    install: dsh plugin --profile qqbot add @tencent-connect/dsh-qqbot
    summary: 腾讯 QQ 开放平台团队（tencent-connect）维护的 QQ 通道插件：在 QQ 私聊与群里直接和 DSH 的 agent 对话，也能在手机给本机 Agent 派活。凭据走扫码绑定，绑过一次不用再扫。
    features:
    - 扫码绑定：首次启动检测到没有凭据就进扫码引导，终端出二维码、手机 QQ 扫一下把凭据存进 profile
    - 私聊与群聊：QQ WebSocket 收消息 → ctx.agents → DSH agent loop，回复用 sendMarkdown 发回
    - 独立 profile：官方装法是单开 qqbot profile，不与 web 混在一起
    - 降级通道：没有端内绑定页的纯 CLI 环境可设 QQBOT_BIND_OPEN_BROWSER=1 拉起系统浏览器扫码页
    - 桌面端零命令行：「插件 → 添加插件」填 @tencent-connect/dsh-qqbot@latest，左下角头像 → 设置 → QQ 机器人扫码
    tags: *id001
    flag: 腾讯官方出品，不是 DeepSeek 官方；装到 qqbot profile
    notes: npm 包全名是 @tencent-connect/dsh-qqbot，漏掉作用域装不上。README 建议升到 0.4.0 以上再扫码——更早版本的终端二维码可能渲染错位。手动装要自备 QQBOT_APPID 与 QQBOT_SECRET。别和其他同名的社区 dsh-qqbot（zaofan-make、Oblivious0214、wang-22-code 等都叫这个名字）搞混，认 tencent-connect 这个组织。
    repo_confirmed: true
    gh:
      stars: 611
      forks: 74
      issues: 49
      language: TypeScript
      license: MIT
      pushed_at: '2026-11-17T14:42:44Z'
      archived: false
      slug: tencent-connect/dsh-qqbot
      stars_label: '611'
      forks_label: '74'
      pushed_date: '2026-11-17'
    category_label: 集成与迁移
    status_label: 官方
    weight: 1010
    url: /plugins/dsh-qqbot/
  generated: true
---

腾讯 QQ 开放平台团队（tencent-connect）维护的 QQ 通道插件：在 QQ 私聊与群里直接和 DSH 的 agent 对话，也能在手机给本机 Agent 派活。凭据走扫码绑定，绑过一次不用再扫。
