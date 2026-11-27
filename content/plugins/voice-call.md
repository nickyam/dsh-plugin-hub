---
title: voice-call（语音通话）
description: 在当前会话里直接开口说话：一句说完停顿就自动转成文字发出，Agent 回复按句朗读，播报中开口即可打断；语音识别与合成可分别选 DeepSeek 或豆包，凭据用你自己的。
categories:
- tool
tags: &id001
- 语音
- 通话
- 豆包
- 打断
weight: 1010
params:
  plugin:
    id: voice-call
    name: voice-call（语音通话）
    aliases:
    - voice-call
    - 语音通话
    category: tool
    status: community
    repo: https://github.com/crease123/voice-call
    install: dsh plugin --profile web add voice-call
    summary: 在当前会话里直接开口说话：一句说完停顿就自动转成文字发出，Agent 回复按句朗读，播报中开口即可打断；语音识别与合成可分别选 DeepSeek 或豆包，凭据用你自己的。
    features:
    - 停顿即发送：说完停半秒自动转写并提交，不点发送也不做二次确认；通话前没发出去的草稿在挂断后仍然保留
    - 开口打断：播报中说话会丢掉排队音频、取消正在合成的请求并取消当前回合，这句说完再作为新输入提交
    - 语音服务可混搭：识别 ASR 与合成 TTS 分别选 DeepSeek 或豆包，共四种组合；走 DeepSeek 时直接复用 DSH 已保存的 DEEPSEEK_API_KEY
    - 通话界面：点输入框右下角的电话图标进入，输入框收起换成五段声条与状态行；播放音量只影响当前客户端，不动系统音量
    - 收音可调：打断灵敏度、最短持续说话时间（默认 200 毫秒，调大可滤掉咳嗽与短促杂音）、音色选择与试听
    - 通话提示词：通话期间把「简短、口语化」的要求作为 System Reminder 注入上下文，挂断即撤回，可编辑也可恢复默认
    - 0.3.6 起不再注册独立 Agent 预设，通话直接使用当前会话的模型、工具与审批策略，也不新增第二份 Agent 记忆
    tags: *id001
    flag: 生态里叫 voice-call / dsh-voice-call / dsh-voice 的至少六个项目，本条锁定 npm 包 voice-call 与仓库 crease123/voice-call；npm 上的 dsh-voice-call 是另一个插件（全程本机合成、以接听 / 拒接方式介入），别混
    notes: 官方仓库 crease123/voice-call，npm 包 voice-call（latest 0.3.10，2026-11-19 发布），MIT。要求 DSH 0.2.2-rc.1 及以上的 0.2.x，engines.dsh >=0.2.2-rc.1 <0.3.0-0，所以 0.3.x 宿主装了也用不了；Node >=24.9。浏览器端靠 AudioWorklet，必须在 https 或 localhost 这类安全上下文里跑，换个地方起不来。语音按整句处理——一段话说完才把完整音频（16 kHz 单声道 PCM16，编码成 base64）上传识别，不做逐字实时字幕。打断只能取消请求，已经执行完的外部操作（写文件、发请求、改配置）不会回滚；挂断只关语音连接，Agent 那个回合还在跑，要停得用会话自己的停止。凭据存 DSH 凭据库，插件不含作者额度，语音服务费用由自己的服务商账号承担。写条目时仓库 4 星，属小项目但 README 与教学视频齐全。
    repo_confirmed: true
    gh:
      stars: 4
      forks: 0
      issues: 0
      language: TypeScript
      license: MIT
      pushed_at: '2026-11-19T12:15:38Z'
      archived: false
      slug: crease123/voice-call
      stars_label: '4'
      forks_label: '0'
      pushed_date: '2026-11-19'
      updated_label: 7 天前有提交
      updated_days: 7
      stale: false
    entry_updated: null
    category_label: 工具与能力
    status_label: 社区
    weight: 1010
    url: /plugins/voice-call/
  generated: true
---

在当前会话里直接开口说话：一句说完停顿就自动转成文字发出，Agent 回复按句朗读，播报中开口即可打断；语音识别与合成可分别选 DeepSeek 或豆包，凭据用你自己的。
