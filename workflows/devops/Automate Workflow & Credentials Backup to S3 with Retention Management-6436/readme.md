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

## 触发方式
- Daily Backup 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：11
- 输出节点：0
- 分类：devops
