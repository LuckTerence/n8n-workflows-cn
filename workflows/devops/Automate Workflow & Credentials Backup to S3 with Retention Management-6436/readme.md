## 简介
**Automate Workflow & Credentials Backup to S3 with Retention Management**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/6436

---

# Automate Workflow & Credentials Backup to S3 with Retention Management


## 节点清单

| 节点 | 类型 |
|------|------|
| Get many workflows | n8n |
| Config | 数据设置 |
| Extract Date | 数据设置 |
| Keep Outdated Backups | 过滤器 |
| Delete Outdated Backups | S3 |
| Export Credentials | 执行命令 |
| Load Credentials | 读写文件 |
| Delete Temporary File | 执行命令 |
| Store Credentials Backup | S3 |
| Store Workflow Backup | S3 |
| Daily Backup | 定时触发器 |
| Get Existing Backups | S3 |



## 功能说明

自动备份系统，定时备份数据或配置，定时执行。

定时触发，通过 工作流编排 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

无需额外 API Key，导入即可运行。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：12
- 触发方式：定时触发

## 触发方式
- Daily Backup 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：11
- 输出节点：0
- 分类：devops
