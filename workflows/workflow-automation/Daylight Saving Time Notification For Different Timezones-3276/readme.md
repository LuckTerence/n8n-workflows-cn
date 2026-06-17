# Daylight Saving Time Notification For Different Timezones

https://n8nworkflows.xyz/workflows/3276

## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Test workflow’ | 手动触发 |
| Timezones List | Code |
| Calculate Zone Date and Time | 数据设置 |
| Check If Daylight Saving Time | 数据设置 |
| Check If Change Tomorrow | IF 判断 |
| Send Notification On Upcoming Change | Slack |
| Calculate Tomorrow's Date | 日期时间 |
| Schedule Trigger | 定时触发器 |
| Send Email On Upcoming Change | Email 发送 |

## 触发方式
- When clicking ‘Test workflow’ 触发
- Schedule Trigger 触发

## 统计
- 节点总数：9
- 触发节点：2
- 处理节点：5
- 输出节点：2
- 分类：workflow-automation
