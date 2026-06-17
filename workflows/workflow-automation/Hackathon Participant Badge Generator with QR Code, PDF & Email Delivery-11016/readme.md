## 简介
**Hackathon Participant Badge Generator with QR Code, PDF & Email Delivery**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/11016

---

# Hackathon Participant Badge Generator with QR Code, PDF & Email Delivery


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
