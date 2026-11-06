---
title: dsh-minigames
description: DSH Web UI 浮动小游戏窗口：等待模型回复或修 bug 时的摸鱼神器；折叠态留下可拖动浮动 🎮 按钮，展开态为可拖拽吸附的面板，内置多款离线小游戏。
categories:
- fun
tags: &id001
- 游戏
- 摸鱼
weight: 1010
params:
  plugin:
    id: dsh-minigames
    name: dsh-minigames
    category: fun
    status: community
    repo: https://github.com/lhh010/dsh-minigames
    install: dsh plugin --profile web add '@dsh-external/dsh-minigames@github:lhh010/dsh-minigames#v0.3.27'
    summary: DSH Web UI 浮动小游戏窗口：等待模型回复或修 bug 时的摸鱼神器；折叠态留下可拖动浮动 🎮 按钮，展开态为可拖拽吸附的面板，内置多款离线小游戏。
    features:
    - 折叠/展开窗口：隐藏后留可拖动浮动 🎮 按钮，展开为可拖拽、自动吸附、持久化位置的游戏面板
    - 18 款全离线小游戏（Canvas 绘制、零资源文件）：恐龙跳一跳、俄罗斯方块、坦克大战(带AI)、消消乐、华容道、贪吃蛇、2048、扫雷、记忆翻牌、五子棋vs AI、跳一跳、打砖块、打地鼠、黑白棋vs AI、Flappy、数独、吃豆人、跟枪练习
    - 预留游戏注册表（registerGame），新增游戏只需实现一个接口
    - 体验细节：隐藏/切标签页自动暂停、每局最高分存 localStorage、键盘输入仅在点击游戏区后生效（不劫持聊天框）
    - 尺寸自适应：画布按面板可用空间重排，宽高上限 960px
    tags: *id001
    flag: 社区项目，非官方；注意 DSH 版本→插件版本对应关系，装错会崩（如 useConversation is not a function）
    notes: README 提示：DSH 版本决定装哪个插件版本（0.1.2-alpha.1 ~ 0.2.1-alpha.1 用新版）；pnpm 11 可能拦截 node-pty 构建脚本，需在 ~/.dsh/profiles/web 下 pnpm approve-builds --all 后重装，并硬刷新浏览器。
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
    url: /plugins/dsh-minigames/
  generated: true
---

DSH Web UI 浮动小游戏窗口：等待模型回复或修 bug 时的摸鱼神器；折叠态留下可拖动浮动 🎮 按钮，展开态为可拖拽吸附的面板，内置多款离线小游戏。
