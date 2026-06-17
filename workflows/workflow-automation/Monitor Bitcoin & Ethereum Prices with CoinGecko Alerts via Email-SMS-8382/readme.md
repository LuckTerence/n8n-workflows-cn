## 简介
**Monitor Bitcoin & Ethereum Prices with CoinGecko Alerts via Email-SMS**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/8382

---

# Monitor Bitcoin & Ethereum Prices with CoinGecko Alerts via Email-SMS


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
