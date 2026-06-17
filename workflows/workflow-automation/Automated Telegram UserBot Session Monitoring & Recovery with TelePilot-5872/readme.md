# Automated Telegram UserBot Session Monitoring & Recovery with TelePilot

https://n8nworkflows.xyz/workflows/5872

## 节点清单

| 节点 | 类型 |
|------|------|
| When chat message received | Chat 触发器 |
| Schedule Trigger | 定时触发器 |
| Stop auth | telePilot |
| Start auth | telePilot |
| Manual control | telePilot |
| Automatic control | telePilot |
| Get Session Status | 数据设置 |
| Stop Session | 数据设置 |
| Start Session | 数据设置 |
| Pass on Closed Status | 过滤器 |
| Send Closed Status message | Telegram |
| Check Session Connection | 过滤器 |
| Send Session Connection message | Telegram |

## 触发方式
- When chat message received 触发
- Schedule Trigger 触发

## 统计
- 节点总数：13
- 触发节点：2
- 处理节点：9
- 输出节点：2
- 分类：workflow-automation
