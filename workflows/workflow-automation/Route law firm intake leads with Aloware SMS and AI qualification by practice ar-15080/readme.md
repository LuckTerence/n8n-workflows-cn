# Route law firm intake leads with Aloware SMS and AI qualification by practice area

https://n8nworkflows.xyz/workflows/15080

## 节点清单

| 节点 | 类型 |
|------|------|
| Law Firm: New Client Inquiry | Webhook |
| Normalize Inquiry Data | 数据设置 |
| Aloware: Create Client Contact | HTTP Request |
| Aloware: Send Intake SMS | HTTP Request |
| Is High-Intent Practice Area? | IF 判断 |
| Aloware: Enroll in AI Intake Sequence | HTTP Request |
| Aloware: Enroll in Consultation Scheduling Sequence | HTTP Request |

## 触发方式
- Law Firm: New Client Inquiry 触发

## 统计
- 节点总数：7
- 触发节点：1
- 处理节点：2
- 输出节点：4
- 分类：workflow-automation
