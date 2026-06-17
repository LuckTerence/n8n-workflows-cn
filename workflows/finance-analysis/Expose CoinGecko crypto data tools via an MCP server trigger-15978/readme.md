## 简介
**Expose CoinGecko crypto data tools via an MCP server trigger**

（待补充中文描述）

> 分类：金融分析 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/15978

---

# Expose CoinGecko crypto data tools via an MCP server trigger


## 节点清单

| 节点 | 类型 |
|------|------|
| When Triggered by CoinGecko | MCP 触发器 |
| Fetch Candlestick Data | coinGeckoTool |
| Retrieve Coin Details | coinGeckoTool |
| Retrieve Multiple Coins | coinGeckoTool |
| Fetch Coin Historical Data | coinGeckoTool |
| Retrieve Market Prices | coinGeckoTool |
| Fetch Market Chart Data | coinGeckoTool |
| Retrieve Current Coin Price | coinGeckoTool |
| Fetch Coin Ticker Data | coinGeckoTool |
| Retrieve Multiple Events | coinGeckoTool |



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
- When Triggered by CoinGecko 触发

## 统计
- 节点总数：10
- 触发节点：1
- 处理节点：9
- 输出节点：0
- 分类：finance-analysis
