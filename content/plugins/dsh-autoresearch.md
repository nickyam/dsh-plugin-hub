---
title: dsh-autoresearch（自动实验循环）
description: 给 DSH 加一个持久化的自动研究/实验循环：创建一个目标后 Agent 连续修改、测量、保留或回滚，会话顶部面板显示结果；开工前先建本地保护，能用 Git 就存基线、否则打私有快照，翻车自动恢复受保护文件。
categories:
- workflow
tags: &id001
- 自动研究
- 实验循环
- 自动化
- workflow
weight: 1010
params:
  plugin:
    id: dsh-autoresearch
    name: dsh-autoresearch（自动实验循环）
    aliases:
    - 自动研究
    - dsh-reprise
    category: workflow
    status: community
    repo: https://github.com/aa2246740/dsh-autoresearch
    install: dsh plugin --profile web add github:aa2246740/dsh-autoresearch#v1.0.11
    summary: 给 DSH 加一个持久化的自动研究/实验循环：创建一个目标后 Agent 连续修改、测量、保留或回滚，会话顶部面板显示结果；开工前先建本地保护，能用 Git 就存基线、否则打私有快照，翻车自动恢复受保护文件。
    features:
    - 自动实验循环：创建目标后连续改→测→留/回滚，结果在会话顶部面板可见
    - 本地保护：开工先建基线（Git 或私有快照），翻车自动恢复受保护文件
    - '版本明确：README 标正式版 1.0.11、适配 DSH 0.2.1-rc.5，安装命令带 #v1.0.11 标签'
    tags: *id001
    flag: 社区项目；会在工作目录反复修改文件，务必在独立目录/有基线保护下使用；安装按 README 固定 v1.0.11 标签
    notes: 仓库 aa2246740/dsh-autoresearch（README 标正式版 1.0.11、适配 DSH 0.2.1-rc.5，安装给 github:aa2246740/dsh-autoresearch#v1.0.11）。GitHub 另有 beibingyangliuying、vlozg 等多个 0 星同名 dsh-autoresearch，本条取 README 有正式版本号、安装说明完整的 aa2246740 主仓。文章描述「设定轮次连续改、测量、保留或回滚、开工建本地保护」与 README 一致。
    repo_confirmed: true
    gh:
      stars: 0
      forks: 0
      issues: 0
      language: TypeScript
      license: MIT
      pushed_at: '2026-11-25T07:51:45Z'
      archived: false
      slug: aa2246740/dsh-autoresearch
      stars_label: '0'
      forks_label: '0'
      pushed_date: '2026-11-25'
      updated_label: 昨天有提交
      updated_days: 1
      stale: false
    entry_updated: '2026-11-17'
    category_label: 协作与工作流
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-autoresearch/
  generated: true
lastmod: '2026-11-17'
---

给 DSH 加一个持久化的自动研究/实验循环：创建一个目标后 Agent 连续修改、测量、保留或回滚，会话顶部面板显示结果；开工前先建本地保护，能用 Git 就存基线、否则打私有快照，翻车自动恢复受保护文件。
