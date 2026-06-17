## 简介
**Automated Dynamic Pricing with AI Competitor Monitoring & Revenue Optimization**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Slack)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/6448

---

# Automated Dynamic Pricing with AI Competitor Monitoring & Revenue Optimization


## 节点清单

| 节点 | 类型 |
|------|------|
| Hourly Pricing Monitor Trigger | 定时触发器 |
| Pricing Configuration Processor | Code |
| Split Monitoring Tasks | 分批处理 |
| Task Processor | Code |
| AI Competitor Price Scraper | ScrapeGraph AI |
| AI Demand Analysis Scraper | ScrapeGraph AI |
| AI Customer Sentiment Scraper | ScrapeGraph AI |
| Merge Pricing Data | 数据合并 |
| Pricing Optimization Engine | Code |
| Price Change Filter | IF 判断 |
| Price Update API Call | HTTP Request |
| Pricing History Logger | Google Sheets |
| Revenue Analytics Logger | Google Sheets |
| Pricing Alert Sender | Slack |
| Pricing Report Sender | Email 发送 |



## 功能说明

监控告警系统，异常检测并发送通知，定时执行。

定时触发，通过 邮箱 + HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- 邮箱 SMTP/IMAP 账号密码

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：15
- 触发方式：定时触发

## 触发方式
- Hourly Pricing Monitor Trigger 触发

## 统计
- 节点总数：15
- 触发节点：1
- 处理节点：11
- 输出节点：3
- 分类：workflow-automation
