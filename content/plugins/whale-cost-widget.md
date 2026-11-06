---
title: 小鲸鱼记账挂件
description: 在 DSH Web/桌面端右下角常驻一只可拖拽吸附的小鲸鱼挂件，监控 DeepSeek 账户余额、今日已用与每轮对话消耗；泡泡、音效与交互可完全自定义，基础记账无需配置令牌。
categories:
- billing
tags: &id001
- 桌宠
- 成本可视化
weight: 1020
params:
  plugin:
    id: whale-cost-widget
    name: 小鲸鱼记账挂件
    aliases:
    - Balance Whale Widget
    - DeepSeek-Balance-Whale-Widget
    - 鲸鱼余额挂件
    category: billing
    status: unknown
    repo: https://github.com/MeteorNOX/DeepSeek-Balance-Whale-Widget
    install: dsh plugin --profile web add github:MeteorNOX/DeepSeek-Balance-Whale-Widget
    summary: 在 DSH Web/桌面端右下角常驻一只可拖拽吸附的小鲸鱼挂件，监控 DeepSeek 账户余额、今日已用与每轮对话消耗；泡泡、音效与交互可完全自定义，基础记账无需配置令牌。
    features:
    - 常驻自启与智能余额监控：随 DSH 界面自动出现，支持 API Key 或登录态取数，60 秒刷新带数字滚动动画
    - 零令牌小鲸鱼记账：通过余额下降观测「今日已用」，并监听本机会话事件按真实 token 用量换算「每轮对话消耗」
    - 完全可自定义的泡泡系统：文本/超链接/图片/随机语句模块化，支持 A/B 加权与跑马灯渐变样式
    - 细腻交互与多端适配：四边拖拽吸附、按压 Q 弹玩偶、移动端自研触摸接管
    - 多厂商余额与额度扩展：内置 34 个厂商模板，可添加任意自定义 API 查询多厂商余额
    tags: *id001
    notes: 基础记账功能无需配置令牌即可用；泡泡/音效/交互均可自定义。npm 包名为 dsh-whale-widget，也可从桌面端 plugin_manager 安装。
    refs:
    - id: wx-dabaihua
      title: DeepSeek Harness 是个啥？大白话讲透 + 10 分钟上手 + 好用插件清单
      url: http://mp.weixin.qq.com/s?__biz=MzkwMDMzMzE0Mg==&mid=2247488511&idx=1&sn=b8f08d42ca17c2895080d4180cd3d6c9
      kind_label: 公众号
      publisher: 微信公众号（原文署名待补）
    - id: wx-quanjing
      title: DeepSeek Harness 插件全景推荐：14 大类、36 款值得装的插件
      url: https://mp.weixin.qq.com/s/btWqFHCDWwgAD_uj2n0MDw
      kind_label: 公众号
      publisher: 智宇AI说
    source_count: 2
    repo_confirmed: true
    category_label: 模型与计费
    status_label: 原文未说明
    weight: 1020
    url: /plugins/whale-cost-widget/
  generated: true
---

在 DSH Web/桌面端右下角常驻一只可拖拽吸附的小鲸鱼挂件，监控 DeepSeek 账户余额、今日已用与每轮对话消耗；泡泡、音效与交互可完全自定义，基础记账无需配置令牌。
