## 简介
**Internet Archive Search API Integration for AI Agents (3 Operations)**

（待补充中文描述）

> 分类：AI Agent | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5535

---

# Internet Archive Search API Integration for AI Agents (3 Operations)


## 节点清单

| 节点 | 类型 |
|------|------|
| Search Services MCP Server | MCP 触发器 |
| Fields that can be requested | HTTP Request 工具 |
| Return relevance-based results from search queries | HTTP Request 工具 |
| Scrape search results from Internet Archive, allowing a scro | HTTP Request 工具 |



## 功能说明

联网搜索工具，AI 驱动的信息检索和分析。

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

- 节点总数：4
- 触发方式：手动或子流程调用

## 触发方式
- Search Services MCP Server 触发

## 统计
- 节点总数：4
- 触发节点：1
- 处理节点：0
- 输出节点：3
- 分类：ai-agent
