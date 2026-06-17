## 简介
**Route customer support requests to AI specialists with OpenRouter**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/15949

---

# Route customer support requests to AI specialists with OpenRouter


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
