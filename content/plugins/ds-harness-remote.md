---
title: ds-harness-remote
description: ds-harness-remote 是基于 DeepSeek Harness 插件机制的远程访问方案，通过低延迟、端到端加密的 P2P / 中继网络，让你用手机、电脑或浏览器随时连回本地 DSH 工作区，无需公网端口。
categories:
- remote
tags: &id001
- 远程
- P2P
- 端到端加密
weight: 1010
params:
  plugin:
    id: ds-harness-remote
    name: ds-harness-remote
    category: remote
    status: community
    repo: https://github.com/liguobao/ds-harness-remote
    install: dsh plugin --profile desktop add -w ds-harness-remote@0.6.3
    summary: ds-harness-remote 是基于 DeepSeek Harness 插件机制的远程访问方案，通过低延迟、端到端加密的 P2P / 中继网络，让你用手机、电脑或浏览器随时连回本地 DSH 工作区，无需公网端口。
    features:
    - 多端远程访问：Web、PC、移动端访问本地 Harness 实例，DSH 优先并兼容 Codex / Cursor / Antigravity 等
    - 端到端加密通道：Host 不监听公网端口，经双向加密通道从任意有网处连接，必要时回退 TURN / Server 中继
    - 原生侧栏能力：远程浏览工作区文件、只读预览、远程终端与授权本地服务预览
    - 多客户端并发：多个客户端可同时连同一 Host，RPC 与流按连接隔离
    - 丰富客户端：DSH Desktop 插件、Web、Android APK、iOS TestFlight、Linux 云服务器与 DSH Go
    tags: *id001
    flag: 加密与中继方式以仓库说明为准
    notes: README 标注当前基线 dsh-v0.2.2-rc.1，Host 端无需公网 IP 或端口转发；Linux 一键安装需登录官网获取授权码。
    refs:
    - id: wx-quanjing
      title: DeepSeek Harness 插件全景推荐：14 大类、36 款值得装的插件
      url: https://mp.weixin.qq.com/s/btWqFHCDWwgAD_uj2n0MDw
      kind_label: 公众号
      publisher: 智宇AI说
    source_count: 1
    repo_confirmed: true
    category_label: 移动端与远程
    status_label: 社区
    weight: 1010
    url: /plugins/ds-harness-remote/
  generated: true
---

ds-harness-remote 是基于 DeepSeek Harness 插件机制的远程访问方案，通过低延迟、端到端加密的 P2P / 中继网络，让你用手机、电脑或浏览器随时连回本地 DSH 工作区，无需公网端口。
