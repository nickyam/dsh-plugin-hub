---
title: dsh-ios
description: dsh-ios 是 DeepSeek Harness 的 iOS 模拟器插件，在对话中提供实时模拟器画面与通过 USB 连接的真实 iPhone 画面，并赋予 AI 代理 22 个工具来启动设备、构建运行应用、驱动 UI 与调试检查。
categories:
- remote
tags: &id001
- iOS
- 模拟器
- 调试
weight: 1010
params:
  plugin:
    id: dsh-ios
    name: dsh-ios
    category: remote
    status: community
    repo: https://github.com/ZSeven-W/dsh-ios
    install: 'dsh plugin --profile web add @zseven-w/dsh-ios@latest

      dsh web

      '
    summary: dsh-ios 是 DeepSeek Harness 的 iOS 模拟器插件，在对话中提供实时模拟器画面与通过 USB 连接的真实 iPhone 画面，并赋予 AI 代理 22 个工具来启动设备、构建运行应用、驱动 UI 与调试检查。
    features:
    - 对话内实时模拟器：把 serve-sim MJPEG 流代理到持久右侧栏面板，浏览器不直连模拟器端口
    - USB 真机连接：在真机上构建并启动 WebDriverAgent，经环回隧道转发控制与屏幕端口
    - 22 个 Agent 工具：覆盖设备管理、截屏、交互、构建运行、日志、AXe 无障碍 UI 树、Vision OCR 等
    - 可交互面板：在画面上点击 / 拖拽 / 旋转 / 按 Home，支持缩放与无框 / 真机框样式
    - SwiftUI 预览热重载：包外生成临时宿主应用，将预览编译为 dylib 在运行中的模拟器内热替换（约 2–5 秒）
    tags: *id001
    notes: README 标注适配 DSH Web 0.2.2-rc.1 与 Desktop 0.2.1-rc.5；需宿主端启用移动网关或模拟器 / 真机环境。
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
    url: /plugins/dsh-ios/
  generated: true
---

dsh-ios 是 DeepSeek Harness 的 iOS 模拟器插件，在对话中提供实时模拟器画面与通过 USB 连接的真实 iPhone 画面，并赋予 AI 代理 22 个工具来启动设备、构建运行应用、驱动 UI 与调试检查。
