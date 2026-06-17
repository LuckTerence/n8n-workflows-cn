## 简介
**Monitor Supplier Financial Health with ScrapeGraphAI & Multi-Channel Risk Alerts**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Slack/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/7129

---

# Monitor Supplier Financial Health with ScrapeGraphAI & Multi-Channel Risk Alerts


## 节点清单

| 节点 | 类型 |
|------|------|
| 📅 Weekly Health Check | 定时触发器 |
| 🏪 Supplier Database Loader | Code |
| 🔍 Has Suppliers to Monitor? | IF 判断 |
| 🕷️ Company Website Scraper | HTTP Request |
| 📰 Financial News Scraper | HTTP Request |
| 🔬 Financial Health Analyzer | Code |
| 📊 Advanced Risk Scorer | Code |
| ⚠️ Risk Above Threshold? | IF 判断 |
| 🔄 Alternative Supplier Finder | Code |
| 📧 Alert Formatter | 数据设置 |
| 📨 Email Alert Sender | Email 发送 |
| 💬 Slack Alert | HTTP Request |
| 🏢 Procurement System Update | HTTP Request |



## 功能说明

监控告警系统，异常检测并发送通知，定时执行。

定时触发，通过 邮箱 + Slack + HTTP API 实现自动化。

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

- 节点总数：13
- 触发方式：定时触发

## 触发方式
- 📅 Weekly Health Check 触发

## 统计
- 节点总数：13
- 触发节点：1
- 处理节点：7
- 输出节点：5
- 分类：workflow-automation
