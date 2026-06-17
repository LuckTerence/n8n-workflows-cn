# Automated Web Scraper: Niche Job-Product Monitor With Telegram Alert

https://n8nworkflows.xyz/workflows/6663

## 节点清单

| 节点 | 类型 |
|------|------|
| Hourly Monitor Trigger | 定时触发器 |
| Fetch Webpage Content | HTTP Request |
| Extract Job/Product Info | htmlExtract |
| If Items Found | IF 判断 |
| Format Notification Message | Function |
| Send Telegram Alert | Telegram |

## 触发方式
- Hourly Monitor Trigger 触发

## 统计
- 节点总数：6
- 触发节点：1
- 处理节点：3
- 输出节点：2
- 分类：workflow-automation
