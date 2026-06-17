# Health Monitoring System with Grok-3 AI Analysis and Family-Doctor Email Alerts

https://n8nworkflows.xyz/workflows/10525

## 节点清单

| 节点 | 类型 |
|------|------|
| Webhook - Submit Health Data | Webhook |
| Extract Health Data | 数据设置 |
| AI Health Analysis Agent | AI Agent |
| Structured Output Parser | 结构化输出解析器 |
| Check If Alert Needed | IF 判断 |
| Prepare Alert Data | 数据设置 |
| Send Email to Family | Email 发送 |
| Check If Doctor Alert Needed | IF 判断 |
| Send Email to Doctor | Email 发送 |
| Merge Alert Results | 数据设置 |
| No Alert Required | 数据设置 |
| Combine Results | 数据合并 |
| Respond to Webhook | 响应 Webhook |
| OpenRouter Chat Model | OpenRouter Chat Model |

## 触发方式
- Webhook - Submit Health Data 触发

## 统计
- 节点总数：14
- 触发节点：1
- 处理节点：10
- 输出节点：3
- 分类：workflow-automation
