# Automated Zalo OA Token Management with OAuth and Webhook Integration

https://n8nworkflows.xyz/workflows/8675

## 节点清单

| 节点 | 类型 |
|------|------|
| Store to SD & Pass token | Code |
| Refresh Token (Zalo v4) | HTTP Request |
| Schedule Trigger | 定时触发器 |
| Execute_Node | Webhook |
| Clean Zalo Static Data | Code |
| Set Refresh Token and App ID | 数据设置 |
| Load to Static Data | Code |
| Webhook | Webhook |
| Load Access Token | Code |

## 触发方式
- Schedule Trigger 触发
- Execute_Node 触发
- Webhook 触发

## 统计
- 节点总数：9
- 触发节点：3
- 处理节点：5
- 输出节点：1
- 分类：workflow-automation
