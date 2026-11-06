---
title: dsh-deepseek-web-login
description: 非官方的 DSH 插件：通过浏览器登录 chat.deepseek.com 捕获登录态凭证，把网页版模型作为 LLM 提供者驱动 agent 的工具调用、思考流与图片理解，不调用官方 API。
categories:
- model
tags: &id001
- 网页凭证
- 免API Key
- 非官方
weight: 1010
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
    tags: *id001
    flag: 涉及账号凭证与网页端私有接口，注意安全与条款；非 DeepSeek 官方客户端
    notes: README 提供三种安装方式（Release tgz / git 装配 / npm），主推桌面端：dsh plugin --profile desktop add github:cv-superding/dsh-deepseek-web-login；npm 装写作 dsh plugin --profile desktop add dsh-deepseek-web-login。这是网页端私有接口的非官方客户端，非反向代理或 DOM 自动化。
    refs:
    - id: wx-quanjing
      title: DeepSeek Harness 插件全景推荐：14 大类、36 款值得装的插件
      url: https://mp.weixin.qq.com/s/btWqFHCDWwgAD_uj2n0MDw
      kind_label: 公众号
      publisher: 智宇AI说
    source_count: 1
    repo_confirmed: true
    category_label: 免费模型与接入
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-deepseek-web-login/
  generated: true
---

非官方的 DSH 插件：通过浏览器登录 chat.deepseek.com 捕获登录态凭证，把网页版模型作为 LLM 提供者驱动 agent 的工具调用、思考流与图片理解，不调用官方 API。
