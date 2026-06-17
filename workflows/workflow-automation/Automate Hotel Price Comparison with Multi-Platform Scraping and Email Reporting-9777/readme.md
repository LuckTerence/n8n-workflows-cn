# Automate Hotel Price Comparison with Multi-Platform Scraping and Email Reporting

https://n8nworkflows.xyz/workflows/9777

## 节点清单

| 节点 | 类型 |
|------|------|
| Webhook - Receive Request | Webhook |
| Parse & Validate Request | Code |
| Check If Ready | IF 判断 |
| Scrape Booking.com | HTTP Request |
| Scrape Agoda | HTTP Request |
| Scrape Expedia | HTTP Request |
| Aggregate & Compare | Code |
| Format Email Report | Code |
| Send Email Report | Email 发送 |
| Webhook Response (Success) | 响应 Webhook |
| Webhook Response (Info) | 响应 Webhook |
| Log Analytics | 数据设置 |
| Save to Google Sheets | Google Sheets |

## 触发方式
- Webhook - Receive Request 触发

## 统计
- 节点总数：13
- 触发节点：1
- 处理节点：6
- 输出节点：6
- 分类：workflow-automation
