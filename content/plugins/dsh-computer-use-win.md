---
title: dsh-computer-use-win（Windows 桌面操控）
description: 让 DSH 看懂并操作真实的 Windows 桌面：找到按钮与输入框、读出屏幕文字、点击打字、切换管理窗口；网页默认在 DSH 自己的浏览器后台完成、不动你的鼠标，用到鼠标键盘时有明显提示、按 Esc 随时停止。
categories:
- tool
tags: &id001
- 桌面操控
- Windows
- 电脑控制
- 工具
weight: 1010
params:
  plugin:
    id: dsh-computer-use-win
    name: dsh-computer-use-win（Windows 桌面操控）
    aliases:
    - dsh-computer-use
    - Windows 电脑操控
    - 桌面控制
    category: tool
    status: community
    repo: https://github.com/Yu-tao-Li/dsh-computer-use-win
    install: dsh plugin --profile desktop add dsh-computer-use-win
    summary: 让 DSH 看懂并操作真实的 Windows 桌面：找到按钮与输入框、读出屏幕文字、点击打字、切换管理窗口；网页默认在 DSH 自己的浏览器后台完成、不动你的鼠标，用到鼠标键盘时有明显提示、按 Esc 随时停止。
    features:
    - Windows 桌面操控：屏幕文字识别、按钮/输入框定位、鼠标键盘操作、窗口管理
    - 不抢前台：网页任务在 DSH 自带浏览器后台完成，不抢焦点、不动用户鼠标
    - 看得见的控制：浮窗按步骤显示思考与操作，用到键鼠时屏幕边缘发亮并给提示条
    - 随时叫停：按 Esc 立即停止当前一轮操作
    - 25 个操作工具 + 1 个管理入口，中英文设置界面
    tags: *id001
    flag: 社区项目；仅 Windows；能真实操作桌面与键鼠，涉及账号/付款操作请全程留意并按需用 Esc 停止
    notes: 文章写的是「dsh-computer-use，目前只有 Windows 版」，据此取 Yu-tao-Li/dsh-computer-use-win（README 明确 Windows 专属、npm 包 dsh-computer-use-win，registry 200）。GitHub 上另有一个 Anionex/dsh-computer-use 是 macOS 版（描述为 Native macOS control），与文章「只有 Windows 版」不符，未收。文章把它当作 dsh-computer-use 介绍，本站以实际 Windows 仓库名建条目并留别名。
    repo_confirmed: true
    gh:
      stars: 796
      forks: 23
      issues: 1
      language: JavaScript
      license: MIT
      pushed_at: '2026-11-18T16:04:56Z'
      archived: false
      slug: Yu-tao-Li/dsh-computer-use-win
      stars_label: '796'
      forks_label: '23'
      pushed_date: '2026-11-18'
      updated_label: 2 天前有提交
      updated_days: 2
      stale: false
    entry_updated: '2026-11-17'
    category_label: 工具与能力
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-computer-use-win/
  generated: true
---

让 DSH 看懂并操作真实的 Windows 桌面：找到按钮与输入框、读出屏幕文字、点击打字、切换管理窗口；网页默认在 DSH 自己的浏览器后台完成、不动你的鼠标，用到鼠标键盘时有明显提示、按 Esc 随时停止。
