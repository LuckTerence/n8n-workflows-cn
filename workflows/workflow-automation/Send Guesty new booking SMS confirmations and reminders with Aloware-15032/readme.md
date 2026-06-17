# Send Guesty new booking SMS confirmations and reminders with Aloware

https://n8nworkflows.xyz/workflows/15032

## 节点清单

| 节点 | 类型 |
|------|------|
| Guesty: New Reservation | Webhook |
| Normalize Reservation Data | 数据设置 |
| Aloware: Create Guest Contact | HTTP Request |
| Aloware: Send Booking Confirmation SMS | HTTP Request |
| Aloware: Enroll in Check-in Reminder Sequence | HTTP Request |
| Wait Until After Checkout | 等待 |
| Aloware: Enroll in Post-Stay Review Sequence | HTTP Request |

## 触发方式
- Guesty: New Reservation 触发

## 统计
- 节点总数：7
- 触发节点：1
- 处理节点：2
- 输出节点：4
- 分类：workflow-automation
