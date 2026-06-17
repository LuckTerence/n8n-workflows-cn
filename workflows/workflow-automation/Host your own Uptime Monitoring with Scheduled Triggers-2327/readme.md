## 简介
**Host your own Uptime Monitoring with Scheduled Triggers**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Slack/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2327

---

# Host your own Uptime Monitoring with Scheduled Triggers


## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Trigger | 定时触发器 |
| Calculate Status | 数据设置 |
| Get Sites | Google Sheets |
| Send Chat Alert | Slack |
| Send Email Alert | Email 发送 |
| Log Uptime Event | Google Sheets |
| Update Site Status | Google Sheets |
| Perform Site Test | HTTP Request |
| For Each Site... | 分批处理 |
| Status Router | Switch 路由 |

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：10
- 触发节点：1
- 处理节点：6
- 输出节点：3
- 分类：workflow-automation
