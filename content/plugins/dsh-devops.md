---
title: dsh-devops
description: 把服务器运维搬进 DSH Web 侧栏：管理 SSH 服务器、监控硬件 / 进程 / 日志、定时做只读 AI 巡检，并把 Git 仓库部署到服务器，形成可复用的部署闭环。
categories:
- workflow
tags: &id001
- 运维
- SSH
- 部署
- 监控
- AI巡检
weight: 1010
params:
  plugin:
    id: dsh-devops
    name: dsh-devops
    aliases:
    - '@bigbigtooth/dsh-devops'
    - DSH-DevOps-Plugin
    - 远程运维
    category: workflow
    status: community
    repo: https://github.com/bigbigtooth/DSH-DevOps-Plugin
    install: dsh plugin --profile web add @bigbigtooth/dsh-devops
    summary: 把服务器运维搬进 DSH Web 侧栏：管理 SSH 服务器、监控硬件 / 进程 / 日志、定时做只读 AI 巡检，并把 Git 仓库部署到服务器，形成可复用的部署闭环。
    features:
    - SSH 服务器管理：添加前强制真实登录测试，首次连接核对并保存主机指纹、指纹变化即暂停；插件私有 SSH 配置与系统配置隔离，支持私钥与跳板机
    - 硬件 / 进程 / 日志监控：CPU、内存、磁盘定时采集（默认 60 秒），进程全量枚举并按项目分组，日志按「项目 → 服务 → 文件」动态发现、增量读取并去重告警
    - 只读 AI 巡检：AI 分批分析异常并给出判断依据与覆盖率，只读边界由工具权限在结构上强制；巡检在服务端常驻，关浏览器不停、宿主重启后恢复且不堆积补跑
    - Git 部署闭环：首次 AI 部署 → 步骤固化为带版本的 .sh 脚本（候选 → 已验证 → 失效，哈希防篡改）→ 后续 git pull --ff-only 一键更新，失败最多两轮 AI 修复后重试
    - 安全设计：凭据 AES-256-GCM 加密存储并统一脱敏，远程命令经白名单解析；无安装期脚本、无遥测、插件自身不持有模型 API Key
    tags: *id001
    flag: 涉及生产服务器写操作，请先在测试环境验证
    notes: 社区项目（MIT，非 DeepSeek 官方），与名称相近的 dsh-ops（T-Auto 的 token 优化工具）不是同一个插件。README 实测组合为 dsh-devops 0.5.0 / 0.4.x 配 DSH 0.1.5-rc.2；0.5.0 起改用 scoped 包名。安装三坑：保存凭据前先设 DSH_DEVOPS_KEY_FILE（不设则重启后凭据无法解密，密钥文件 0600 且丢失不可找回）、同版本重装须先 remove 再 add、装完必须重启宿主。本站直连 npm registry 查询 @bigbigtooth/dsh-devops 返回 404，npm 上只有他人预留的 dsh-devops@0.0.1 占位包；若 npm 路径装不上，改用 README 的 Release tarball（github.com/bigbigtooth/DSH-DevOps-Plugin/releases/latest/download/dsh-devops-latest.tgz）。巡检只读，部署写入仅限显式创建的任务，不读取 DSH 会话内容。
    refs:
    - id: wx-devops
      title: DeepSeek Harness这个神级插件，用完我直接跪了！
      url: https://mp.weixin.qq.com/s/gdWT1tC-ajn2HMjwJJKA4w
      kind_label: 公众号
      publisher: 运维网工（原文署名 bigbigtooth）
    source_count: 1
    repo_confirmed: true
    category_label: 协作与工作流
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-devops/
  generated: true
---

把服务器运维搬进 DSH Web 侧栏：管理 SSH 服务器、监控硬件 / 进程 / 日志、定时做只读 AI 巡检，并把 Git 仓库部署到服务器，形成可复用的部署闭环。
