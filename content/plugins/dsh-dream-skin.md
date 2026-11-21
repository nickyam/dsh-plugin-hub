---
title: dsh-dream-skin（Dream Skin 换肤）
description: 给 DSH Web 换肤的原生插件：8 套原创 Mirage 主题在「设置 → 个性化皮肤」一键切换，支持自定义壁纸（本地图 / 图片 URL / 渐变 / 必应每日 / 轮播）、叠加强调色、毛玻璃 / 液态玻璃材质与主题包导入导出分享。纯走 ctx.theme 官方扩展点，不改安装包、不注入。
categories:
- fun
tags: &id001
- 换肤
- 主题
- 壁纸
- 强调色
weight: 1010
params:
  plugin:
    id: dsh-dream-skin
    name: dsh-dream-skin（Dream Skin 换肤）
    aliases:
    - Dream Skin
    - 梦幻皮肤
    - 个性化皮肤
    category: fun
    status: community
    repo: https://gitcode.com/LLLAAAAA/dsh-dream-skin
    install: dsh plugin --profile web add dsh-dream-skin
    summary: 给 DSH Web 换肤的原生插件：8 套原创 Mirage 主题在「设置 → 个性化皮肤」一键切换，支持自定义壁纸（本地图 / 图片 URL / 渐变 / 必应每日 / 轮播）、叠加强调色、毛玻璃 / 液态玻璃材质与主题包导入导出分享。纯走 ctx.theme 官方扩展点，不改安装包、不注入。
    features:
    - 8 套原创主题（Mirage 幻梦系列）深浅兼顾，每套自带专属弥散光背景，一键切换不动用户调过的参数
    - 壁纸 2.0：本地图 / 图片 URL / 渐变预设 / 必应每日，可调透明度、模糊、填充方式与取景偏移；支持图片链接或本地文件夹轮播
    - 每用户强调色 Accent：12 个色块 + 选色盘 + 随机，以 overrideTokens 叠加层改色、不动皮肤本身
    - 主题包导入 / 导出 / 分享：一个 *.dsh-theme.json = manifest + 全套 tokens，可复制分享链接（编码进 URL hash），本地主题包库支持收藏与随机换肤
    - 玻璃材质（毛玻璃 / 液态玻璃）与低功耗模式：一键关掉全部 backdrop-filter 与壁纸模糊，三态自动跟随系统「减少透明度」
    - 三层持久化（localStorage + 宿主侧 dream-skin.json），桌面版换端口、重启不丢皮肤与壁纸
    tags: *id001
    flag: 官方仓库已从 GitHub 迁至 gitcode（原 GitHub 账号封禁），npm 包 dsh-dream-skin 已正式发布；与独立桌面软件 xxloocee/Dream-Skin 不是同一项目
    notes: 官方仓库 gitcode.com/LLLAAAAA/dsh-dream-skin（npm 包 dsh-dream-skin，latest 11.16.0）。仓库在 GitCode 而非 GitHub，本站 repo 字段如实填 GitCode 地址；GitHub 数据抓取只覆盖 github.com 仓库，此条无星标数据属正常。安装官方唯一命令 dsh plugin --profile web add dsh-dream-skin，报错补 -w；刚发版 24h 内 README 建议写死版本号。文章只给包名「dsh-dream-skin」与「多套主题 + 强调色 + 壁纸 + 上传自己图片做壁纸」描述，与仓库 README 吻合，据此收录；文章未给仓库地址，仓库由包名检索核实。注意区分：xxloocee/Dream-Skin 是需下载 dmg/exe 的独立桌面换肤软件、非 DSH 插件，DamonYanglong/dsh-dream-skin 虽同名但无 8 套主题与主题包系统，二者均未收。
    repo_confirmed: true
    gh: null
    entry_updated: '2026-11-21'
    category_label: 娱乐与彩蛋
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-dream-skin/
  generated: true
---

给 DSH Web 换肤的原生插件：8 套原创 Mirage 主题在「设置 → 个性化皮肤」一键切换，支持自定义壁纸（本地图 / 图片 URL / 渐变 / 必应每日 / 轮播）、叠加强调色、毛玻璃 / 液态玻璃材质与主题包导入导出分享。纯走 ctx.theme 官方扩展点，不改安装包、不注入。
