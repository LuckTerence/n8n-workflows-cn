# Monitor Supplier Financial Health with ScrapeGraphAI & Multi-Channel Risk Alerts

https://n8nworkflows.xyz/workflows/7129

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

## 触发方式
- 📅 Weekly Health Check 触发

## 统计
- 节点总数：13
- 触发节点：1
- 处理节点：7
- 输出节点：5
- 分类：workflow-automation
