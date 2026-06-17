# Extract and self-correct meeting action items with OpenRouter and webhooks

https://n8nworkflows.xyz/workflows/15995

## 节点清单

| 节点 | 类型 |
|------|------|
| Webhook - Meeting Notes | Webhook |
| Normalize Request | Code |
| Extraction Agent | AI Agent |
| Window Buffer Memory | 记忆缓冲区 |
| Parse + Validate | Code |
| Validated or Max Attempts? | IF 判断 |
| Finalize Response | Code |
| Respond to Client | 响应 Webhook |
| Increment + Feedback | Code |
| OpenRouter Chat Model | OpenRouter Chat Model |

## 触发方式
- Webhook - Meeting Notes 触发

## 统计
- 节点总数：10
- 触发节点：1
- 处理节点：8
- 输出节点：1
- 分类：workflow-automation
