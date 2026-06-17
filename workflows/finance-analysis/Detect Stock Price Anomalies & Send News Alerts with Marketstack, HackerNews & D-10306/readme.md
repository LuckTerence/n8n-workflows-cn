## 简介
**Detect Stock Price Anomalies & Send News Alerts with Marketstack, HackerNews & DeepL**

（待补充中文描述）

> 分类：金融分析 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/10306

---

# Detect Stock Price Anomalies & Send News Alerts with Marketstack, HackerNews & DeepL


## 节点清单

| 节点 | 类型 |
|------|------|
| Daily Check | 定时触发器 |
| Get Stock Data | marketstack |
| Calculate Deviation | Code |
| Is Anomaly? (status != "normal") | IF 判断 |
| Get Related News | hackerNews |
| Translate News | deepL |
| Send Alert to Slack | Slack |
| Send Normal Report to Slack | Slack |
| Merge Original + Translated | 数据合并 |
| Add Symbol Field | 数据设置 |
| Compose Slack Message | Code |
| Build News Keyword | Code |



## 功能说明

金融数据分析系统，市场行情采集与 AI 分析告警，定时执行。

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

- 节点总数：12
- 触发方式：定时触发

## 触发方式
- Daily Check 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：9
- 输出节点：2
- 分类：finance-analysis
