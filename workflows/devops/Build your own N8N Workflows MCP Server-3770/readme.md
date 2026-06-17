## 简介
**Build your own N8N Workflows MCP Server**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3770

---

# Build your own N8N Workflows MCP Server


## 节点清单

| 节点 | 类型 |
|------|------|
| Simplify Workflows | 数据设置 |
| When Executed by Another Workflow | 执行工作流触发器 |
| Operations | Switch 路由 |
| Get MCP-tagged Workflows | n8n |
| Filter Matching Ids | 过滤器 |
| Store In Memory | Redis |
| AddTool Success | 数据设置 |
| AddTool Error | 数据设置 |
| Get Memory | Redis |
| Split Out | 数据拆分 |
| Filter Matching IDs | 过滤器 |
| Store In Memory1 | Redis |
| Remove Tool Success | 数据设置 |
| Convert to JSON | 数据设置 |
| listTools Success | 数据设置 |
| Get MCP-tagged Workflows1 | n8n |
| Simplify Workflows1 | 数据设置 |
| listTools Success1 | 数据聚合 |
| Get Parameters | 数据设置 |
| executeTool Result | 数据聚合 |
| AI Agent | AI Agent |
| When chat message received | Chat 触发器 |
| MCP Client | MCP 客户端 |
| Simple Memory | 记忆缓冲区 |
| Convert to JSON1 | 数据设置 |
| Has Workflow Available? | IF 判断 |
| ExecuteTool Error | 数据设置 |
| Workflow Exists? | IF 判断 |
| N8N Workflows MCP Server | MCP 触发器 |
| Add Workflow | 工作流工具 |
| RemoveWorkflow | 工作流工具 |
| List Workflows | 工作流工具 |
| SearchWorkflows | 工作流工具 |
| ExecuteWorkflow | 工作流工具 |
| Execute Workflow with PassThrough Variables | 执行工作流 |
| OpenAI Chat Model | OpenAI Chat Model |
| Is Empty Array? | IF 判断 |
| Delete Key | Redis |



## 功能说明

MCP 协议工具服务，为 AI Agent 暴露 API 接口。

Chat 消息触发，通过 工作流编排 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：38
- 触发方式：Chat 消息触发

## 触发方式
- When Executed by Another Workflow 触发
- When chat message received 触发
- N8N Workflows MCP Server 触发

## 统计
- 节点总数：38
- 触发节点：3
- 处理节点：35
- 输出节点：0
- 分类：devops
