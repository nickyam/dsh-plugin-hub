---
title: DSH Skills Manager
description: 把散落在本机与项目里的 Agent 技能收拢到 DSH 统一管理：全局 / 项目 / 发现 / 回收站四视图，跨 20 多种工具与 CLI 环境读取，并从技能市场与公开仓库浏览、订阅、增量更新与备份回退。
categories:
- tool
tags: &id001
- 技能管理
- 多Agent
- 技能市场
weight: 1030
params:
  plugin:
    id: dsh-skills-manager
    name: DSH Skills Manager
    aliases:
    - '@michengai/dsh-skills-manager'
    - 技能管理器
    category: tool
    status: community
    repo: https://github.com/MichengAI/dsh-skills-manager
    install: dsh plugin --profile web add @michengai/dsh-skills-manager@latest --registry=https://registry.npmjs.org/
    summary: 把散落在本机与项目里的 Agent 技能收拢到 DSH 统一管理：全局 / 项目 / 发现 / 回收站四视图，跨 20 多种工具与 CLI 环境读取，并从技能市场与公开仓库浏览、订阅、增量更新与备份回退。
    features:
    - 四视图集中管理：全局技能、项目技能、发现、回收站，支持搜索、状态筛选与来源折叠
    - 广泛生态兼容：覆盖 DSH、公共 Agent、Codex、Claude Code、Copilot、Cursor、Antigravity、Windsurf、Qoder、Trae 等 20+ 工具与 CLI，统一读取且不改动第三方文件
    - 公共市场与仓库订阅：内置发现中心接 ClawHub 热门榜与 skills.sh 技能市场，支持公开 GitHub 仓库订阅、增量更新检测与版本备份回退
    - 分类与拖拽归类：按来源建分类文件夹、拖拽卡片归类排序、分类级一键启停，分类元数据独立保存不动物理文件
    - 回收站与防误删：删除优先移入回收站，完整保留安装身份与更新历史以便安全恢复
    - 成本与体验：技能简介近似 Token 徽标与常驻系统提示词 Token 汇总，760px 宽屏详情弹窗与一键复制 Markdown 正文
    tags: *id001
    flag: 社区项目（Apache-2.0，非 DeepSeek 官方）
    notes: 仓库 MichengAI/dsh-skills-manager（master 分支），npm 包 @michengai/dsh-skills-manager，README 版本 1.4.11（文章写 1.2.26，以仓库为准）。兼容 DSH 0.2.x 全系列（>=0.2.0-rc.1 <0.3.0-0）；仍用 0.1.x 的须改装 1.1.23，不要装 @latest。装后在「设置 → 技能」使用，需重启 DSH 并刷新页面。支持带路径前缀的反向代理部署（API 按 document.baseURI 相对解析）。与 dsh-client-ui-skill-explorer 功能有重叠，一般装一个即可。
    refs:
    - id: wx-shuzishanshui
      title: DSH 十大插件大洗牌：桌宠掉队，billion-context 月下载破百万
      url: https://mp.weixin.qq.com/s/ymm_FIwOinNF1mRcmts53g
      kind_label: 公众号
      publisher: 数字山水间（公众号：码途山海）
    - id: wx-top10-30d
      title: DSH 近 30 天插件 TOP10，鲸鱼娘挂件霸榜第一
      url: https://mp.weixin.qq.com/s/7C46btfXy97CahMiDuOEnQ
      kind_label: 公众号
      publisher: 小白分享1234（公众号）
    - id: wx-shixiang
      title: 亲测，DSH 最应该装的 10 个插件
      url: https://mp.weixin.qq.com/s/DXkOWSmgT6k3Ypsukl5GJA
      kind_label: 公众号
      publisher: 世相智能体（公众号：世相Ai智能体）
    source_count: 3
    repo_confirmed: true
    category_label: 工具与能力
    status_label: 社区
    weight: 1030
    url: /plugins/dsh-skills-manager/
  generated: true
---

把散落在本机与项目里的 Agent 技能收拢到 DSH 统一管理：全局 / 项目 / 发现 / 回收站四视图，跨 20 多种工具与 CLI 环境读取，并从技能市场与公开仓库浏览、订阅、增量更新与备份回退。
