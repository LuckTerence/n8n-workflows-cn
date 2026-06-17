# Send Telegram notifications for new Feedspace testimonials

https://n8nworkflows.xyz/workflows/12152

## 节点清单

| 节点 | 类型 |
|------|------|
| Receive Feedspace Webhook | Webhook |
| Send Telegram Notification | Telegram |
| Has Error? | IF 判断 |
| Success Response | 响应 Webhook |
| Format Error Details | Code |
| Error Response | 响应 Webhook |

## 触发方式
- Receive Feedspace Webhook 触发

## 统计
- 节点总数：6
- 触发节点：1
- 处理节点：2
- 输出节点：3
- 分类：workflow-automation
