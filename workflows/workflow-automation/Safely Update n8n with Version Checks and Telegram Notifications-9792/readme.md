# Safely Update n8n with Version Checks and Telegram Notifications

https://n8nworkflows.xyz/workflows/9792

## 节点清单

| 节点 | 类型 |
|------|------|
| Get Current Version | 执行命令 |
| Get Latest Version | HTTP Request |
| Compare Versions | Code |
| Merge Versions | 数据合并 |
| If Update Available? | IF 判断 |
| Get Executions | n8n |
| Check Running Workflows | Function |
| If Can Update? | IF 判断 |
| Notify Update Start | Telegram |
| Notify Latest Version | Telegram |
| Notify Update Available | Telegram |
| Execute Update | 执行命令 |
| Daily Trigger | 定时触发器 |
| n8n Startup Trigger | n8nTrigger |
| Wait | 等待 |

## 触发方式
- Daily Trigger 触发
- n8n Startup Trigger 触发

## 统计
- 节点总数：15
- 触发节点：2
- 处理节点：9
- 输出节点：4
- 分类：workflow-automation
