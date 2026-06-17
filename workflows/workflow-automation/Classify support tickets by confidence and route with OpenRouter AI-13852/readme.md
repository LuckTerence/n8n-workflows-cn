## 简介
**Classify support tickets by confidence and route with OpenRouter AI**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/13852

---

# Classify support tickets by confidence and route with OpenRouter AI


## 节点清单

| 节点 | 类型 |
|------|------|
| Webhook - Incoming Ticket | Webhook |
| Normalize Ticket | Code |
| AI - Classify | AI Agent |
| Parse + Validate | Code |
| Confidence Threshold | Switch 路由 |
| Route by Category | Switch 路由 |
| Flag for Review | Code |
| Send to Human Queue | Code |
| Billing Team | Code |
| Technical Team | Code |
| Sales Team | Code |
| General Inbox | Code |
| Respond | 响应 Webhook |
| OpenRouter Chat Model | OpenRouter Chat Model |

## 触发方式
- Webhook - Incoming Ticket 触发

## 统计
- 节点总数：14
- 触发节点：1
- 处理节点：12
- 输出节点：1
- 分类：workflow-automation
