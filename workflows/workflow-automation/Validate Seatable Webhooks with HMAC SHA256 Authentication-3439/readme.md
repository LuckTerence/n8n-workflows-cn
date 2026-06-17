# Validate Seatable Webhooks with HMAC SHA256 Authentication

https://n8nworkflows.xyz/workflows/3439

## 节点清单

| 节点 | 类型 |
|------|------|
| 200 | 响应 Webhook |
| 403 | 响应 Webhook |
| Calculate sha256 | 加密 |
| Seatable Webhook | Webhook |
| Add nodes for processing | 空操作 |
| hash matches | IF 判断 |

## 触发方式
- Seatable Webhook 触发

## 统计
- 节点总数：6
- 触发节点：1
- 处理节点：3
- 输出节点：2
- 分类：workflow-automation
