## 简介
**Automate Event RSVPs with Email Validation & Badge Generation using VerifiEmail & HTMLCssToImage**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A-adapted（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/10169

---

# Automate Event RSVPs with Email Validation & Badge Generation using VerifiEmail & HTMLCssToImage


## 节点清单

| 节点 | 类型 |
|------|------|
| IF Email Valid? | IF 判断 |
| Prepare Badge Data | 数据设置 |
| Send Confirmation Email - Gmail | Email 发送 |
| Log to Google Sheets - Valid | Google Sheets |
| Send Rejection Email - Invalid | Email 发送 |
| Log Invalid to Sheets | Google Sheets |
| Verifi Email | verifiEmail |
| Webhook - RSVP Form Submission | Webhook |
| HTML/CSS to Image | htmlCssToImage |

## 触发方式
- Webhook - RSVP Form Submission 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：6
- 输出节点：2
- 分类：workflow-automation
