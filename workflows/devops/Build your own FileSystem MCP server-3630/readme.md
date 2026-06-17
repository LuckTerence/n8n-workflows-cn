## 简介
**Build your own FileSystem MCP server**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：10 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/3630

---

# Build your own FileSystem MCP server


## 节点清单

| 节点 | 类型 |
|------|------|
| FileSystem MCP Server | MCP 触发器 |
| ListDirectory | executeCommandTool |
| CreateDirectory | executeCommandTool |
| When Executed by Another Workflow | 执行工作流触发器 |
| Operation | Switch 路由 |
| readOneOrMultipleFiles | 执行命令 |
| ReadFiles | 工作流工具 |
| WriteFiles | 工作流工具 |
| writeOneOrMultipleFiles | 执行命令 |
| SearchDirectory | executeCommandTool |

## 触发方式
- FileSystem MCP Server 触发
- When Executed by Another Workflow 触发

## 统计
- 节点总数：10
- 触发节点：2
- 处理节点：8
- 输出节点：0
- 分类：devops
