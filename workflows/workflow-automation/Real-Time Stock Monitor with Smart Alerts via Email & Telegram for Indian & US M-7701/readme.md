# Real-Time Stock Monitor with Smart Alerts via Email & Telegram for Indian & US Markets

https://n8nworkflows.xyz/workflows/7701

## 节点清单

| 节点 | 类型 |
|------|------|
| Market Hours Trigger | 定时触发器 |
| Read Stock Watchlist | Google Sheets |
| Parse Watchlist Data | Code |
| Fetch Live Stock Price | HTTP Request |
| Smart Alert Logic | Code |
| Check Alert Conditions | IF 判断 |
| Send Email Alert | Email 发送 |
| Send Telegram Alert | Telegram |
| Update Alert History | Google Sheets |
| Alert Status Check | IF 判断 |
| Success Notification | Email 发送 |
| Error Notification | Email 发送 |

## 触发方式
- Market Hours Trigger 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：6
- 输出节点：5
- 分类：workflow-automation
