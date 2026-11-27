---
title: ego-browser（看得见的 Agent 浏览器）
description: 把 ego-lite（给 AI Agent 用的 Chromium）接进 DSH，并在右侧边栏开一扇实时的窗：agent 在点哪里、滚到哪、卡在哪个验证码上都看得见，你也能直接在画面上点一下把它接管过来。
categories:
- tool
tags: &id001
- 浏览器
- 可观察
- 人机接管
weight: 1030
params:
  plugin:
    id: dsh-ego-browser
    name: ego-browser（看得见的 Agent 浏览器）
    aliases:
    - ego
    - 可观察浏览器
    - 接管浏览器
    category: tool
    status: community
    repo: https://github.com/omdsh-dev/dsh-ego-browser
    install: dsh plugin --profile desktop add dsh-ego-browser
    summary: 把 ego-lite（给 AI Agent 用的 Chromium）接进 DSH，并在右侧边栏开一扇实时的窗：agent 在点哪里、滚到哪、卡在哪个验证码上都看得见，你也能直接在画面上点一下把它接管过来。
    features:
    - 实时观察窗：SSE 推流 + 标签条 + 历史抽屉，画面后端可选 CDP JPEG 或 FFmpeg H.264
    - 看得见也控得住：监控窗里点击、拖拽、滚动会回传到真实浏览器，需要时亲手接管，不必打断 agent 重来
    - 35 个 ego_* 结构化工具：任务空间、语义树快照、标签管理、导航与等待、点击填写悬停拖拽、截图下载上传、原始 CDP 与多步脚本
    - 登录态导入：ego_login_import 把日常 Chrome / Edge / Brave 的 cookie 按域名搬进来，优先走扩展桥接（Chrome 127+ 的 ABE 也能用），cookie 值不进日志
    - 人机验证与等人：ego_captcha 探测，ego_wait_for_human 在 CAPTCHA / 登录 / 2FA 上停下来等你
    - 健壮性：冷启动只重试 CDP 瞬态错误、worker 单实例守卫 + 崩溃自愈、卸载不阻塞宿主退出
    - 轨迹与回放：按会话写 JSONL 到 ~/.dsh/plugin-data/ego-browser/trajectories，ego_replay 可重放；默认对填写的文本脱敏
    - 平台自足：Linux / Windows / macOS 自动探测 Chrome，内置 --no-sandbox wrapper，root / 容器 / 无显示器免配置
    tags: *id001
    flag: 与 Da1dr1em/dsh-ego-browser 是两个仓库，别混
    notes: 需要 DSH ≥ 0.1.2-rc.1、Node ≥ 22。侧栏优先注册进 DSH 0.2.1 起的原生右侧边栏；宿主没有原生侧栏时回退到 dsh-better-sidebar（≥ 0.12.2，推荐 ≥ 0.17.1），两个都没有就只留工具、不显示面板。Windows 上 Chrome / Edge ≥ 127 的 profile 复制路径会读到 0 条 cookie（ABE 绑定原始路径），必须走扩展桥接。README 徽章写 MIT，但 GitHub 识别的许可证是 NOASSERTION（自定义条款），要商用或再分发先自己读一眼 LICENSE。
    repo_confirmed: true
    gh:
      stars: 586
      forks: 59
      issues: 0
      language: TypeScript
      license: GPL-3.0
      pushed_at: '2026-11-23T11:43:36Z'
      archived: false
      slug: omdsh-dev/dsh-ego-browser
      stars_label: '586'
      forks_label: '59'
      pushed_date: '2026-11-23'
      updated_label: 3 天前有提交
      updated_days: 3
      stale: false
    entry_updated: '2026-11-19'
    category_label: 工具与能力
    status_label: 社区
    weight: 1030
    url: /plugins/dsh-ego-browser/
  generated: true
lastmod: '2026-11-19'
---

把 ego-lite（给 AI Agent 用的 Chromium）接进 DSH，并在右侧边栏开一扇实时的窗：agent 在点哪里、滚到哪、卡在哪个验证码上都看得见，你也能直接在画面上点一下把它接管过来。
