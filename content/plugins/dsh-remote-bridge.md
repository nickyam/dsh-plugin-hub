---
title: dsh-remote-bridge（远程访问桥）
description: 把 DSH 内核的私有 remote 协议翻译成版本化 REST，让 dsh-companion 等受信手机客户端在离开电脑后仍能用同一套聊天、会话、文件与设备能力；桌面端在设置里提供「手机设置」面板，远程访问默认关闭、不启用时只监听回环地址。
categories:
- remote
tags: &id001
- 远程访问
- 手机配对
- REST
- 隧道
weight: 1010
params:
  plugin:
    id: dsh-remote-bridge
    name: dsh-remote-bridge（远程访问桥）
    aliases:
    - dsh-workspace（旧名）
    - 远程访问桥
    category: remote
    status: community
    repo: https://github.com/westanke/dsh-remote-bridge
    install: dsh plugin --profile web add dsh-remote-bridge
    summary: 把 DSH 内核的私有 remote 协议翻译成版本化 REST，让 dsh-companion 等受信手机客户端在离开电脑后仍能用同一套聊天、会话、文件与设备能力；桌面端在设置里提供「手机设置」面板，远程访问默认关闭、不启用时只监听回环地址。
    features:
    - 协议桥接：私有 remote 协议转版本化 REST，聊天、会话、文件、设备全程留在同一台机器，配 dsh-companion 手机端（GitHub / Gitee）使用
    - 手机设置面板：DSH 设置内联折叠卡片，主列表五张（远程访问 / 外网隧道 / 设备 / 回收站 / App 下载）+ 默认收起的高级设置组（根目录 / 识图 / 插件）
    - 安全默认：远程访问默认关闭，未启用只监听回环地址，不会自动暴露到局域网；管理员可设绑定 IP、端口与新设备初始权限
    - 跨平台：Windows / macOS / Linux，安装包含编译产物无需在服务器重建；界面默认中文可切英文
    tags: *id001
    flag: 社区项目（AGPL-3.0，非 DeepSeek 官方）；远程访问把本机开放给手机，注意信任边界
    notes: 仓库 westanke/dsh-remote-bridge（main 分支），npm 包 dsh-remote-bridge，README 版本 v2.11.1。由 dsh-workspace 在 2.0.4 改名而来；REST 前缀 /dsh-workspace-api 与状态目录 dsh-workspace 为兼容旧 App 刻意保留，属预期行为。务必用 >= v2.0.4。环境要求 DSH 内核 >=0.2.2-rc.1 <0.3.0、Node.js ^22.19.0 或 >=24、默认端口 3090 可用。它是文章（wx-top10-30d）第 9 名已弃用的 dsh-remote-web-ui（@linxin666）的接替者；本站只收接替者，不收弃用包。
    repo_confirmed: true
    gh:
      stars: 6
      forks: 0
      issues: 3
      language: TypeScript
      license: AGPL-3.0
      pushed_at: '2026-11-18T22:06:27Z'
      archived: false
      slug: westanke/dsh-remote-bridge
      stars_label: '6'
      forks_label: '0'
      pushed_date: '2026-11-18'
      updated_label: 5 天前有提交
      updated_days: 5
      stale: false
    entry_updated: '2026-11-17'
    category_label: 移动端与远程
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-remote-bridge/
  generated: true
---

把 DSH 内核的私有 remote 协议翻译成版本化 REST，让 dsh-companion 等受信手机客户端在离开电脑后仍能用同一套聊天、会话、文件与设备能力；桌面端在设置里提供「手机设置」面板，远程访问默认关闭、不启用时只监听回环地址。
