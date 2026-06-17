# Compare Flight Prices Across Multiple Booking Platforms with Email Reports

https://n8nworkflows.xyz/workflows/9788

## 节点清单

| 节点 | 类型 |
|------|------|
| Webhook - Receive Flight Request | Webhook |
| Parse & Validate Flight Request | Code |
| Check If Request Valid | IF 判断 |
| Scrape Kayak | SSH |
| Scrape Skyscanner | SSH |
| Scrape Expedia | SSH |
| Scrape Google Flights | SSH |
| Aggregate & Analyze Prices | Code |
| Format Email Report | Code |
| Send Email Report | Email 发送 |
| Webhook Response (Success) | 响应 Webhook |
| Webhook Response (Error) | 响应 Webhook |

## 触发方式
- Webhook - Receive Flight Request 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：8
- 输出节点：3
- 分类：workflow-automation
