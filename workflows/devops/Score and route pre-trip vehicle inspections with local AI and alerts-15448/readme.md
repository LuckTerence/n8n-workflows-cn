# Score and route pre-trip vehicle inspections with local AI and alerts

https://n8nworkflows.xyz/workflows/15448

## 节点清单

| 节点 | 类型 |
|------|------|
| HTTP Request | HTTP Request |
| Parse Input | Code |
| Score Calculator | Code |
| Flag Rules | Code |
| Ollama AI | HTTP Request |
| Parse AI Response | Code |
| Final Score | Code |
| Route by Status | Switch 路由 |
| Respond OK | 响应 Webhook |
| Respond Flagged | 响应 Webhook |
| Webhook3 | Webhook |
| Send an Email2 | Email 发送 |

## 触发方式
- Webhook3 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：6
- 输出节点：5
- 分类：devops
