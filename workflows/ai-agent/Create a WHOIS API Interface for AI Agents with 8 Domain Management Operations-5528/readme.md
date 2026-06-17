## 简介
**Create a WHOIS API Interface for AI Agents with 8 Domain Management Operations**

（待补充中文描述）

> 分类：AI Agent | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5528

---

# Create a WHOIS API Interface for AI Agents with 8 Domain Management Operations


## 节点清单

| 节点 | 类型 |
|------|------|
| Bulk WHOIS MCP Server | MCP 触发器 |
| Get your batches | HTTP Request 工具 |
| Create batch. Batch is then being processed until | HTTP Request 工具 |
| Delete batch | HTTP Request 工具 |
| Get batch | HTTP Request 工具 |
| Query domain database | HTTP Request 工具 |
| Check domain availability | HTTP Request 工具 |
| Check domain rank (authority). | HTTP Request 工具 |
| WHOIS query for a domain | HTTP Request 工具 |



## 功能说明

API 集成接口，连接和编排多个第三方服务。

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

- 节点总数：9
- 触发方式：手动或子流程调用

## 触发方式
- Bulk WHOIS MCP Server 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：0
- 输出节点：8
- 分类：ai-agent
