---
title: dsh-im（9 渠道 IM 专线）
description: 通过扫码或机器人凭据把主流 IM 接进 DSH：微信、飞书、钉钉、企业微信、QQ、Slack、Telegram、Discord、WhatsApp、iMessage 等一个插件全收，手机发句话就能驱动电脑上的 agent。
categories:
- integration
tags: &id001
- IM
- 微信
- 飞书
- 远程接入
weight: 1020
params:
  plugin:
    id: dsh-im
    name: dsh-im（9 渠道 IM 专线）
    aliases:
    - '@xmanrui/dsh-im'
    - IM 机器人
    - 信息专线
    category: integration
    status: community
    repo: https://github.com/xmanrui/dsh-im
    install: dsh plugin --profile web add -w @xmanrui/dsh-im
    summary: 通过扫码或机器人凭据把主流 IM 接进 DSH：微信、飞书、钉钉、企业微信、QQ、Slack、Telegram、Discord、WhatsApp、iMessage 等一个插件全收，手机发句话就能驱动电脑上的 agent。
    features:
    - 多渠道接入：微信、飞书、钉钉、企微、QQ、Slack、Telegram、Discord、WhatsApp、iMessage，扫码或机器人凭据二选一
    - 本机凭据：Secret / Token 只提交给本机 Harness Host 并写入受保护凭据存储，状态接口和机器人列表不回传
    - 配置即引导：安装后在「设置 → IM机器人」按各渠道内置引导完成扫码或凭据配置
    - npm 稳定版优先：推荐 @xmanrui/dsh-im，也可用 GitHub 源安装器试用未发布代码（pnpm 10+ 可能需允许构建脚本）
    tags: *id001
    flag: 社区项目；接入机器人涉及各平台凭据，注意 Token 安全与平台条款
    notes: 仓库 xmanrui/dsh-im，npm 包名是 scoped 的 @xmanrui/dsh-im——README 明确「安装请认准完整包名」，GitHub 上另有 MichengAI/dsh-im-connect、SoledadAki/dsh-im-qq-wechat 等近似项目，本站取名字精确、功能覆盖最广的 xmanrui 主仓。文章说的「二维码接 9 个渠道」与 README 渠道列表一致（实际列了 10 个）。安装带 -w 参数（写 profile），Web 与 Desktop 命令分别为 --profile web / --profile desktop，装完重启。
    repo_confirmed: true
    gh:
      stars: 3700
      forks: 391
      issues: 162
      language: JavaScript
      license: MIT
      pushed_at: '2026-11-07T05:03:35Z'
      archived: false
      slug: xmanrui/dsh-im
      stars_label: '3700'
      forks_label: '391'
      pushed_date: '2026-11-07'
      updated_label: 14 天前有提交
      updated_days: 14
      stale: false
    entry_updated: '2026-11-17'
    category_label: 集成与迁移
    status_label: 社区
    weight: 1020
    url: /plugins/dsh-im/
  generated: true
---

通过扫码或机器人凭据把主流 IM 接进 DSH：微信、飞书、钉钉、企业微信、QQ、Slack、Telegram、Discord、WhatsApp、iMessage 等一个插件全收，手机发句话就能驱动电脑上的 agent。
