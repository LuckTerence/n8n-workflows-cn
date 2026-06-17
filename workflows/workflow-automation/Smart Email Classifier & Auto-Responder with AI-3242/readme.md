# Smart Email Classifier & Auto-Responder with AI

https://n8nworkflows.xyz/workflows/3242

## 节点清单

| 节点 | 类型 |
|------|------|
| Sentiment Analysis | sentimentAnalysis |
| Azure OpenAI Chat Model | Azure OpenAI Chat Model |
| Spam | Email 发送 |
| Gmail | Email 发送 |
| Important | Email 发送 |
| Promotion | Email 发送 |
| Notification | Email 发送 |
| Personal | Email 发送 |
| Call request | Email 发送 |
| Needs Reply | Email 发送 |
| important? | sentimentAnalysis |
| Draft Reply | AI Agent |
| $INPUTS$ | 数据设置 |
| Draft | Gmail 工具 |
| Get emails | Gmail 工具 |
| needs reply? | sentimentAnalysis |
| No Operation, do nothing | 空操作 |
| Telegram | Telegram |
| Google Calendar | Google Calendar 工具 |
| Gmail Trigger | Gmail 触发器 |
| json schema | 结构化输出解析器 |
| Write draft | Email 发送 |

## 触发方式
- Gmail Trigger 触发

## 统计
- 节点总数：22
- 触发节点：1
- 处理节点：11
- 输出节点：10
- 分类：workflow-automation
