# Route CRM new leads to Aloware for instant SMS and AI qualification calls

https://n8nworkflows.xyz/workflows/15018

## 节点清单

| 节点 | 类型 |
|------|------|
| CRM: New Lead Received | Webhook |
| Normalize Lead Data | 数据设置 |
| Aloware: Create or Update Contact | HTTP Request |
| Aloware: Send Instant Lead SMS | HTTP Request |
| Is Hot Lead? | IF 判断 |
| Aloware: Enroll in AI Qualification Sequence | HTTP Request |
| Aloware: Enroll in Nurture Sequence | HTTP Request |

## 触发方式
- CRM: New Lead Received 触发

## 统计
- 节点总数：7
- 触发节点：1
- 处理节点：2
- 输出节点：4
- 分类：workflow-automation
