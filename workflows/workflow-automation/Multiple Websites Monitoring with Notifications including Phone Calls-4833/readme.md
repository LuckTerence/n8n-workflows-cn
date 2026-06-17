## 简介
**Multiple Websites Monitoring with Notifications including Phone Calls**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A-adapted（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4833

---

# Multiple Websites Monitoring with Notifications including Phone Calls


## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Trigger | 定时触发器 |
| Loop Over Items | 分批处理 |
| Check website status | HTTP Request |
| Website URLs | Google Sheets |
| Get Active Down Record | Google Sheets |
| Update Uptime and Total Downtime | Google Sheets |
| Find Existing Record | Code |
| Add Downtime Record | Google Sheets |
| Notify over Phone Call | HTTP Request |
| Check Downtime Exists | IF 判断 |
| Email Notification for Down | Email 发送 |
| Slack Notification for Down | Slack |
| Telegram Notification for Down | Telegram |
| Email Notification for Up | Email 发送 |
| Slack Notification for Up | Slack |
| Telegram Notification for Up | Telegram |
| If Down Record Exist | IF 判断 |
| If Site Up | IF 判断 |
| Get Existing Down Records | Google Sheets |

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：19
- 触发节点：1
- 处理节点：10
- 输出节点：8
- 分类：workflow-automation
