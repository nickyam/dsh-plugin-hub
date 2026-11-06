---
title: DSH Better Sidebar
description: 开放的侧边栏底座：在 DSH 里加一条原生右侧栏 + 自绘底部面板，把文件渲染 / 编辑、终端、侧边对话、Git、子代理等面板整合到一起，并通过 ctx.betterSidebar 服务向所有插件开放，第三方可注册新侧边栏页面。
categories:
- ui
tags: &id001
- 侧边栏
- Git
- 效率
weight: 1020
params:
  plugin:
    id: dsh-better-sidebar
    name: DSH Better Sidebar
    aliases:
    - DSH-better-sidebar
    - Better Sidebar
    category: ui
    status: community
    repo: https://github.com/omdsh-dev/DSH-better-sidebar
    install: dsh plugin --profile web add dsh-better-sidebar@latest
    summary: 开放的侧边栏底座：在 DSH 里加一条原生右侧栏 + 自绘底部面板，把文件渲染 / 编辑、终端、侧边对话、Git、子代理等面板整合到一起，并通过 ctx.betterSidebar 服务向所有插件开放，第三方可注册新侧边栏页面。
    features:
    - 右侧栏 + 底部面板双工作台
    - 内置文件渲染/编辑、终端、侧边对话、Git、子代理页面
    - 开放 ctx.betterSidebar 服务，支持三方扩展注册新页面
    - 与 dsh-web-all 全家桶配合作为默认右侧面板
    tags: *id001
    flag: 需按 DSH 版本选对应插件版本
    notes: 安装前硬刷新浏览器（Cmd/Ctrl+Shift+R）。注意版本匹配：DSH 0.2.2-rc.1+ 用 @0.30.1；0.2.1 线（含当前 latest）需钉 @0.28.2；更老的 host 见 README 版本对照表——装错版本会触发版本拒绝错误。
    refs:
    - id: baike-dsh
      title: 百度百科：DeepSeek Harness
      url: https://baike.baidu.com/item/deepseek%20harness/68533699
      kind_label: 百科
      publisher: 百度百科
    - id: wx-quanjing
      title: DeepSeek Harness 插件全景推荐：14 大类、36 款值得装的插件
      url: https://mp.weixin.qq.com/s/btWqFHCDWwgAD_uj2n0MDw
      kind_label: 公众号
      publisher: 智宇AI说
    source_count: 2
    repo_confirmed: true
    category_label: 界面与体验
    status_label: 社区
    weight: 1020
    url: /plugins/dsh-better-sidebar/
  generated: true
---

开放的侧边栏底座：在 DSH 里加一条原生右侧栏 + 自绘底部面板，把文件渲染 / 编辑、终端、侧边对话、Git、子代理等面板整合到一起，并通过 ctx.betterSidebar 服务向所有插件开放，第三方可注册新侧边栏页面。
