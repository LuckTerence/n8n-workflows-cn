## 简介
**Send automated payment reminders for Xero invoices via Outlook email**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：6 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/12648

---

# Send automated payment reminders for Xero invoices via Outlook email


## 节点清单

| 节点 | 类型 |
|------|------|
| Daily Invoice Check Trigger | 定时触发器 |
| Fetch All Xero Invoices | xero |
| Filter Out Paid Invoices | IF 判断 |
| Filter Invoices Due Soon | IF 判断 |
| Calculate Days Until Due | Code |
| Log Reminder in Xero History | HTTP Request |
| Send a message1 | Outlook |

## 触发方式
- Daily Invoice Check Trigger 触发

## 统计
- 节点总数：7
- 触发节点：1
- 处理节点：4
- 输出节点：2
- 分类：workflow-automation
