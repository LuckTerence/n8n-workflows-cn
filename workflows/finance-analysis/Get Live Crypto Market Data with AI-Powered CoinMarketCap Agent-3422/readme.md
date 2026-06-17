## 简介
**Get Live Crypto Market Data with AI-Powered CoinMarketCap Agent**

（待补充中文描述）

> 分类：金融分析 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3422

---

# Get Live Crypto Market Data with AI-Powered CoinMarketCap Agent


## 节点清单

| 节点 | 类型 |
|------|------|
| When Executed by Another Workflow | 执行工作流触发器 |
| CoinMarketCap Crypto Agent | AI Agent |
| Crypto Agent Brain | OpenAI Chat Model |
| Crypto Agent Memory | 记忆缓冲区 |
| CoinMarketCap Price | HTTP 工具 |
| Crypto Map | HTTP 工具 |
| Crypto Info | HTTP 工具 |
| Crypto Listings | HTTP 工具 |
| Global Metrics | HTTP 工具 |
| Price Conversion | HTTP 工具 |



## 功能说明

金融数据分析系统，市场行情采集与 AI 分析告警。

手动触发，通过 工作流编排 实现自动化。

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

- 节点总数：10
- 触发方式：手动或子流程调用

## 触发方式
- When Executed by Another Workflow 触发

## 统计
- 节点总数：10
- 触发节点：1
- 处理节点：3
- 输出节点：6
- 分类：finance-analysis
