---
title: dsh-anti-ads
description: DSH Web 广告拦截器，用四层独立防御拦截 dsh-ads 插件的所有广告位；只针对 dsh-ads，右下角小徽章记录拦掉的弹层数。
categories:
- fun
tags: &id001
- 去广告
- 梗
weight: 1010
params:
  plugin:
    id: dsh-anti-ads
    name: dsh-anti-ads
    category: fun
    status: community
    repo: https://github.com/HuanLinOTO/dsh-plugin-anti-ads
    install: dsh plugin --profile web add github:HuanLinOTO/dsh-plugin-anti-ads
    summary: DSH Web 广告拦截器，用四层独立防御拦截 dsh-ads 插件的所有广告位；只针对 dsh-ads，右下角小徽章记录拦掉的弹层数。
    features:
    - 四层防御：将 dsh-ads 的自身设置键写为全 false、广播其 retire 事件、从 DOM 清理门户、短路其动态层 fetch
    - 全部客户端实现，可在自带设置页一键移除
    - 持久化拦截状态默认开启，跨刷新持续生效
    - 仅作用于 dsh-ads 一个插件；「启用拦截」开关在设置页与徽章面板，关闭等于恢复广告
    tags: *id001
    flag: 社区项目，非官方；仅针对 dsh-ads，需与 dsh-ads 配合才有意义
    notes: README 提示：L4 广播的「本次关闭」是 dsh-ads 刻意做成不可撤销的，若已广播过，广告层要刷新页面才会回来；拦截器只清理 dsh-ads 自身设置的广告位。
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
    url: /plugins/dsh-anti-ads/
  generated: true
---

DSH Web 广告拦截器，用四层独立防御拦截 dsh-ads 插件的所有广告位；只针对 dsh-ads，右下角小徽章记录拦掉的弹层数。
