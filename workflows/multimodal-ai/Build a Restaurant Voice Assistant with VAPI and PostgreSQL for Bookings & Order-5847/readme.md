# Build a Restaurant Voice Assistant with VAPI and PostgreSQL for Bookings & Orders

https://n8nworkflows.xyz/workflows/5847

## 节点清单

| 节点 | 类型 |
|------|------|
| Trigger: Voice Request (VAPI) | Webhook |
| Update Data (Table Booking / Orders) | PostgreSQL |
| Respond: Booking/Order Confirmation (VAPI) | 响应 Webhook |
| Wait For Response | 等待 |
| Wait For Response1 | 等待 |
| Trigger: Info Request (VAPI) | Webhook |
|  Get Restaurant Info (Postgres) | PostgreSQL |
| Respond: Restaurant Details (VAPI) | 响应 Webhook |

## 触发方式
- Trigger: Voice Request (VAPI) 触发
- Trigger: Info Request (VAPI) 触发

## 统计
- 节点总数：8
- 触发节点：2
- 处理节点：4
- 输出节点：2
- 分类：multimodal-ai
