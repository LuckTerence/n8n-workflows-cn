## 简介
**Aggregate Crypto and Stock Market News Feed from Multiple Sources**

（待补充中文描述）

> 分类：金融分析 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/11103

---

# Aggregate Crypto and Stock Market News Feed from Multiple Sources


## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Trigger | 定时触发器 |
| RSS Read - Coindesk | RSS Feed |
| RSS Read - Google news | RSS Feed |
| RSS Read - X Posts | RSS Feed |
| Source set - Coindesk | 数据设置 |
| Source set - Google news | 数据设置 |
| Source set - Cointelegraph | 数据设置 |
| Source set - X Posts | 数据设置 |
| Merge - Coindesk + Google news | 数据合并 |
| Merge - X posts + CoinTelegraph | 数据合并 |
| Merge - Merge previous two merges | 数据合并 |
| Code - Keywords Filter | Code |
| Code - Array bind | Code |
| Webhook | Webhook |
| Merge | 数据合并 |
| Init RunConfig | Code |
| IF Gate - Coindesk | IF 判断 |
| IF Gate - Google news | IF 判断 |
| IF Gate - CoinTelegraph | IF 判断 |
| IF Gate - X | IF 判断 |
| X Batches | 分批处理 |
| IF - More X batches? | IF 判断 |
| Code - Finalize X batches (emit combined) | Code |
| Code - Accumulate X items | Code |
| Code - Reset X accumulator | Code |
| Code - URL Build - XCancel | Code |
| Code - Tag topic - Google news | Code |
| Code - Tag topic - Coin desk | Code |
| Code - Tag topic - X | Code |
| Code - URL build - Google news | Code |
| HTTP Request - Send to your backend | HTTP Request |
| Loop back – X Batches | 空操作 |
| Code - Tag topic - Coin telegraph | Code |
| RSS Read - CoinTelegraph | RSS Feed |



## 功能说明

金融数据分析系统，市场行情采集与 AI 分析告警，定时执行。

定时触发、Webhook触发，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

无需额外 API Key，导入即可运行。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：34
- 触发方式：定时触发, Webhook 触发

## 触发方式
- Schedule Trigger 触发
- RSS Read - Coindesk 触发
- RSS Read - Google news 触发
- RSS Read - X Posts 触发
- Webhook 触发
- RSS Read - CoinTelegraph 触发

## 统计
- 节点总数：34
- 触发节点：6
- 处理节点：27
- 输出节点：1
- 分类：finance-analysis
