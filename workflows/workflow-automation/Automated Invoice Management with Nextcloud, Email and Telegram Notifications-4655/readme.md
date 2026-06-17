# Automated Invoice Management with Nextcloud, Email and Telegram Notifications

https://n8nworkflows.xyz/workflows/4655

## 节点清单

| 节点 | 类型 |
|------|------|
| Start | 定时触发器 |
| List Incoming Invoices | NextCloud |
| File Exists? | IF 判断 |
| Download Invoice | NextCloud |
| Send Email | Email 发送 |
| Archive File | NextCloud |
| Notify Telegram | Telegram |
| Set Parameters | 数据设置 |

## 触发方式
- Start 触发

## 统计
- 节点总数：8
- 触发节点：1
- 处理节点：5
- 输出节点：2
- 分类：workflow-automation
