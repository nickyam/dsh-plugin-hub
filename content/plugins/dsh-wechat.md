---
title: dsh-wechat
description: 把微信联系人接到 DeepSeek Harness 会话的桥接插件：每个微信发送者对应一个独立的 DSH 会话（wechat-），各自保留上下文；扫码绑定一次后，在微信里发消息即可驱动 Agent，电脑息屏时也能值守。
categories:
- integration
tags: &id001
- 微信
- 远程
- 桥接
weight: 1010
params:
  plugin:
    id: dsh-wechat
    name: dsh-wechat
    aliases:
    - 微信桥接
    category: integration
    status: community
    repo: https://github.com/dAI-aigc/dsh-wechat
    install: dsh plugin --profile web add github:dAI-aigc/dsh-wechat
    summary: 把微信联系人接到 DeepSeek Harness 会话的桥接插件：每个微信发送者对应一个独立的 DSH 会话（wechat-），各自保留上下文；扫码绑定一次后，在微信里发消息即可驱动 Agent，电脑息屏时也能值守。
    features:
    - 一个联系人一个会话：每个微信发送者对应独立的 DSH 会话（wechat-），互不串上下文
    - 白名单：只服务允许的发送者；不配置 allowFrom 时仅扫码登录的微信号本人可用
    - 入站支持文本、图片、文件；语音 / 视频 / 转发卡片跳过并留日志
    - 原生「正在输入」指示：一轮运行期间向微信发送 typing 指示（每 15 秒续发）
    - 桥接会话自动挂到 cwd 对应工作区，直接出现在 Web 端侧栏分组下
    tags: *id001
    notes: 走腾讯 iLink 机器人通道（ilinkai.weixin.qq.com），协议层基于 @tencent-weixin/openclaw-weixin（MIT）并改写为 DSH 原生。社区另有多个微信桥接实现（panqing0313/dsh-plugin-weixin、gnulife/dsh-plugin-wechat、zgat/dsh-wechat 等），本条目以 dAI-aigc/dsh-wechat 为准。装好后需重启 dsh web 生效。
    refs:
    - id: wx-dabaihua
      title: DeepSeek Harness 是个啥？大白话讲透 + 10 分钟上手 + 好用插件清单
      url: http://mp.weixin.qq.com/s?__biz=MzkwMDMzMzE0Mg==&mid=2247488511&idx=1&sn=b8f08d42ca17c2895080d4180cd3d6c9
      kind_label: 公众号
      publisher: 微信公众号（原文署名待补）
    source_count: 1
    repo_confirmed: true
    category_label: 集成与迁移
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-wechat/
  generated: true
---

把微信联系人接到 DeepSeek Harness 会话的桥接插件：每个微信发送者对应一个独立的 DSH 会话（wechat-），各自保留上下文；扫码绑定一次后，在微信里发消息即可驱动 Agent，电脑息屏时也能值守。
