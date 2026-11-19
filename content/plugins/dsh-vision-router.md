---
title: dsh-vision-router（视觉路由）
description: 给纯文本 DSH 模型装上「眼睛」：内置免 Key 视觉链与十多个像素级视觉工具，看图问答、目标定位、裁剪取色、抠图、截图等都能当普通工具调用来做；需要时点输入框旁的 👁 Vision 开关，图进入会话日志、可溯源可复现。
categories:
- visual
tags: &id001
- 视觉
- 免Key
- 像素工具
- 看图
weight: 1010
params:
  plugin:
    id: dsh-vision-router
    name: dsh-vision-router（视觉路由）
    aliases:
    - deepstare
    - 视觉路由
    - dsh 的眼睛
    - 免Key视觉链
    category: visual
    status: community
    repo: https://github.com/ysr666/dsh-vision-router
    install: dsh plugin --profile web add dsh-vision-router
    summary: 给纯文本 DSH 模型装上「眼睛」：内置免 Key 视觉链与十多个像素级视觉工具，看图问答、目标定位、裁剪取色、抠图、截图等都能当普通工具调用来做；需要时点输入框旁的 👁 Vision 开关，图进入会话日志、可溯源可复现。
    features:
    - 免 Key 开箱可用：内置免费视觉后端，一键安装、无需 Python、无需自己配 Key；另有匿名 cloud 兜底，默认即会把图片发给云端视觉模型（涉密内容须开 strict local-only）
    - 像素级视觉工具：看图问答、grounding 定位、crop 裁剪、取色、像素比对、OCR、SVG 描摹、抠图与截图等十多个 deep tools，输出可度量可复现
    - 像普通工具调用一样用图：开启 👁 Vision 后，图片轮次走正常 tool-calling 流程，图能进 DSH 会话日志，不再「看完就忘」
    - 本地 OCR 可选：v3.4.0 起本地 OCR 改为手动开启，可复用系统 Tesseract（chi_sim+eng）或按需装 SHA 校验的 Tesseract.js/WASM；大多数用户无需装
    - 第三方审计徽章：README 挂有 dsh-recommend 认证、dshbase 安装测试与 DeepGuard 审计标记（历史 v2.0.1），站方未实测
    tags: *id001
    flag: 社区项目；默认会把图片/裁剪图发给云端视觉模型（含匿名兜底），涉密或敏感素材请开 strict local-only；DSH >=0.2.1-rc.5 <0.3.0-0、Node.js >=24.9.0
    notes: 仓库 ysr666/dsh-vision-router（GitHub 搜索同名项目很多，本条取 README 详实、带 dsh-recommend 认证与 DeepGuard 审计标记、★ 数遥遥领先的 ysr666 主仓）。文章把它在视频里的叫法写作 deepstare，插件包名是 dsh-vision-router。README 有专门的「Data flow and strict local-only use」小节说明数据外发。
    repo_confirmed: true
    gh:
      stars: 1286
      forks: 63
      issues: 4
      language: JavaScript
      license: MIT
      pushed_at: '2026-11-19T01:27:38Z'
      archived: false
      slug: ysr666/dsh-vision-router
      stars_label: '1286'
      forks_label: '63'
      pushed_date: '2026-11-19'
    category_label: 视觉与设计
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-vision-router/
  generated: true
---

给纯文本 DSH 模型装上「眼睛」：内置免 Key 视觉链与十多个像素级视觉工具，看图问答、目标定位、裁剪取色、抠图、截图等都能当普通工具调用来做；需要时点输入框旁的 👁 Vision 开关，图进入会话日志、可溯源可复现。
