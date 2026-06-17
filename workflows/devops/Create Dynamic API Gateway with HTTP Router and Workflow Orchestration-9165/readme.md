## 简介
**Create Dynamic API Gateway with HTTP Router and Workflow Orchestration**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/9165

---

# Create Dynamic API Gateway with HTTP Router and Workflow Orchestration


## 节点清单

| 节点 | 类型 |
|------|------|
| HEAD | 数据设置 |
| Execute Workflow | 执行工作流 |
| Success | 响应 Webhook |
| Aggregate Method Branches | 数据设置 |
| PUT | 数据设置 |
| PATCH | 数据设置 |
| DELETE | 数据设置 |
| POST | 数据设置 |
| GET | 数据设置 |
| Routes Config | 数据设置 |
| Query param exists? | IF 判断 |
| Universal Receiver | Webhook |
| [Error] Required query param missing | 响应 Webhook |
| Resolve | Code |
| Route is OK? | IF 判断 |
| Status = 405? | IF 判断 |
| [Error] Method Not Allowed | 响应 Webhook |
| Error - Not OK | 响应 Webhook |
| Error - Subflow | 响应 Webhook |

## 触发方式
- Universal Receiver 触发

## 统计
- 节点总数：19
- 触发节点：1
- 处理节点：13
- 输出节点：5
- 分类：devops
