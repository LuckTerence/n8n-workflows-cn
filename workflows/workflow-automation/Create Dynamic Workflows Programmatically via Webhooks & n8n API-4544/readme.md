## 简介
**Create Dynamic Workflows Programmatically via Webhooks & n8n API**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4544

---

# Create Dynamic Workflows Programmatically via Webhooks & n8n API


## 节点清单

| 节点 | 类型 |
|------|------|
| Webhook | Webhook |
| Validate JSON | Code |
| Validation Successful? | IF 判断 |
| Create Workflow | HTTP Request |
| API Successful? | IF 判断 |
| Success Response | 数据设置 |
| Validation Error | 数据设置 |
| API Error | 数据设置 |

## 触发方式
- Webhook 触发

## 统计
- 节点总数：8
- 触发节点：1
- 处理节点：6
- 输出节点：1
- 分类：workflow-automation
