# Automated Workflow & Credential Restoration System for Self-Hosted Environments

https://n8nworkflows.xyz/workflows/9154

## 节点清单

| 节点 | 类型 |
|------|------|
| Start Restore | 手动触发 |
| SUCCESS email | Email 发送 |
| List Bkp Folders | 执行命令 |
| Restore Credentials | 执行命令 |
| SUCCESS email Workflows | Email 发送 |
| Exclude Current Workflow From Selection | 执行命令 |
| Restore Workflows | 执行命令 |
| Init | Code |
| Restore Credentials? | IF 判断 |
| Restore Workflows? | IF 判断 |
| Delete TEMP Folder | 执行命令 |
| ERROR: Find Most Recent Bkp Folder | 停止并报错 |
| Find Last Backup | Code |

## 触发方式
- Start Restore 触发

## 统计
- 节点总数：13
- 触发节点：1
- 处理节点：10
- 输出节点：2
- 分类：workflow-automation
