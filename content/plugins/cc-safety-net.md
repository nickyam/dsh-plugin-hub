---
title: cc-safety-net（执行前防护）
description: 在工具调用真正执行之前先看一眼命令要干什么：git reset --hard、git push --force、危险目标的 rm -rf、find -delete、PowerShell Remove-Item 一律拦下，读取 SSH 私钥、.env、~/.aws、CLI 凭据的动作也拦。它解析命令本身做什么，套一层 bash -c 或 python -c、换个参数顺序都藏不住。
categories:
- security
tags: &id001
- 安全
- 命令拦截
- 凭据保护
weight: 1020
params:
  plugin:
    id: cc-safety-net
    name: cc-safety-net（执行前防护）
    aliases:
    - 安全网
    - 命令防护
    - safety net
    category: security
    status: community
    repo: https://github.com/kenryu42/cc-safety-net
    install: npx -y cc-safety-net@latest install --deepseek-harness
    summary: 在工具调用真正执行之前先看一眼命令要干什么：git reset --hard、git push --force、危险目标的 rm -rf、find -delete、PowerShell Remove-Item 一律拦下，读取 SSH 私钥、.env、~/.aws、CLI 凭据的动作也拦。它解析命令本身做什么，套一层 bash -c 或 python -c、换个参数顺序都藏不住。
    features:
    - 拦破坏性命令：不只认字面，藏在 bash -c / python -c 里的也认得；PowerShell 脚本文件会读盘判内容
    - 拦凭据访问：SSH 私钥、.env、~/.aws、各家编码 CLI 的凭据目录，shell 与 agent 的文件工具两条路都管
    - 三档预设 + 逐条开关：Standard / Strict / Paranoid，配本地网页 GUI，不用手写配置
    - 规则书：官方提供 Terraform、AWS、gcloud、Azure 规则包，也能写自己的 JSON；规则书只能加限制、不能删内置规则
    - 团队策略共享：把策略目录提交进 git，别人 clone 或云端会话继承同一套规则
    - 可嵌入：Node.js 里直接调 checkCommand，不装 hook 也能复用同一套判定
    - 配置坏了不会失守：策略文件解析失败时回落到安全默认值，而不是静默放行
    tags: *id001
    flag: 是拦截器不是沙箱，不隔离进程、不管网络出口
    notes: 定位要说清——它 deny 调用，但不设置文件权限、不监控网络出口、不把进程关进容器，真正的沙箱还得靠宿主。路径匹配基本按 POSIX 来，PowerShell 覆盖有限。Node 18 以上，Windows / macOS / Linux 都能跑。装完先用 doctor 自检、status 看状态，怀疑没生效时先确认策略文件能不能正常解析（解析失败是有意回落，不是坏了）。README 把 DSH 的安装细节放在官网文档页（ccsafetynet.com/docs/installation/deepseek-harness），命令走 --deepseek-harness 这个开关。它同时支持 Claude Code、Codex、Cursor、Copilot CLI、Gemini CLI 等十几个 CLI，DSH 只是其中一个接入点。
    repo_confirmed: true
    gh:
      stars: 2075
      forks: 98
      issues: 5
      language: TypeScript
      license: MIT
      pushed_at: '2026-11-18T17:47:46Z'
      archived: false
      slug: kenryu42/cc-safety-net
      stars_label: '2075'
      forks_label: '98'
      pushed_date: '2026-11-18'
    category_label: 安全与治理
    status_label: 社区
    weight: 1020
    url: /plugins/cc-safety-net/
  generated: true
---

在工具调用真正执行之前先看一眼命令要干什么：git reset --hard、git push --force、危险目标的 rm -rf、find -delete、PowerShell Remove-Item 一律拦下，读取 SSH 私钥、.env、~/.aws、CLI 凭据的动作也拦。它解析命令本身做什么，套一层 bash -c 或 python -c、换个参数顺序都藏不住。
