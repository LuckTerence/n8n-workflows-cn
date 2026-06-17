# Route customer support requests to AI specialists with OpenRouter

https://n8nworkflows.xyz/workflows/15949

## 节点清单

| 节点 | 类型 |
|------|------|
| Webhook - Customer Request | Webhook |
| Normalize Request | Code |
| Orchestrator Agent | AI Agent |
| Billing_Specialist | agentTool |
| Technical_Specialist | agentTool |
| Account_Specialist | agentTool |
| Parse Final Response | Code |
| Orchestrator Succeeded? | IF 判断 |
| Escalate to Human | Code |
| Respond to Customer | 响应 Webhook |
| OpenRouter Chat Model | OpenRouter Chat Model |
| OpenRouter Chat Model1 | OpenRouter Chat Model |
| OpenRouter Chat Model2 | OpenRouter Chat Model |
| OpenRouter Chat Model3 | OpenRouter Chat Model |

## 触发方式
- Webhook - Customer Request 触发

## 统计
- 节点总数：14
- 触发节点：1
- 处理节点：12
- 输出节点：1
- 分类：workflow-automation
