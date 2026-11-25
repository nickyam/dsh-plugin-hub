---
title: dsh-meme（表情包发图）
description: DSH 的表情包插件：输入框旁一键发图，按图库/情绪筛选与搜索，AI 按聊天气氛主动斗图，内置大肥鱼图库；图库可上传入库、扫描新增、ZIP 导入导出，或从市场一键安装，也可经 dsh-im 把表情以原生图片消息发到 QQ/微信/飞书。
categories:
- fun
tags: &id001
- 表情包
- 斗图
- 图库
- 发图
weight: 1010
params:
  plugin:
    id: dsh-meme
    name: dsh-meme（表情包发图）
    aliases:
    - 表情包发图
    - 斗图插件
    - dsh-meme
    category: fun
    status: community
    repo: https://github.com/yyh-001/dsh-meme
    install: dsh plugin --profile web add dsh-meme
    summary: DSH 的表情包插件：输入框旁一键发图，按图库/情绪筛选与搜索，AI 按聊天气氛主动斗图，内置大肥鱼图库；图库可上传入库、扫描新增、ZIP 导入导出，或从市场一键安装，也可经 dsh-im 把表情以原生图片消息发到 QQ/微信/飞书。
    features:
    - 一键发图：输入框点 😊 搜图/筛选，默认把原图作为附件发给 AI（可在设置关闭），关掉「点图直接发送」后只插光标处随文字发
    - 主动斗图：AI 按聊天情绪自己找图接梗，分关闭/看气氛/活跃/每轮都发四档，提示词可改
    - IM/手机斗图：经 dsh-im 接入 QQ/微信/飞书后以原生图片消息发出，手机经局域网 IP 打开 DSH Web 收发（默认关）
    - 学会新图与整理图库：上传说「把这张图入库」自动识别分类描述，meme_list/meme_update 让 AI 列清单查重改分类，删除留面板防误删
    - 开箱即用：内置大肥鱼图库 24 张，零第三方运行依赖，Node 内置 SQLite；MIT
    tags: *id001
    flag: Node.js >=22.13.0；默认把原图作为附件发给 AI（可关）；与站内 dsh-emoji（行内表情）、dsh-nekowhale-stickers（带标注的表情知识库）是不同插件
    notes: 官方仓库 github.com/yyh-001/dsh-meme（npm 包 dsh-meme，MIT，默认分支 main）。文章只给包名 dsh-meme 与「输入框附近选表情包 + 搜索分类导入导出 + 默认把原图作附件发给 AI（可关）」，与 README 逐条吻合，据此收录；仓库由包名检索核实。文章示例安装命令 dsh plugin --profile web add dsh-meme 与 README 一致。文章提醒「默认发原图给 AI 的行为可在设置关闭，需结合实际模型链路判断数据流向」，这点在 README 也有明确说明，作为 notes 保留。它主打输入框发图/图库管理，与站内 dsh-emoji（hellodigua，给 AI 回复加行内表情）和 dsh-nekowhale-stickers（Loping151，322 张标注场景的表情知识库）功能侧重不同，未合并；别名「表情包」已被 dsh-nekowhale-stickers 占用，故本条别名用「表情包发图」。
    repo_confirmed: true
    gh: null
    entry_updated: '2026-11-24'
    category_label: 娱乐与彩蛋
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-meme/
  generated: true
---

DSH 的表情包插件：输入框旁一键发图，按图库/情绪筛选与搜索，AI 按聊天气氛主动斗图，内置大肥鱼图库；图库可上传入库、扫描新增、ZIP 导入导出，或从市场一键安装，也可经 dsh-im 把表情以原生图片消息发到 QQ/微信/飞书。
