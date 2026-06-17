## 简介
**Connect Buffer Social Media Management API to AI Agents via MCP Protocol**

（待补充中文描述）

> 分类：AI Agent | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5547

---

# Connect Buffer Social Media Management API to AI Agents via MCP Protocol


## 节点清单

| 节点 | 类型 |
|------|------|
| Bufferapp MCP Server | MCP 触发器 |
| Get Buffer Configuration | HTTP Request 工具 |
| Get Link Share Count | HTTP Request 工具 |
| Update Profile Schedules | HTTP Request 工具 |
| Get Profile Schedules | HTTP Request 工具 |
| Get Pending Updates | HTTP Request 工具 |
| Reorder Profile Updates | HTTP Request 工具 |
| Get Sent Updates | HTTP Request 工具 |
| Shuffle Profile Updates | HTTP Request 工具 |
| Get Profile Details | HTTP Request 工具 |
| List User Profiles | HTTP Request 工具 |
| Create Status Updates | HTTP Request 工具 |
| Delete Status Update | HTTP Request 工具 |
| Get Update Interactions | HTTP Request 工具 |
| Move Update to Top | HTTP Request 工具 |
| Share Update Immediately | HTTP Request 工具 |
| Edit Status Update | HTTP Request 工具 |
| Get Status Update | HTTP Request 工具 |
| Get User Details | HTTP Request 工具 |



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

- 节点总数：19
- 触发方式：手动或子流程调用

## 触发方式
- Bufferapp MCP Server 触发

## 统计
- 节点总数：19
- 触发节点：1
- 处理节点：0
- 输出节点：18
- 分类：ai-agent
