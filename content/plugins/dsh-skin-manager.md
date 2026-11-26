---
title: dsh-skin-manager（鲸鱼娘皮肤管理器）
description: 鲸鱼娘皮肤系列配套的常驻皮肤管理模块：在 DSH 设置页注册「皮肤管理」，发现并互斥切换官方默认与已安装皮肤，渲染各皮肤自带的开关、下拉、滑杆与可见时段配置；同时装多套皮肤时必须启用它。
categories:
- fun
tags: &id001
- 皮肤
- 主题
- 换肤
weight: 1010
params:
  plugin:
    id: dsh-skin-manager
    name: dsh-skin-manager（鲸鱼娘皮肤管理器）
    aliases:
    - skin-manager
    - '@smalltailqwq/dsh-client-ui-skin-deep-whale-manager'
    - 皮肤管理器
    category: fun
    status: community
    repo: https://github.com/Small-tailqwq/dsh-deep-whale/tree/main/skin-manager
    install: dsh plugin --profile web add '@smalltailqwq/dsh-client-ui-skin-deep-whale-manager'
    summary: 鲸鱼娘皮肤系列配套的常驻皮肤管理模块：在 DSH 设置页注册「皮肤管理」，发现并互斥切换官方默认与已安装皮肤，渲染各皮肤自带的开关、下拉、滑杆与可见时段配置；同时装多套皮肤时必须启用它。
    features:
    - 从当前 Web profile 依赖里发现所有带有效 skin.json 的皮肤，官方默认与任意皮肤之间互斥切换
    - 启动兜底：两套及以上皮肤同时启用时原子回退官方默认；桌面切换同步核对宿主插件清单与页面激活标记
    - 渲染皮肤通过版本化协议暴露的开关/下拉/复选/滑杆/颜色/可见时段配置（当前 v2，兼容 v1 声明）
    - DSH 0.1.7+ 自动停用不支持当前版本的皮肤，点「切换」确认后按皮肤版本+DSH 版本精确放行
    - 管理页可把官方预设插件图标切成当前皮肤提供的图形，默认关闭
    - 窄屏下再点一次已打开的全局面板入口即可回到对话
    tags: *id001
    flag: 本身不是皮肤；只装一套皮肤时可选，同时装多套皮肤则必须装并一直保持启用
    notes: 官方仓库 Small-tailqwq/dsh-deep-whale 的 skin-manager 子目录，npm 包 @smalltailqwq/dsh-client-ui-skin-deep-whale-manager。README 明确：已装 @linxin666/dsh-web-all 的用户请用 dsh-web 自带皮肤中心及其适配皮肤，不要装本管理器，两套发行不能同 profile 叠装。与皮肤一起装、首次装完重启一次 DSH；两套皮肤都装时首次重启会显示官方默认，这是管理器把它们都关掉等用户去选，属预期行为。管理器自身 MIT 许可，皮肤美术资源另有 CC BY-NC-SA 4.0 禁商用条款（见各皮肤条目）。
    repo_confirmed: true
    gh:
      stars: 3152
      forks: 103
      issues: 6
      language: TypeScript
      license: NOASSERTION
      pushed_at: '2026-11-26T08:29:37Z'
      archived: false
      slug: Small-tailqwq/dsh-deep-whale
      stars_label: '3152'
      forks_label: '103'
      pushed_date: '2026-11-26'
      updated_label: 今天有提交
      updated_days: 0
      stale: false
    entry_updated: '2026-11-19'
    category_label: 娱乐与彩蛋
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-skin-manager/
  generated: true
lastmod: '2026-11-19'
---

鲸鱼娘皮肤系列配套的常驻皮肤管理模块：在 DSH 设置页注册「皮肤管理」，发现并互斥切换官方默认与已安装皮肤，渲染各皮肤自带的开关、下拉、滑杆与可见时段配置；同时装多套皮肤时必须启用它。
