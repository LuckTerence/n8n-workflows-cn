## 简介
**Export Odoo Company Data via API Endpoint with JSON-Excel Output Options**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：8 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/9653

---

# Export Odoo Company Data via API Endpoint with JSON-Excel Output Options


## 节点清单

| 节点 | 类型 |
|------|------|
| Receive Company Request | Webhook |
| Prepare Dynamic Filter | Function |
| Fetch Companies from Odoo | odoo |
| Prepare Output Data | Function |
| Check If Excel Required | IF 判断 |
| Convert to Excel | 转换为文件 |
| Respond with File | 响应 Webhook |
| Respond with JSON | 响应 Webhook |
| Code | Code |

## 触发方式
- Receive Company Request 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：6
- 输出节点：2
- 分类：devops
