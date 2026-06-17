# Protect public webhooks with Ainoflow Guard rate limiting

https://n8nworkflows.xyz/workflows/13491

## 节点清单

| 节点 | 类型 |
|------|------|
| Webhook | Webhook |
| Config | 数据设置 |
| BuildIdentity | Code |
| GuardCheck | HTTP Request |
| IfAllowed | IF 判断 |
| BusinessLogic | Code |
| RespondOk | 响应 Webhook |
| BuildDeniedResponse | 数据设置 |
| RespondRateLimited | 响应 Webhook |

## 触发方式
- Webhook 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：5
- 输出节点：3
- 分类：devops
