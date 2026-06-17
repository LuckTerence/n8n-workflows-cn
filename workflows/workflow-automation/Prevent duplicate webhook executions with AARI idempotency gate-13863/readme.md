# Prevent duplicate webhook executions with AARI idempotency gate

https://n8nworkflows.xyz/workflows/13863

## 节点清单

| 节点 | 类型 |
|------|------|
| Incoming webhook event | Webhook |
| AARI idempotency gate | HTTP Request |
| Duplicate detected? | IF 判断 |
| ⛔ Stop duplicate execution | 数据设置 |
| ✅ Run your action here | 数据设置 |
| 📋 Report SUCCESS | HTTP Request |

## 触发方式
- Incoming webhook event 触发

## 统计
- 节点总数：6
- 触发节点：1
- 处理节点：3
- 输出节点：2
- 分类：workflow-automation
