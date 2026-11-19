---
title: dsh-deepseek-web-login
description: 非官方的 DSH 插件：通过浏览器登录 chat.deepseek.com 捕获登录态凭证，把网页版模型作为 LLM 提供者驱动 agent 的工具调用、思考流与图片理解，不调用官方 API。
categories:
- model
tags: &id001
- 网页凭证
- 免API Key
- 非官方
weight: 1020
params:
  plugin:
    id: dsh-deepseek-web-login
    name: dsh-deepseek-web-login
    category: model
    status: community
    repo: https://github.com/cv-superding/dsh-deepseek-web-login
    install: dsh plugin --profile desktop add github:cv-superding/dsh-deepseek-web-login
    summary: 非官方的 DSH 插件：通过浏览器登录 chat.deepseek.com 捕获登录态凭证，把网页版模型作为 LLM 提供者驱动 agent 的工具调用、思考流与图片理解，不调用官方 API。
    features:
    - 网页登录无 API Key：在 Electron 独立分区窗口登录，旁路捕获 Authorization、cookie 与指纹头
    - PoW 求解：在浏览器页面上下文里执行 DeepSeek 的 wasm PoW 挑战，WASM 地址自动发现、失败回退
    - 流式兼容：同时兼容 response/fragments 与 thinking_content/content 两套 SSE 格式，按逻辑流去重
    - 工具调用：用提示词 JSON 协议 + 流式过滤器合成 tool-call 块，补足网页端缺失的 function calling
    - 图片输入：走网页端文件上传通道，同一张图多处出现自动去重
    - 账号库与防风控：本机保存多个账号可一键切换；设置页提供请求节流、随机间隔、会话清理与调用台账，0.7.0 起 PoW 改为在真实浏览器页面里求解、按 DSH 会话复用连接以降低被识别概率（仍需 Edge/Chrome，README 明确不保证不被封）
    tags: *id001
    flag: 涉及账号凭证与网页端私有接口，注意安全与条款；非 DeepSeek 官方客户端；一个账号同一时间只开一个聊天窗口，多开可能触发临时封禁
    notes: README 提供三种安装方式（Release tgz / git 装配 / npm），主推桌面端：dsh plugin --profile desktop add github:cv-superding/dsh-deepseek-web-login；npm 装写作 dsh plugin --profile desktop add dsh-deepseek-web-login。这是网页端私有接口的非官方客户端，非反向代理或 DOM 自动化。文章（wx-you-liao）只给 git 来源并称更新失败无法回滚，README 说明市场条目当前将该包标为 npm 为 null（未发布）、仅支持 git 来源，故更新需从 GitHub 拉取；该文强调的 40 万字符 / 并发 2 次等风控阀门属文章实测口径，本站不采信为结论。
    repo_confirmed: true
    gh:
      stars: 382
      forks: 47
      issues: 18
      language: JavaScript
      license: Apache-2.0
      pushed_at: '2026-11-15T09:05:07Z'
      archived: false
      slug: cv-superding/dsh-deepseek-web-login
      stars_label: '382'
      forks_label: '47'
      pushed_date: '2026-11-15'
    category_label: 免费模型与接入
    status_label: 社区
    weight: 1020
    url: /plugins/dsh-deepseek-web-login/
  generated: true
---

非官方的 DSH 插件：通过浏览器登录 chat.deepseek.com 捕获登录态凭证，把网页版模型作为 LLM 提供者驱动 agent 的工具调用、思考流与图片理解，不调用官方 API。
