## 简介
**Automated Forex and Gold Trading Signal Handler with MetaTrader 5 via Webhooks**

（待补充中文描述）

> 分类：金融分析 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/11439

---

# Automated Forex and Gold Trading Signal Handler with MetaTrader 5 via Webhooks


## 节点清单

| 节点 | 类型 |
|------|------|
| Receive Signal (POST) | Webhook |
| Store Signal | Code |
| Respond to POST | 响应 Webhook |
| Get Pending Signals (GET) | Webhook |
| Fetch Pending Signals | Code |
| Return Signals | 响应 Webhook |
| Confirm Signal Processed (POST) | Webhook |
| Mark as Processed | Code |
| Confirm Response | 响应 Webhook |
| clear all signals | Code |
| Clear all signals (POST) | Webhook |
| Market Order (POST) | Webhook |
| market order code | Code |
| Respond to Webhook | 响应 Webhook |
| Limit Order (POST) | Webhook |
| limit order code | Code |
| Respond to Limit Order | 响应 Webhook |
| confirm signals are cleared | 响应 Webhook |



## 功能说明

金融数据分析系统，市场行情采集与 AI 分析告警，Webhook 触发。

Webhook触发，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

无需额外 API Key，导入即可运行。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：18
- 触发方式：Webhook 触发

## 触发方式
- Receive Signal (POST) 触发
- Get Pending Signals (GET) 触发
- Confirm Signal Processed (POST) 触发
- Clear all signals (POST) 触发
- Market Order (POST) 触发
- Limit Order (POST) 触发

## 统计
- 节点总数：18
- 触发节点：6
- 处理节点：6
- 输出节点：6
- 分类：finance-analysis
