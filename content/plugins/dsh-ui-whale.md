---
title: dsh-ui-whale
description: DSH Web UI 的常驻像素鲸鱼伙伴插件：在会话标题栏常驻一只手绘像素小鲸鱼，随会话快照实时反应——空闲眨眼、偶尔摆尾、思考时持续动、回合完成喷水、点击冒爱心、空闲久了睡觉，零核心改动。
categories:
- fun
tags: &id001
- 皮肤
- 像素风
- 桌宠
weight: 1010
params:
  plugin:
    id: dsh-ui-whale
    name: dsh-ui-whale
    category: fun
    status: community
    repo: https://github.com/lhh010/dsh-ui-whale
    install: dsh plugin --profile web add '@dsh-external/dsh-ui-whale@github:lhh010/dsh-ui-whale#v0.3.31'
    summary: DSH Web UI 的常驻像素鲸鱼伙伴插件：在会话标题栏常驻一只手绘像素小鲸鱼，随会话快照实时反应——空闲眨眼、偶尔摆尾、思考时持续动、回合完成喷水、点击冒爱心、空闲久了睡觉，零核心改动。
    features:
    - 常驻像素鲸鱼：会话标题栏右侧一只手绘像素小鲸鱼，随会话状态实时反应
    - 空闲眨眼、偶尔摆尾/动胸鳍；连续空闲 10 秒入睡（头顶灰色 Z），有活动立即醒来
    - 思考/运行/工作中：尾巴持续摆动 + 胸鳍扑动 + 眨眼更频繁
    - 回合完成时头顶喷水庆祝；点击鲸鱼左上角冒粉色爱心
    - 纯浏览器端 UI 呈现：不进入模型请求、不增加提示词、不改工具 schema；22 帧手绘像素画分层 CSS 渲染
    tags: *id001
    flag: 社区项目，非官方；注意 DSH 版本→插件版本对应关系，装错会崩
    notes: README 提示：DSH 版本决定装哪个插件版本（0.1.2-alpha.1 ~ 0.2.1-alpha.1 用新版）；pnpm 11 可能拦截 node-pty 等构建脚本，需在 ~/.dsh/profiles/web 下 pnpm approve-builds --all 后重装并硬刷新浏览器。
    refs:
    - id: baike-dsh
      title: 百度百科：DeepSeek Harness
      url: https://baike.baidu.com/item/deepseek%20harness/68533699
      kind_label: 百科
      publisher: 百度百科
    source_count: 1
    repo_confirmed: true
    category_label: 娱乐与彩蛋
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-ui-whale/
  generated: true
---

DSH Web UI 的常驻像素鲸鱼伙伴插件：在会话标题栏常驻一只手绘像素小鲸鱼，随会话快照实时反应——空闲眨眼、偶尔摆尾、思考时持续动、回合完成喷水、点击冒爱心、空闲久了睡觉，零核心改动。
