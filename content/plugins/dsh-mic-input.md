---
title: dsh-mic-input（麦克风输入）
description: 给 DSH Web 输入框加一个麦克风按钮，点一下开始口述、识别结果实时落进输入框；全部在浏览器里用内置 Web Speech API 完成，无服务端、无 API Key、无需下载模型，音频只发给浏览器自带的语音服务。
categories:
- ui
tags: &id001
- 语音输入
- 麦克风
- Web Speech
- 界面
weight: 1010
params:
  plugin:
    id: dsh-mic-input
    name: dsh-mic-input（麦克风输入）
    aliases:
    - 语音输入
    - 话筒输入
    category: ui
    status: community
    repo: https://github.com/QT-Chen/dsh-mic-input
    install: dsh plugin --profile web add dsh-mic-input
    summary: 给 DSH Web 输入框加一个麦克风按钮，点一下开始口述、识别结果实时落进输入框；全部在浏览器里用内置 Web Speech API 完成，无服务端、无 API Key、无需下载模型，音频只发给浏览器自带的语音服务。
    features:
    - 麦克风按钮：在输入框工具行（发送键旁）加麦克风，点击开始/停止，录音时红色脉冲环
    - 实时转写：边说边出字， interim 结果直接填进输入框
    - 不重复文字：草稿始终基于录音开始时的文本重建，并去除中间结果回显前缀，修复常见重复 bug
    - 纯客户端：Chrome 用 Google 语音服务、Edge 用 Azure 语音服务，无需 Key
    tags: *id001
    flag: 社区项目；语音识别走浏览器自带服务（Edge→Azure / Chrome→Google），音频会发给对应浏览器语音服务；npm 安装免 allowBuilds
    notes: 仓库 QT-Chen/dsh-mic-input（README 标题即 dsh-mic-input，与文章名字精确一致），npm 已发布 dsh-mic-input（registry 200），README 给 git 与 npm 两种方式，本站 install 用 npm 稳定版免构建授权。GitHub 另有 woodess/dsh-voice-input、hjcnx/dsh-web-voice-input 等近似项目，本条取文章点名且名字精确的 QT-Chen 仓库。
    repo_confirmed: true
    gh:
      stars: 3
      forks: 2
      issues: 2
      language: JavaScript
      license: MIT
      pushed_at: '2026-08-16T14:56:34Z'
      archived: false
      slug: QT-Chen/dsh-mic-input
      stars_label: '3'
      forks_label: '2'
      pushed_date: '2026-08-16'
      updated_label: 3 个月前有提交
      updated_days: 99
      stale: false
    entry_updated: '2026-11-17'
    category_label: 界面与体验
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-mic-input/
  generated: true
---

给 DSH Web 输入框加一个麦克风按钮，点一下开始口述、识别结果实时落进输入框；全部在浏览器里用内置 Web Speech API 完成，无服务端、无 API Key、无需下载模型，音频只发给浏览器自带的语音服务。
