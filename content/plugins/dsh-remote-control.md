---
title: dsh-remote-control（远程接手另一台 DSH）
description: 在当前窗口用原生 DSH 界面操作另一台电脑上的 DSH——不套远程桌面，也不做一个简化面板，对端还是同一套界面、控件和操作方式，审批与 AI 提问由远程端回答。
categories:
- remote
tags: &id001
- 远程
- 双机接力
- 原生界面
weight: 1010
params:
  plugin:
    id: dsh-remote-control
    name: dsh-remote-control（远程接手另一台 DSH）
    aliases:
    - 远程控制
    - 远程接手
    - remote control
    category: remote
    status: community
    repo: https://github.com/stjq12/dsh-remote-control
    install: 两台电脑都装 github:stjq12/dsh-remote-control
    summary: 在当前窗口用原生 DSH 界面操作另一台电脑上的 DSH——不套远程桌面，也不做一个简化面板，对端还是同一套界面、控件和操作方式，审批与 AI 提问由远程端回答。
    features:
    - 原生界面而不是远程桌面：对端仍跑自己的 DSH，只是把当前窗口的流量接到那边
    - 本机页 / 远程页：本机页开放带凭据的 /bridge，远程页填地址与 token 接过去
    - 审批与提问跟着走：有远程控制端时，审批和 ask_user 由远程端回答
    - 下载限定目录：可以只授权某个目录作为下载落点
    - 令牌有时长：5 分钟到 24 小时的有限时长优先，用完关开关；永久选项也会在 DSH 退出时结束
    tags: *id001
    flag: 明文 ws:// 加 token，必须套加密隧道
    notes: README 把安全话说在前头：bridge 用明文 ws:// 加 bearer token，只该跑在 Tailscale、SSH 端口转发、WireGuard 这类加密隧道里；token 等价于被控端 Harness 的完整控制权，别分享别截图，怀疑泄露立刻轮换。限制也写明了：只支持 ws://、没有 WSS/TLS，不支持远程上传文件，字节 RPC 结果 64 MB 上限、普通下载走 256 KB 分块。下载权限只管下载，预览仍可能通过 RPC 读到别的文件，所以只授权最窄的目录。Host 侧代码只在 DSH 启动时加载，换插件必须完全退出再启动。另有一个同名实现 icrefin/dsh-remote-control 走 relay 中转、配对令牌一次性，思路不同，装之前先认清是哪一个。
    repo_confirmed: true
    gh:
      stars: 2
      forks: 0
      issues: 0
      language: JavaScript
      license: MIT
      pushed_at: '2026-11-09T05:09:29Z'
      archived: false
      slug: stjq12/dsh-remote-control
      stars_label: '2'
      forks_label: '0'
      pushed_date: '2026-11-09'
      updated_label: 11 天前有提交
      updated_days: 11
      stale: false
    category_label: 移动端与远程
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-remote-control/
  generated: true
---

在当前窗口用原生 DSH 界面操作另一台电脑上的 DSH——不套远程桌面，也不做一个简化面板，对端还是同一套界面、控件和操作方式，审批与 AI 提问由远程端回答。
