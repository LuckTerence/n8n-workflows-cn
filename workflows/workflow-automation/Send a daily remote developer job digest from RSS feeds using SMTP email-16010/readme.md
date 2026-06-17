## 简介
**Send a daily remote developer job digest from RSS feeds using SMTP email**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/16010

---

# Send a daily remote developer job digest from RSS feeds using SMTP email


## 节点清单

| 节点 | 类型 |
|------|------|
| Every Day at 8 AM | 定时触发器 |
| Config | 数据设置 |
| Expand Board URLs | Code |
| Split Job Boards | 分批处理 |
| RSS Read | RSS Feed |
| Log Fetch Error | Code |
| Normalize Jobs | Code |
| Filter by Keyword & Recency | Code |
| Deduplicate Jobs | Code |
| Collect All New Jobs | 数据聚合 |
| Any New Jobs? | IF 判断 |
| Build Email HTML | Code |
| Send Digest Email | Email 发送 |
| No New Jobs — Skip | 数据设置 |

## 触发方式
- Every Day at 8 AM 触发
- RSS Read 触发

## 统计
- 节点总数：14
- 触发节点：2
- 处理节点：11
- 输出节点：1
- 分类：workflow-automation
