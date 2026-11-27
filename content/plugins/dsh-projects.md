---
title: DSH-projects（DeepSeek 生态又添神器：给 DeepSeek Harness 请一个项目经理）
description: 个人助理管理任务与项目：拆分任务、记上下文、看板验收，npm 包 deepseek-harness-projects-plugin@preview，MIT，engines.dsh >=0.2.0 <0.3.0。让人从整理上下文的杂活中解放出来，只需感知目标和完成标准。
categories:
- tool
tags: &id001
- 项目管理
- 任务拆分
- 上下文管理
- personal-assistant
weight: 1010
params:
  plugin:
    id: dsh-projects
    name: DSH-projects（DeepSeek 生态又添神器：给 DeepSeek Harness 请一个项目经理）
    aliases:
    - deepseek-harness-projects-plugin
    category: tool
    status: community
    repo: https://github.com/hovocope135-tech/DSH-projects
    install: dsh plugin --profile web add deepseek-harness-projects-plugin@preview
    summary: 个人助理管理任务与项目：拆分任务、记上下文、看板验收，npm 包 deepseek-harness-projects-plugin@preview，MIT，engines.dsh >=0.2.0 <0.3.0。让人从整理上下文的杂活中解放出来，只需感知目标和完成标准。
    features:
    - 一切围绕任务本身的属性去组织context，管理多agent是伪命题，真正需要管理的只有context
    - 最大化吸收 context，把人从整理上下文的杂活里解放出来，靠 screenpipe 等本机渠道收集信息，按项目整理上下文，不需要人工搬运
    - 任务拆分：个人助理把需求拆成项目和任务，每个任务有背景、产出、进展、完成标准
    - 看板验收：交付在「待你决定」卡片，我点头才算完成，可请求修改
    - 上下文持久化：基于 screenpipe 收集电脑活动记录、飞书消息、本地文件，按 10 分钟一段整理成时间线
    tags: *id001
    flag: npm 包 deepseek-harness-projects-plugin@preview（MIT，engines.dsh >=0.2.0 <0.3.0）；Node 24 以上；安装前建确保本机装有 Screenpipe 以获取上下文记录。首次打开需要捏助理（起名、定快捷键），此后一句目标即建项目、拆任务。文章版本 1.0.0-preview.1 对应 npm latest，preview.3 对应图中这一版。常用命令：/助理 启动、/项目 新建、/任务 拆分、/验 收、/下线 交代三件事。插件源码 github.com/hovocope135-tech/DSH-projects，装之前可自行审阅；不替你拍板、不替你验收、不以你名义发消息，飞书只读。
    notes: npm 包 latest 1.0.0-preview.1（对应图中旧界面），preview.3 对应文中所示新界面。安装需要 npm install -g @deepseek-ai/dsh，Node 24 以上和模型 API key。首次打开跟着「捏一个你的助理」选样子和性格、起名字、定呼出快捷键，默认叫 Tacit。电脑活动记录需要在「助理设置」的「活动与设备」里开启，开启后可问「用一张图展现我今天做了什么」。不替你拍板、不替你验收，也不以你名义发消息，飞书只读。插件是在你电脑上跑的第三方代码，装之前可翻翻源码，或让 AI 帮你审一遍。安装命令：dsh plugin --profile web add deepseek-harness-projects-plugin@preview；启动后在浏览器打开它给的地址。回滚用的旧版本号、发版说明里每页条数、导出上限这些数字还未写死，需要逐条确认。
    repo_confirmed: true
    gh:
      stars: 502
      forks: 12
      issues: 1
      language: JavaScript
      license: MIT
      pushed_at: '2026-11-23T09:50:32Z'
      archived: false
      slug: hovocope135-tech/DSH-projects
      stars_label: '502'
      forks_label: '12'
      pushed_date: '2026-11-23'
      stale: false
    entry_updated: '2026-11-26'
    category_label: 工具与能力
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-projects/
  generated: true
lastmod: '2026-11-26'
---

个人助理管理任务与项目：拆分任务、记上下文、看板验收，npm 包 deepseek-harness-projects-plugin@preview，MIT，engines.dsh >=0.2.0 <0.3.0。让人从整理上下文的杂活中解放出来，只需感知目标和完成标准。
