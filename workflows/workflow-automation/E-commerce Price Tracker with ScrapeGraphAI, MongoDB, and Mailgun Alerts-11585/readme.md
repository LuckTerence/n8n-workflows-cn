## 简介
**E-commerce Price Tracker with ScrapeGraphAI, MongoDB, and Mailgun Alerts**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：10 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/11585

---

# E-commerce Price Tracker with ScrapeGraphAI, MongoDB, and Mailgun Alerts


## 节点清单

| 节点 | 类型 |
|------|------|
| Incoming Monitor Request | Webhook |
| Define Product Sources | Code |
| Split URLs | 分批处理 |
| Scrape Product Page | ScrapeGraph AI |
| Combine Scraped Data | 数据合并 |
| Analyze Price Movement | Code |
| Store to MongoDB | MongoDB |
| Significant Price Change? | IF 判断 |
| Prepare Alert Email | 数据设置 |
| Send Mailgun Alert | mailgun |
| Send Webhook Response | 响应 Webhook |

## 触发方式
- Incoming Monitor Request 触发

## 统计
- 节点总数：11
- 触发节点：1
- 处理节点：9
- 输出节点：1
- 分类：workflow-automation
