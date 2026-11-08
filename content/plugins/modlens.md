---
title: modlens
description: DSH 上能力最强的视觉插件（作者自称）：给 DeepSeek、GLM 等纯文本模型外挂视觉能力，粘贴图片即得结构化 JSON 证据（OCR、版面、语义），无需先存文件再传路径。
categories:
- visual
tags: &id001
- OCR
- 视觉
- 结构化输出
weight: 1010
params:
  plugin:
    id: modlens
    name: modlens
    category: visual
    status: community
    repo: https://github.com/liustack/modlens
    install: npx -y @deepseek-ai/dsh plugin --profile web add @liustack/modlens@3.27.2
    summary: DSH 上能力最强的视觉插件（作者自称）：给 DeepSeek、GLM 等纯文本模型外挂视觉能力，粘贴图片即得结构化 JSON 证据（OCR、版面、语义），无需先存文件再传路径。
    features:
    - 粘贴即识别：在纯文本模型上粘贴图片自动转临时文件或 (modlens vision) 变体，自动覆盖可识别的路由
    - 最轻侵入：不改任何 harness 配置、无本地代理守护进程，卸载即删文件夹恢复原状
    - 零配置启动：复用 Claude Code / Codex / OpenCode / Pi 等既有设置，免费通道可用 Antigravity CLI 或 Gemini Key
    - 多 Key 轮转：逗号分隔的 Key 在鉴权 / 限流 / 配额失败时轮转，其他失败跳过剩余 Key 保留既有故障转移
    - 证据而非臆测：输出完整转录、阅读顺序版面区域、实体与关系列表，模型可引用具体细节
    tags: *id001
    flag: 与 dsh-vision-toolkit 是不同条目，本站不合并
    notes: README 注明 Web UI 里直接粘贴图片可能被宿主拒绝（DeepSeek 适配器硬编码 inputModalities 为 text），read_image 在 Web UI 已验证端到端可用。仓库另含兄弟插件 ModSearch（免费网页搜索）。
    refs:
    - id: wx-quanjing
      title: DeepSeek Harness 插件全景推荐：14 大类、36 款值得装的插件
      url: https://mp.weixin.qq.com/s/btWqFHCDWwgAD_uj2n0MDw
      kind_label: 公众号
      publisher: 智宇AI说
    source_count: 1
    repo_confirmed: true
    category_label: 视觉与设计
    status_label: 社区
    weight: 1010
    url: /plugins/modlens/
  generated: true
---

DSH 上能力最强的视觉插件（作者自称）：给 DeepSeek、GLM 等纯文本模型外挂视觉能力，粘贴图片即得结构化 JSON 证据（OCR、版面、语义），无需先存文件再传路径。
