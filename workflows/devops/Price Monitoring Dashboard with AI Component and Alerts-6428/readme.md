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

## 触发方式
- Daily Price Check Trigger 触发
- Manual Price Check Webhook 触发

## 统计
- 节点总数：10
- 触发节点：2
- 处理节点：4
- 输出节点：4
- 分类：devops
