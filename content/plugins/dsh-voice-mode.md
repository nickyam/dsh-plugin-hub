---
title: dsh-voice-mode（全双工语音）
description: 给 DSH 会话加全双工语音：边说边出字、按句朗读、发声打断，可开关流式识别、字幕与 TTS；识别在宿主端推理（默认免 API Key），朗读默认走 Edge 在线服务、可选本地 VITS/Kokoro 或 OpenAI 兼容远程引擎。
categories:
- tool
tags: &id001
- 语音
- 语音输入
- 朗读
weight: 1010
params:
  plugin:
    id: dsh-voice-mode
    name: dsh-voice-mode（全双工语音）
    aliases:
    - dsh-voice-mode
    - 语音模式
    category: tool
    status: community
    repo: https://github.com/qishuilalala/dsh-voice-mode
    install: dsh plugin --profile web add dsh-voice-mode
    summary: 给 DSH 会话加全双工语音：边说边出字、按句朗读、发声打断，可开关流式识别、字幕与 TTS；识别在宿主端推理（默认免 API Key），朗读默认走 Edge 在线服务、可选本地 VITS/Kokoro 或 OpenAI 兼容远程引擎。
    features:
    - 语音输入：流式识别进草稿，本地识别免 API Key；状态条显示模型加载进度，国内可配 hf-mirror.com 镜像
    - 按句朗读 + 实时字幕：朗读走 Edge 在线服务，可选本地 VITS（WASM）/ Kokoro（原生 addon）或自建 POST /v1/audio/speech 远程引擎（失败自动回退本地）
    - 发声打断：说话即停止当前朗读，once 打断续说，切会话停朗读
    - 自动发送与打断行为可在设置中调整；设置存放位置按 DSH 版本区分（0.1.6 用官方设置存储，0.1.7+ 用插件自有文件）
    - v0.7.39 补丁版跟进到 dsh 0.2.2-rc.5 的锚点、类型与隔离运行时复核（仓库自述，非真实麦克风/全平台验收）
    tags: *id001
    flag: 同类同名项目很多（Hericaneeeeee、wuhe888、bin-r00t 等），本站取 npm 正式包 dsh-voice-mode 对应的 qishuilalala 主仓
    notes: 官方仓库 qishuilalala/dsh-voice-mode，npm 包 dsh-voice-mode，安装后按实际部署方式重启宿主。GitHub 上另有 dsh-voice-mode-custom、dsh-voice-mode-plus、dsh-voice-mode-headless、dsh-voice-mode-desktop 等多个非官方分支或同名实现，包名与 README 特征（流式识别入草稿 + 按句朗读 + 开口打断 + 本地识别免 Key）锁定 qishuilalala 主仓。朗读效果取决于模型、设备、回声消除与网络，README 不承诺全平台可用。文章只强调语音输入省时间，实际插件功能远不止输入。
    repo_confirmed: true
    gh:
      stars: 37
      forks: 12
      issues: 0
      language: JavaScript
      license: NOASSERTION
      pushed_at: '2026-11-26T12:49:35Z'
      archived: false
      slug: qishuilalala/dsh-voice-mode
      stars_label: '37'
      forks_label: '12'
      pushed_date: '2026-11-26'
      updated_label: 今天有提交
      updated_days: 0
      stale: false
    entry_updated: '2026-11-19'
    category_label: 工具与能力
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-voice-mode/
  generated: true
lastmod: '2026-11-19'
---

给 DSH 会话加全双工语音：边说边出字、按句朗读、发声打断，可开关流式识别、字幕与 TTS；识别在宿主端推理（默认免 API Key），朗读默认走 Edge 在线服务、可选本地 VITS/Kokoro 或 OpenAI 兼容远程引擎。
