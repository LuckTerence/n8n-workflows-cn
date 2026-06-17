## 简介
**Generate n8n Workflow Inventory Reports with JSON & Excel Export Options**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：10 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/10852

---

# Generate n8n Workflow Inventory Reports with JSON & Excel Export Options


## 节点清单

| 节点 | 类型 |
|------|------|
| Receive Request | Webhook |
| Parse Query Params | Code |
| Fetch All Workflows | n8n |
| Filter by Status | Code |
| Extract Workflow Metadata | Code |
| Switch Output Type | Switch 路由 |
| Return JSON Response | Code |
| Respond to Webhook1 | 响应 Webhook |
| Return JSON Response1 | Code |
| Respond to Webhook2 | 响应 Webhook |
| Convert to File | 转换为文件 |

## 触发方式
- Receive Request 触发

## 统计
- 节点总数：11
- 触发节点：1
- 处理节点：8
- 输出节点：2
- 分类：workflow-automation
