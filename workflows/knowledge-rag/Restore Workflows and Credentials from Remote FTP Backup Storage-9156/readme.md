## 简介
**Restore Workflows and Credentials from Remote FTP Backup Storage**

（待补充中文描述）

> 分类：知识库 RAG | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/9156

---

# Restore Workflows and Credentials from Remote FTP Backup Storage


## 节点清单

| 节点 | 类型 |
|------|------|
| SUCCESS email Credentials | Email 发送 |
| List Credentials Folders | FTP |
| Start Restore | 手动触发 |
| List Most Recent Workflows Folder | FTP |
| Write Workflow Files To Disk | 读写文件 |
| Write Credential Files To Disk | 读写文件 |
| SUCCESS email Workflows | Email 发送 |
| ERROR: Find Most Recent Credentials Folder | 停止并报错 |
| Download Workflow Files | FTP |
| Download Credential Files | FTP |
| Filter out Credentials sub-folder | 过滤器 |
| Exclude Current Workflow From Selection | 执行命令 |
| Restore Workflows | 执行命令 |
| Restore Credentials | 执行命令 |
| Restore Credentials? | IF 判断 |
| Restore Workflows? | IF 判断 |
| Init | Code |
| Create Temp Folder | 执行命令 |
| List Credentials Files | FTP |
| Find Last Backup | Code |

## 触发方式
- Start Restore 触发

## 统计
- 节点总数：20
- 触发节点：1
- 处理节点：17
- 输出节点：2
- 分类：knowledge-rag
