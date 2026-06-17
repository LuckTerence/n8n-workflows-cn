# Hackathon Participant Badge Generator with QR Code, PDF & Email Delivery

https://n8nworkflows.xyz/workflows/11016

## 节点清单

| 节点 | 类型 |
|------|------|
| Webhook Trigger | Webhook |
| Validate Input | Function |
| Email Valid? | IF 判断 |
| Generate Badge ID & URL | Function |
| Download PDF | HTTP Request |
| Send Badge via Gmail | Email 发送 |
| Success Response | 响应 Webhook |
| Verifi Email | verifiEmail |
| HTML to PDF | htmlcsstopdf |
| Log to Sheets | Google Sheets |

## 触发方式
- Webhook Trigger 触发

## 统计
- 节点总数：10
- 触发节点：1
- 处理节点：6
- 输出节点：3
- 分类：workflow-automation
