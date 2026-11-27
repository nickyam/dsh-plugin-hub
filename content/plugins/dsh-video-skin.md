---
title: dsh-video-skin（视频皮肤）
description: 给 DSH 加一段视频皮肤：一段短片无声循环铺成聊天背景，另一段做有声开机动画并在片尾交叉溶解进界面；右下角半透明小圆钮调透明度，开机动画点一下即可跳过，零依赖。
categories:
- fun
tags: &id001
- 皮肤
- 主题
- 视频
weight: 1010
params:
  plugin:
    id: dsh-video-skin
    name: dsh-video-skin（视频皮肤）
    aliases:
    - dsh-video-skin
    - 视频皮肤
    - 开机动画皮肤
    category: fun
    status: community
    repo: https://github.com/Something11235/dsh-video-skin
    install: dsh plugin --profile web add dsh-video-skin@0.1.6
    summary: 给 DSH 加一段视频皮肤：一段短片无声循环铺成聊天背景，另一段做有声开机动画并在片尾交叉溶解进界面；右下角半透明小圆钮调透明度，开机动画点一下即可跳过，零依赖。
    features:
    - 聊天背景：短片循环铺满界面，无声，透明度在界面里的滑块实时调节，调完刷新仍在
    - 开机动画：一段有声短片，片尾交叉溶解进 DSH 界面，点击画面随时跳过
    - 零依赖；npm 预编译包 dsh-video-skin@0.1.6，也可从 github:Something11235/dsh-video-skin#main 装源码
    - 桌面版（Electron）索引注入表只在宿主启动时收集一次，装完必须完全退出并重新打开 DSH，刷新页面不够
    tags: *id001
    flag: 文章描述的「大肥鱼说欢迎回家、界面里走动工作休息」README 未证实，本站按 README 只记视频背景+有声开机动画
    notes: 官方仓库 Something11235/dsh-video-skin，npm 包 dsh-video-skin（latest 0.1.6），安装栏按 README 钉 0.1.6（不带版本号则跟随 latest）。卸载用 `dsh plugin --profile <profile> remove dsh-video-skin` 或仓库的 scripts/uninstall.ps1。文中把开机动画内容具象成「大肥鱼说欢迎回家」及界面内走动/工作/休息的桌宠动画，README 并无此描述，属文章口径不采信。
    repo_confirmed: true
    gh:
      stars: 139
      forks: 12
      issues: 8
      language: JavaScript
      license: MIT
      pushed_at: '2026-11-03T14:29:02Z'
      archived: false
      slug: Something11235/dsh-video-skin
      stars_label: '139'
      forks_label: '12'
      pushed_date: '2026-11-03'
      stale: false
    entry_updated: '2026-11-27'
    category_label: 娱乐与彩蛋
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-video-skin/
  generated: true
lastmod: '2026-11-27'
---

给 DSH 加一段视频皮肤：一段短片无声循环铺成聊天背景，另一段做有声开机动画并在片尾交叉溶解进界面；右下角半透明小圆钮调透明度，开机动画点一下即可跳过，零依赖。
