---
title: dsh-mobile
description: Whaleness（dsh-mobile）是 DeepSeek Harness 的第三方原生移动客户端，Android 与 iOS 通过 Kotlin Multiplatform 共享核心逻辑，经宿主端的 dsh-plugin-mobile-gateway 以 WebSocket 把工作区、会话、实时回复与 Agent 轨迹带到手机。
categories:
- remote
tags: &id001
- iOS
- Android
- WebSocket
- 移动
weight: 1010
params:
  plugin:
    id: dsh-mobile
    name: dsh-mobile
    category: remote
    status: community
    repo: https://github.com/Clarklevis1995/dsh-mobile
    install: dsh plugin --profile web add dsh-plugin-mobile-gateway@latest
    summary: Whaleness（dsh-mobile）是 DeepSeek Harness 的第三方原生移动客户端，Android 与 iOS 通过 Kotlin Multiplatform 共享核心逻辑，经宿主端的 dsh-plugin-mobile-gateway 以 WebSocket 把工作区、会话、实时回复与 Agent 轨迹带到手机。
    features:
    - 实时原生对话：WebSocket 流式推送 Markdown、代码、推理、工具调用与图片附件
    - 语音与文本输入：按住说话转写可编辑草稿，支持斜杠命令与排队消息
    - 多 Host 与工作区：保存并切换多个 Gateway Host 凭据，浏览 / 创建 / 切换工作区与会话
    - 文件卡片与预览：从会话打开文件卡、远程目录浏览、分块校验下载，预览 PDF / 图片 / 代码
    - 插件管理与定时任务：浏览官方与已装插件及其状态，查看、编辑与删除定时任务
    tags: *id001
    notes: 移动端 App 需配合宿主端的 dsh-plugin-mobile-gateway（0.11.2+）使用；iOS 走 TestFlight、Android 走 GitHub Releases APK（独立的第三方客户端，与 DeepSeek 无隶属关系）。
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
    url: /plugins/dsh-mobile/
  generated: true
---

Whaleness（dsh-mobile）是 DeepSeek Harness 的第三方原生移动客户端，Android 与 iOS 通过 Kotlin Multiplatform 共享核心逻辑，经宿主端的 dsh-plugin-mobile-gateway 以 WebSocket 把工作区、会话、实时回复与 Agent 轨迹带到手机。
