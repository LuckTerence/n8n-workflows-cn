## 简介
**Send Aloware SMS confirmations, reminders, and no-show rebooking for appointments**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：9 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/15021

---

# Send Aloware SMS confirmations, reminders, and no-show rebooking for appointments


## 节点清单

| 节点 | 类型 |
|------|------|
| Booking System: Appointment Created | Webhook |
| Normalize Appointment Data | 数据设置 |
| Aloware: Create or Update Patient Contact | HTTP Request |
| Aloware: Send Booking Confirmation SMS | HTTP Request |
| Aloware: Enroll in Reminder Sequence | HTTP Request |
| Wait Until After Appointment | 等待 |
| Aloware: Check If Appointment Completed | HTTP Request |
| Was It a No-Show? | IF 判断 |
| Aloware: Enroll in No-Show Re-booking Sequence | HTTP Request |
| Appointment Completed — No Action | 空操作 |

## 触发方式
- Booking System: Appointment Created 触发

## 统计
- 节点总数：10
- 触发节点：1
- 处理节点：4
- 输出节点：5
- 分类：workflow-automation
