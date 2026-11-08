---
title: dsh-vision-toolkit
description: DSH 原生视觉工具包：为纯文本模型赋予图像问答、长截图 OCR、UI 还原与 GUI 视觉任务能力，把视觉工具与 Skill 无缝嵌入 Profile、会话、设置、Artifacts 与 Web UI。
categories:
- visual
tags: &id001
- 多图
- UI还原
- 批量处理
- 视觉
weight: 1010
params:
  plugin:
    id: dsh-vision-toolkit
    name: dsh-vision-toolkit
    category: visual
    status: community
    repo: https://github.com/Anionex/dsh-vision-toolkit
    install: dsh plugin --profile web add @anionex/dsh-vision-toolkit
    summary: DSH 原生视觉工具包：为纯文本模型赋予图像问答、长截图 OCR、UI 还原与 GUI 视觉任务能力，把视觉工具与 Skill 无缝嵌入 Profile、会话、设置、Artifacts 与 Web UI。
    features:
    - 粘贴图片直接问：粘贴后纯文本模型自动切到 (Vision Toolkit) 变体，保留原生缩略图与会话历史
    - 一条命令安装：安装后于 Settings → Vision Toolkit 配置视觉提供商即可启用
    - 提取任务关键内容：围绕当前任务提取证据（错误在哪、按钮在哪），而非笼统描述，省 token 且更准
    - 实战检验的方法论：捆绑 vision-skills，带入上游 playbooks 指导 Agent 看什么、选什么工具、如何验证
    - 10 种可组合视觉工具：vision_glance、vision_ground、vision_detect、vision_crop、vision_trace、vision_long_screenshot_ocr 等，坐标统一用原始像素格式
    tags: *id001
    flag: 视觉能力打包自上游 agent-vision-toolkit
    notes: README 注明其视觉能力来自打包固定的上游项目 agent-vision-toolkit，本仓库负责 DSH 原生集成。另提供 headless / desktop profile 的同形安装命令。
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
    url: /plugins/dsh-vision-toolkit/
  generated: true
---

DSH 原生视觉工具包：为纯文本模型赋予图像问答、长截图 OCR、UI 还原与 GUI 视觉任务能力，把视觉工具与 Skill 无缝嵌入 Profile、会话、设置、Artifacts 与 Web UI。
