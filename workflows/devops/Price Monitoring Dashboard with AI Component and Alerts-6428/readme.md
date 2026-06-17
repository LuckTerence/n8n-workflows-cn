## 简介
**Price Monitoring Dashboard with AI Component and Alerts**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（需替换Google Sheets/Slack)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/6428

---

# Price Monitoring Dashboard with AI Component and Alerts


## 节点清单

| 节点 | 类型 |
|------|------|
| Daily Price Check Trigger | 定时触发器 |
| Manual Price Check Webhook | Webhook |
| Amazon Price Scraper | HTTP Request |
| Best Buy Price Scraper | HTTP Request |
| Target Price Scraper | HTTP Request |
| AI Price Data Extractor | ScrapeGraph AI |
| Price Analysis & Intelligence | Code |
| Google Sheets Price Log | Google Sheets |
| Price Change Alert Filter | IF 判断 |
| Slack Price Alert | Slack |



## 功能说明

监控告警系统，异常检测并发送通知，定时执行。

定时触发、Webhook触发，通过 在线表格 + Slack + HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

无需额外 API Key，导入即可运行。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：10
- 触发方式：定时触发, Webhook 触发

## 触发方式
- Daily Price Check Trigger 触发
- Manual Price Check Webhook 触发

## 统计
- 节点总数：10
- 触发节点：2
- 处理节点：4
- 输出节点：4
- 分类：devops
