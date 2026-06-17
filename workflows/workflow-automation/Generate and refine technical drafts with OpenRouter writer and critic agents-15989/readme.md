# Generate and refine technical drafts with OpenRouter writer and critic agents

https://n8nworkflows.xyz/workflows/15989

## 节点清单

| 节点 | 类型 |
|------|------|
| Webhook - Brief In | Webhook |
| Normalize Request | Code |
| Writer Agent | AI Agent |
| OpenRouter - Writer | OpenRouter Chat Model |
| Parse Writer Output | Code |
| Critic Agent | AI Agent |
| OpenRouter - Critic | OpenRouter Chat Model |
| Parse Critic Output | Code |
| Passed or Max Iterations? | IF 判断 |
| Finalize Response | Code |
| Respond to Client | 响应 Webhook |
| Increment + Stage Feedback | Code |

## 触发方式
- Webhook - Brief In 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：10
- 输出节点：1
- 分类：workflow-automation
