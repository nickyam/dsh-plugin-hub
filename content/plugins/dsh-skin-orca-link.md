---
title: dsh-skin-orca-link（虎鲸链路皮肤）
description: 鲸鱼娘皮肤系列的第二套：小黑鲸操作员配全直角界面与直线重绘图标，亮色白色机械舱、暗色夜间书房各含空态与工作态场景；纯展示层插件，不碰模型请求。
categories:
- fun
tags: []
weight: 1010
params:
  plugin:
    id: dsh-skin-orca-link
    name: dsh-skin-orca-link（虎鲸链路皮肤）
    aliases:
    - orca-link
    - '@smalltailqwq/dsh-client-ui-skin-orca-link'
    - 虎鲸链路
    category: fun
    status: community
    repo: https://github.com/Small-tailqwq/dsh-deep-whale/tree/main/orca-link
    install: dsh plugin --profile web add '@smalltailqwq/dsh-client-ui-skin-orca-link'
    summary: 鲸鱼娘皮肤系列的第二套：小黑鲸操作员配全直角界面与直线重绘图标，亮色白色机械舱、暗色夜间书房各含空态与工作态场景；纯展示层插件，不碰模型请求。
    features:
    - 全局直角契约：按钮/输入框/卡片/菜单/弹窗等圆角归零，状态信号与 favicon 方形化
    - 运行时把宿主 SVG 图标重绘为仅由水平垂直线、45 度折线与方块构成的直线图形，卸载即还原
    - 亮/暗各一对 16:9 场景（机械舱/夜间书房），640ms 交叉淡化，随任务状态切换
    - 侧栏顶部十状态角色（待机/同步/工作/授权/输入/审阅/完成/失败/离线/就绪）多帧动作
    - 峰谷定价红绿灯按北京时间显色，工作日高峰前 20 分钟黄灯预警，展开侧栏可看详情卡
    - 对第三方插件侧栏入口有注入格式要求（data-dsh-part 或 data-plugin-entry），形态不符的按钮会被当宿主原生控件处理
    flag: 美术资源 CC BY-NC-SA 4.0 禁止商业使用；与 dsh-web-all 自带皮肤中心的适配版不能叠装
    notes: 官方仓库 Small-tailqwq/dsh-deep-whale 的 orca-link 子目录，npm 包 @smalltailqwq/dsh-client-ui-skin-orca-link（另见 maid-atelier 与 skin-manager 条目）。README 明确：已装 @linxin666/dsh-web-all 的用户请在 dsh-web 自带皮肤中心装适配版，不能与 standalone 版同 profile 叠装。同时装多套皮肤必须装并保持 skin-manager 启用。侧栏入口注入要求详见子包 README，装了第三方插件发现入口消失时先查这一条。代码 MIT、美术 CC BY-NC-SA 4.0 禁商用。
    repo_confirmed: true
    gh:
      stars: 3127
      forks: 103
      issues: 9
      language: TypeScript
      license: NOASSERTION
      pushed_at: '2026-11-15T12:42:34Z'
      archived: false
      slug: Small-tailqwq/dsh-deep-whale
      stars_label: '3127'
      forks_label: '103'
      pushed_date: '2026-11-15'
    category_label: 娱乐与彩蛋
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-skin-orca-link/
  generated: true
---

鲸鱼娘皮肤系列的第二套：小黑鲸操作员配全直角界面与直线重绘图标，亮色白色机械舱、暗色夜间书房各含空态与工作态场景；纯展示层插件，不碰模型请求。
