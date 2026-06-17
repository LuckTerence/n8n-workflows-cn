# Monitor Bitcoin & Ethereum Prices with CoinGecko Alerts via Email-SMS

https://n8nworkflows.xyz/workflows/8382

## 节点清单

| 节点 | 类型 |
|------|------|
| Every 15 Minutes | 定时触发器 |
| Get Crypto Prices | HTTP Request |
| Compute Threshold Flags | Code |
| Any Alert? | IF 判断 |
| Format Alert Email | Code |
| Send a message | Email 发送 |
| Send an SMS/MMS/WhatsApp message | twilio |

## 触发方式
- Every 15 Minutes 触发

## 统计
- 节点总数：7
- 触发节点：1
- 处理节点：4
- 输出节点：2
- 分类：workflow-automation
