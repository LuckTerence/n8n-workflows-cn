## 简介
**Automatic Email Unsubscribe Handler: Outlook to BigQuery Integration**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：11 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/6333

---

# Automatic Email Unsubscribe Handler: Outlook to BigQuery Integration


## 节点清单

| 节点 | 类型 |
|------|------|
| Loop Over Items1 | 分批处理 |
| Summarize | 文本摘要 |
| Edit Fields | 数据设置 |
| Edit Fields1 | 数据设置 |
| Run Ever 4 Hours | 定时触发器 |
| Query Bigquery for all Unsubscribes | Google BigQuery |
| Today & 7 Days Ago | Code |
| Get Emails in Past 7 Days | Outlook |
| Filter for Unsubscribes | 过滤器 |
| Keep Only New Unsubs | 数据合并 |
| Aggregate to email level | 文本摘要 |
| Add unsubscribes to Table | Google BigQuery |

## 触发方式
- Run Ever 4 Hours 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：10
- 输出节点：1
- 分类：workflow-automation
