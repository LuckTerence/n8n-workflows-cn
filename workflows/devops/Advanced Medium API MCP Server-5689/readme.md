## 简介
**Advanced Medium API MCP Server**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5689

---

# Advanced Medium API MCP Server


## 节点清单

| 节点 | 类型 |
|------|------|
| Medium MCP Server | MCP 触发器 |
| Get Welcome Message | HTTP Request 工具 |
| Get Article Details | HTTP Request 工具 |
| Get Article Content | HTTP Request 工具 |
| Get Article Fans | HTTP Request 工具 |
| Get Article Markdown | HTTP Request 工具 |
| Get Related Articles | HTTP Request 工具 |
| Get Article Responses | HTTP Request 工具 |
| Get Latest Posts | HTTP Request 工具 |
| Get Related Tags | HTTP Request 工具 |
| Get Top Writers | HTTP Request 工具 |
| Get Top Feeds | HTTP Request 工具 |
| Get List Details | HTTP Request 工具 |
| Get List Articles | HTTP Request 工具 |
| Get List Responses | HTTP Request 工具 |
| Get Publication ID | HTTP Request 工具 |
| Get Publication Details | HTTP Request 工具 |
| Get Publication Articles | HTTP Request 工具 |
| Get Publication Newsletter | HTTP Request 工具 |
| Search Articles | HTTP Request 工具 |
| Search Lists | HTTP Request 工具 |
| Search Publications | HTTP Request 工具 |
| Search Tags | HTTP Request 工具 |
| Search Users | HTTP Request 工具 |
| Get User ID | HTTP Request 工具 |
| Get User Details | HTTP Request 工具 |
| Get User Articles | HTTP Request 工具 |
| Get User Followers | HTTP Request 工具 |
| Get User Following | HTTP Request 工具 |
| Get User Interests | HTTP Request 工具 |
| Get User Lists | HTTP Request 工具 |
| Get User Publications | HTTP Request 工具 |
| Get User Top Articles | HTTP Request 工具 |



## 功能说明

MCP 协议工具服务，为 AI Agent 暴露 API 接口。

手动触发，通过 HTTP API 实现自动化。

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

- 节点总数：33
- 触发方式：手动或子流程调用

## 触发方式
- Medium MCP Server 触发

## 统计
- 节点总数：33
- 触发节点：1
- 处理节点：0
- 输出节点：32
- 分类：devops
