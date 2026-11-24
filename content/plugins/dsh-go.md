---
title: DSH Go（Android 客户端）
description: 把 DSH 搬到 Android 手机上的第三方客户端：App 内装好 PRoot 版 Ubuntu + Node.js + DSH 引擎，手机本地就能跑；也能通过 SSH 或 DSHarness Remote 接管电脑、服务器上的 DSH，两种主机在同一个聊天界面里切换。
categories:
- remote
tags: &id001
- Android
- 移动端
- 远程接管
weight: 1010
params:
  plugin:
    id: dsh-go
    name: DSH Go（Android 客户端）
    aliases:
    - dsh-Go
    - 安卓客户端
    - 手机 DSH
    category: remote
    status: community
    repo: https://github.com/ccch1mneyyy/dsh-Go
    install: 从 GitHub Releases 或 go.dshtui.com/download 下载对应架构的 APK 侧载（没有 npm 包，也不是 dsh plugin add）
    summary: 把 DSH 搬到 Android 手机上的第三方客户端：App 内装好 PRoot 版 Ubuntu + Node.js + DSH 引擎，手机本地就能跑；也能通过 SSH 或 DSHarness Remote 接管电脑、服务器上的 DSH，两种主机在同一个聊天界面里切换。
    features:
    - 本机运行：PRoot 兼容启动，免 Root、免 Termux，占约 1 GB；只连远程主机的话不必装本机环境
    - 远程接管：SSH 或 DSHarness Remote 连电脑 / 服务器，聊天页能直接跳到那台机器接着同一个会话
    - 生成中插话：模型回复时排队新消息，可选「立即发送」打断或「插入」进当前轮
    - 插件界面：原生 Flutter 工具卡、表单与面板，仓库带 SDK、教程与示例（sdk/plugin-kit 未发 npm，得先 clone）
    - 手机操控：无障碍 / Shizuku / 自连 ADB 读屏点按输入，敏感动作三级确认，支付、银行、券商类默认拦截
    - 分享与回放：单条回复生成分享卡，整段会话生成端到端加密的回放链接，密钥只在链接里、服务端读不到
    - 外观：Deepy 与鲸娘桌宠、六种主题色、四种图标，横屏与平板切常驻侧栏
    tags: *id001
    flag: 是客户端不是插件，安装走 APK 侧载
    notes: Android 8.0（API 26）以上，发布包只有 arm64-v8a 与 x86_64，没有 32 位 ARM；包名 io.github.ccch1mneyyy.dsh_app，targetSdk 28，以侧载为目标、不是 Google Play 配置。远程通道有明确缺口：只支持图片附件、App 内打不开网页版、插件管理只能开关、不支持 DS Bot 与对话记录导出。手机操控只对正常模式下的本机引擎开放，不打扰模式要 Android 14+ 加 Shizuku 或自连 ADB，熄屏会停任务、闲置 3 分钟自动结束。默认开启匿名使用统计，可在「设置 → 隐私与分享」关。iOS 版还在开发与真机测试，没有公开安装包。项目自己声明与 DeepSeek 无隶属关系，AGPL-3.0。
    repo_confirmed: true
    gh:
      stars: 27263
      forks: 1310
      issues: 738
      language: Dart
      license: AGPL-3.0
      pushed_at: '2026-11-18T09:20:06Z'
      archived: false
      slug: ccch1mneyyy/dsh-Go
      stars_label: 27.3k
      forks_label: '1310'
      pushed_date: '2026-11-18'
      updated_label: 6 天前有提交
      updated_days: 6
      stale: false
    entry_updated: '2026-11-19'
    category_label: 移动端与远程
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-go/
  generated: true
---

把 DSH 搬到 Android 手机上的第三方客户端：App 内装好 PRoot 版 Ubuntu + Node.js + DSH 引擎，手机本地就能跑；也能通过 SSH 或 DSHarness Remote 接管电脑、服务器上的 DSH，两种主机在同一个聊天界面里切换。
