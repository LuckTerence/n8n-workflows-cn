## 简介
**Build your own PostgreSQL MCP server**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：11 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/3631

---

# Build your own PostgreSQL MCP server


## 节点清单

| 节点 | 类型 |
|------|------|
| GetTableSchema | PostgreSQL 工具 |
| ListTables | PostgreSQL 工具 |
| When Executed by Another Workflow | 执行工作流触发器 |
| CreateTableRecords | 工作流工具 |
| ReadTableRecord | PostgreSQL |
| Operation | Switch 路由 |
| UpdateTableRecord | PostgreSQL |
| UpdateTableRecords | 工作流工具 |
| CreateTableRecord | PostgreSQL |
| ReadTableRows | 工作流工具 |
| PostgreSQL MCP Server | MCP 触发器 |

## 触发方式
- When Executed by Another Workflow 触发
- PostgreSQL MCP Server 触发

## 统计
- 节点总数：11
- 触发节点：2
- 处理节点：9
- 输出节点：0
- 分类：devops
