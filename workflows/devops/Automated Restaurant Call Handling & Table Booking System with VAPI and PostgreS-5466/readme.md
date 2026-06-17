# Automated Restaurant Call Handling & Table Booking System with VAPI and PostgreSQL

https://n8nworkflows.xyz/workflows/5466

## 节点清单

| 节点 | 类型 |
|------|------|
| Query Table Availability (Postgres) | PostgreSQL |
| Respond: Availability Status (VAPI) | 响应 Webhook |
| Trigger: Booking Request (VAPI)	 | Webhook |
| Upsert Booking in Postgres	 | PostgreSQL |
| Respond: Booking Confirmation (VAPI)	 | 响应 Webhook |
| Trigger: Booking Request (VAPI)	1 | Webhook |

## 触发方式
- Trigger: Booking Request (VAPI)	 触发
- Trigger: Booking Request (VAPI)	1 触发

## 统计
- 节点总数：6
- 触发节点：2
- 处理节点：2
- 输出节点：2
- 分类：devops
