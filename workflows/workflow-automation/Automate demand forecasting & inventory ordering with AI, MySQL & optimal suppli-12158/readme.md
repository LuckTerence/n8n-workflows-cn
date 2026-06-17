## 简介
**Automate demand forecasting & inventory ordering with AI, MySQL & optimal supplier selection**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/12158

---

# Automate demand forecasting & inventory ordering with AI, MySQL & optimal supplier selection


## 节点清单

| 节点 | 类型 |
|------|------|
| Run Daily at 03:00 | 定时触发器 |
| Fetch POS Data | HTTP Request |
| Fetch Historical Sales | MySQL |
| Fetch Weather Forecast | HTTP Request |
| Fetch SNS Trends | HTTP Request |
| Fetch Inventory Master | HTTP Request |
| Merge Data 1 | 数据合并 |
| Merge Data 2 | 数据合并 |
| Format Prediction Dataset | Code |
| Call AI Prediction API | HTTP Request |
| Calculate Stock Shortage | Code |
| Finalize Order Qty | Code |
| Check Order Necessity | IF 判断 |
| Split by Product | 分批处理 |
| Get Quote Supplier A | HTTP Request |
| Get Quote Supplier B | HTTP Request |
| Get Quote Supplier C | HTTP Request |
| Merge Quotes | 数据合并 |
| Select Best Supplier | Code |
| Execute Auto Order | HTTP Request |
| Update Inventory System | HTTP Request |
| Save Order Log | MySQL |
| Check Anomalies | IF 判断 |
| Slack Anomaly Alert | Slack |



## 功能说明

电商自动化，订单处理或商品管理，定时执行。

定时触发，通过 Slack + HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

无需额外 API Key，导入即可运行。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：24
- 触发方式：定时触发

## 触发方式
- Run Daily at 03:00 触发

## 统计
- 节点总数：24
- 触发节点：1
- 处理节点：12
- 输出节点：11
- 分类：workflow-automation
