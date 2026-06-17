## 简介
**Build your own SQLite MCP server**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3632

---

# Build your own SQLite MCP server


## 节点清单

| 节点 | 类型 |
|------|------|
| When Executed by Another Workflow | 执行工作流触发器 |
| Operation | Switch 路由 |
| SQLite MCP Server | MCP 触发器 |
| CreateRecord | Code |
| UpdateRecord | Code |
| ReadRecords | Code |
| DescribeTables | 代码工具 |
| ListTables | 代码工具 |
| CreateRecords | 工作流工具 |
| UpdateRows | 工作流工具 |
| ReadRows | 工作流工具 |



## 功能说明

MCP 协议工具服务，为 AI Agent 暴露 API 接口。

手动触发，通过 数据库 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com
- 数据库连接信息

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：11
- 触发方式：手动或子流程调用

## 触发方式
- When Executed by Another Workflow 触发
- SQLite MCP Server 触发

## 统计
- 节点总数：11
- 触发节点：2
- 处理节点：9
- 输出节点：0
- 分类：devops
