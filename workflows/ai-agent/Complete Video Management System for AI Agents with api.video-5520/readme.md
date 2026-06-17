## 简介
**Complete Video Management System for AI Agents with api.video**

（待补充中文描述）

> 分类：AI Agent | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5520

---

# Complete Video Management System for AI Agents with api.video


## 节点清单

| 节点 | 类型 |
|------|------|
| api.video MCP Server | MCP 触发器 |
| Show account | HTTP Request 工具 |
| List live stream player sessions | HTTP Request 工具 |
| List player session events | HTTP Request 工具 |
| List video player sessions | HTTP Request 工具 |
| Authenticate | HTTP Request 工具 |
| Refresh token | HTTP Request 工具 |
| List all live streams | HTTP Request 工具 |
| Create live stream | HTTP Request 工具 |
| Delete a live stream | HTTP Request 工具 |
| Show live stream | HTTP Request 工具 |
| Update a live stream | HTTP Request 工具 |
| Delete a thumbnail | HTTP Request 工具 |
| Upload a thumbnail | HTTP Request 工具 |
| List all players | HTTP Request 工具 |
| Create a player | HTTP Request 工具 |
| Delete a player | HTTP Request 工具 |
| Show a player | HTTP Request 工具 |
| Update a player | HTTP Request 工具 |
| Delete logo | HTTP Request 工具 |
| Upload a logo | HTTP Request 工具 |
| Upload with an upload token | HTTP Request 工具 |
| List all active upload tokens. | HTTP Request 工具 |
| Generate an upload token | HTTP Request 工具 |
| Delete an upload token | HTTP Request 工具 |
| Show upload token | HTTP Request 工具 |
| List all videos | HTTP Request 工具 |
| Create a video | HTTP Request 工具 |
| Delete a video | HTTP Request 工具 |
| Show a video | HTTP Request 工具 |
| Update a video | HTTP Request 工具 |
| Upload a video | HTTP Request 工具 |
| Show video status | HTTP Request 工具 |
| Pick a thumbnail | HTTP Request 工具 |
| Upload a thumbnail 1 | HTTP Request 工具 |
| List video captions | HTTP Request 工具 |
| Delete a caption | HTTP Request 工具 |
| Show a caption | HTTP Request 工具 |
| Update caption | HTTP Request 工具 |
| Upload a caption | HTTP Request 工具 |
| List video chapters | HTTP Request 工具 |
| Delete a chapter | HTTP Request 工具 |
| Show a chapter | HTTP Request 工具 |
| Upload a chapter | HTTP Request 工具 |
| List all webhooks | HTTP Request 工具 |
| Create Webhook | HTTP Request 工具 |
| Delete a Webhook | HTTP Request 工具 |
| Show Webhook details | HTTP Request 工具 |



## 功能说明

AI 视频生成工作流，自动创作视频内容。

手动触发，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com
- 通义万相 API Key → https://dashscope.aliyun.com

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：48
- 触发方式：手动或子流程调用

## 触发方式
- api.video MCP Server 触发

## 统计
- 节点总数：48
- 触发节点：1
- 处理节点：0
- 输出节点：47
- 分类：ai-agent
