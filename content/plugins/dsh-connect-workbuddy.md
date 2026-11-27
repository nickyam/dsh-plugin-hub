---
title: dsh-connect-workbuddy（WorkBuddy 模型接入）
description: 把本机已登录的 WorkBuddy 账号（国内版 / 国际版）接入 DSH 模型选择器：模型目录带上游积分倍率、逐模型开关图片输入与思考、多账号池自动换号、每日签到与只读积分概览。仅复用本机登录态，不提供账号、不共享凭据。
categories:
- model
tags: &id001
- WorkBuddy
- 模型接入
- 积分倍率
- 多账号
weight: 1010
params:
  plugin:
    id: dsh-connect-workbuddy
    name: dsh-connect-workbuddy（WorkBuddy 模型接入）
    aliases:
    - WorkBuddy 模型接入
    - dsh-connect-workbuddy
    - WB 接入
    category: model
    status: community
    repo: https://github.com/dingminhua/dsh-connect-workbuddy
    install: dsh plugin --profile web add dsh-connect-workbuddy
    summary: 把本机已登录的 WorkBuddy 账号（国内版 / 国际版）接入 DSH 模型选择器：模型目录带上游积分倍率、逐模型开关图片输入与思考、多账号池自动换号、每日签到与只读积分概览。仅复用本机登录态，不提供账号、不共享凭据。
    features:
    - 国内版（workbuddy）与国际版（workbuddy-global）两个供应商可并行，设置页分 tab 管理，有账号的区域模型才出现在选择器
    - 模型管理：从上游刷新完整目录，逐项勾选启用、设默认推理档、关思考开关；倍率由上游给出、插件不写死，活动时段显示折后价
    - 只读积分：卡片与输入框胶囊显示积分读数，按当前会话选中模型自动切国内 / 国际版；排队、限流、恢复时间按上游原文如实显示
    - 账号池：勾选多账号签到与按模型测试，启用后失败自动换号；每日自动签到默认关闭
    - 可选能力默认关闭：模型自主生图 / 生视频工具、侧边栏整页入口、上游用量页身份对齐
    tags: *id001
    flag: 依赖 WorkBuddy 客户端接口（非官方开放 API），上游收紧时可能失效，README 明确提示账号风险
    notes: 官方仓库 github.com/dingminhua/dsh-connect-workbuddy（npm 包 dsh-connect-workbuddy，MIT）。文章只给包名「dsh-connect-workbuddy」与「把已登录 WorkBuddy 的模型放进 DSH 模型选择器」一句描述，与 README 核心定位吻合，据此收录；仓库由包名检索核实。功能细节（双供应商、倍率、账号池、生图/生视频工具等）均按官方 README 整理，不照抄文章。README 反复声明只复用本机登录态、不共享凭据、不绕过计费，且提醒上游可能限制非官方客户端；倍率、模型名、价格均为上游实时给出，本站不写死具体数字。另有 jojoman2024/dsh-workbuddy-connect、sixzjd/dsh-workbuddy-connect 等多个同类插件，功能相近但非同一仓库，未混收。
    repo_confirmed: true
    gh:
      stars: 2049
      forks: 207
      issues: 10
      language: TypeScript
      license: MIT
      pushed_at: '2026-11-26T17:20:29Z'
      archived: false
      slug: dingminhua/dsh-connect-workbuddy
      stars_label: '2049'
      forks_label: '207'
      pushed_date: '2026-11-26'
      stale: false
    entry_updated: '2026-11-21'
    category_label: 免费模型与接入
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-connect-workbuddy/
  generated: true
lastmod: '2026-11-21'
---

把本机已登录的 WorkBuddy 账号（国内版 / 国际版）接入 DSH 模型选择器：模型目录带上游积分倍率、逐模型开关图片输入与思考、多账号池自动换号、每日签到与只读积分概览。仅复用本机登录态，不提供账号、不共享凭据。
