## 简介
**Build your own CUSTOM API MCP server**

（待补充中文描述）

> 分类：DevOps | 适配等级：B（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3638

---

# Build your own CUSTOM API MCP server


## 节点清单

| 节点 | 类型 |
|------|------|
| When Executed by Another Workflow | 执行工作流触发器 |
| Operation | Switch 路由 |
| Paycaptain MCP Server | MCP 触发器 |
| Update Employee | 工作流工具 |
| Get Employee | 工作流工具 |
| Get Employees | HTTP Request |
| Search Employees | 工作流工具 |
| Log Call | Google Sheets |
| Filter Matches | 过滤器 |
| Aggregate Search Results | 数据聚合 |
| Get Employees1 | HTTP Request |
| Filter Matching ID | 过滤器 |
| Strip Sensitive Fields1 | 数据设置 |
| Strip Sensitive Fields | 数据设置 |
| Update Employee1 | HTTP Request |
| Valid Fields Only | 数据设置 |
| Has Valid Request? | IF 判断 |
| Get Error Response | 数据设置 |
| Get Success Response | 数据设置 |
| Aggregate Get Response | 数据聚合 |

## 触发方式
- When Executed by Another Workflow 触发
- Paycaptain MCP Server 触发

## 统计
- 节点总数：20
- 触发节点：2
- 处理节点：15
- 输出节点：3
- 分类：devops
