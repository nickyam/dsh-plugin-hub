---
title: dsh-image-gen（对话生图）
description: 让 Agent 本身学会画图的原生图像创作插件：一句话批量生成整组图，看得懂画布上的涂鸦与圈选，自动从 500+ 灵感库套用风格模板，另有 Studio 工作台、多模型横向对比与图库；已有 ChatGPT / Grok / Google 订阅可免额外 API Key 生图。
categories:
- visual
tags: &id001
- 生图
- 画布
- 多模型
- BYOK
weight: 1010
params:
  plugin:
    id: dsh-image-gen
    name: dsh-image-gen（对话生图）
    aliases:
    - 生图插件
    - 图像创作
    category: visual
    status: community
    repo: https://github.com/shanliuling/dsh-image-gen
    install: dsh plugin --profile web add dsh-image-gen@latest
    summary: 让 Agent 本身学会画图的原生图像创作插件：一句话批量生成整组图，看得懂画布上的涂鸦与圈选，自动从 500+ 灵感库套用风格模板，另有 Studio 工作台、多模型横向对比与图库；已有 ChatGPT / Grok / Google 订阅可免额外 API Key 生图。
    features:
    - 对话批量生图：一条消息拆成多个 Prompt 逐张生成并收进图库，支持 GIF 动图
    - AI 画布：看得懂草图与圈选，圈出剑换成斧头、火柴人草图成图，在原页面改图
    - 灵感库与 Agent 套用：500+ 案例库检索风格模板自动套用；同一提示词让多个模型各出一版横向对比
    - 多后端：Gemini、OpenAI / Compatible、Seedream、DashScope、Grok Imagine、GLM-Image 与本地 ComfyUI
    - BYOK 订阅复用：已有 ChatGPT、Grok、Google 订阅登录即可生图，API Key 经 DSH Credentials 保存不回显明文
    tags: *id001
    flag: 社区项目（Apache-2.0，非 DeepSeek 官方）；生图走第三方后端，注意各 Provider 的内容政策与费用
    notes: 仓库 shanliuling/dsh-image-gen，npm 包 dsh-image-gen，README 标 v0.11.3（npm registry 实时版本，文章只写 @latest）。README 安装命令带 pnpm 前缀（pnpm dsh plugin ...），本站 install 用等价的无前缀写法；从源码装可用 `dsh plugin --profile web add git+https://github.com/shanliuling/dsh-image-gen.git`。生图为 BYOK 模式，支持订阅账号登录复用额度。文章（wx-shixiang）称「500+ Prompt 灵感库、多模型对比、订阅免 Key」，与 README 一致。
    repo_confirmed: true
    category_label: 视觉与设计
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-image-gen/
  generated: true
---

让 Agent 本身学会画图的原生图像创作插件：一句话批量生成整组图，看得懂画布上的涂鸦与圈选，自动从 500+ 灵感库套用风格模板，另有 Studio 工作台、多模型横向对比与图库；已有 ChatGPT / Grok / Google 订阅可免额外 API Key 生图。
