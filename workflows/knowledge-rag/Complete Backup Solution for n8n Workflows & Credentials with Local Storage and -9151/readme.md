## 简介
**Complete Backup Solution for n8n Workflows & Credentials with Local Storage and FTP**

（待补充中文描述）

> 分类：知识库 RAG | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：22 | 难度：⭐⭐⭐ 高级
> 原始来源：https://n8nworkflows.xyz/workflows/9151

---

# Complete Backup Solution for n8n Workflows & Credentials with Local Storage and FTP


## 节点清单

| 节点 | 类型 |
|------|------|
| Backup Summary | Code |
| Write Backup Log | 读写文件 |
| Send email | Email 发送 |
| Write Email Log | 读写文件 |
| Create Date Folder | 执行命令 |
| Init | Code |
| Daily Backup | 定时触发器 |
| Convert to File | 转换为文件 |
| Fetch Workflows | n8n |
| Clean Filename | Code |
| Write Each Workflow To Disk | 读写文件 |
| ERROR: Backup Summary | 停止并报错 |
| ERROR: Clean Filename | 停止并报错 |
| Read/Write Files from Disk | 读写文件 |
| List Credential Files | 执行命令 |
| Output Credential Items | Code |
| Aggregate | 数据聚合 |
| Merge | 数据合并 |
| Upload Credentials To FTP | FTP |
| FTP Logger (credentials) | Code |
| FTP Logger (workflows) | Code |
| Export Credentials | 执行命令 |
| Upload Workflows To FTP | FTP |

## 触发方式
- Daily Backup 触发

## 统计
- 节点总数：23
- 触发节点：1
- 处理节点：21
- 输出节点：1
- 分类：knowledge-rag
