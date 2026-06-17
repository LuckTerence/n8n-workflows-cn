## 简介
**Build a full REST-API with n8n webhooks**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/12789

---

# Build a full REST-API with n8n webhooks


## 节点清单

| 节点 | 类型 |
|------|------|
| -> POST | 数据设置 |
| -> GET | 数据设置 |
| -> PUT | 数据设置 |
| -> DELETE | 数据设置 |
| v1/seg1 | Webhook |
| v1/seg2 | Webhook |
| v1/seg3 | Webhook |
| _CFG | Code |
| _REQUEST | 数据设置 |
| Respond to Webhook1 | 响应 Webhook |
| Invalid Route | 响应 Webhook |
| Clear JSON | 数据设置 |
| Invalid Route1 | 响应 Webhook |
| Invalid Route2 | 响应 Webhook |
| Invalid Route3 | 响应 Webhook |
| Respond to Webhook | 响应 Webhook |
| Routing | 空操作 |
| Check baz status | 空操作 |
| Create new baz | 空操作 |
| Implementation | 执行工作流 |
| Implementation1 | 执行工作流 |
| Merge | 数据合并 |
| /foo | Switch 路由 |
| api root | Switch 路由 |
| /foo/bar/baz | 空操作 |
| /foo/bar | Switch 路由 |
| /foo/qux | Switch 路由 |
| baz METHOD | Switch 路由 |
| regular Set node | 数据设置 |
| non-passthrough node | 执行工作流 |
| data via $json | 数据设置 |
| Named node | 数据设置 |
| non-passthrough node1 | 执行工作流 |
| data via $('NODE') | 数据设置 |
| example: default $json-based | 空操作 |
| example: $('NODE') based | 空操作 |
| example: check for execution | 空操作 |
| run examples | 手动触发 |
| optional path | 数据设置 |
| 50:50 randomizer | IF 判断 |
| non-passthrough node2 | 执行工作流 |
| data with fallback | 数据设置 |
| API entry point | 空操作 |

## 触发方式
- v1/seg1 触发
- v1/seg2 触发
- v1/seg3 触发
- run examples 触发

## 统计
- 节点总数：43
- 触发节点：4
- 处理节点：33
- 输出节点：6
- 分类：devops
