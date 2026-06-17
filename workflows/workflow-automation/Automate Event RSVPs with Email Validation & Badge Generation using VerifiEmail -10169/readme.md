# Automate Event RSVPs with Email Validation & Badge Generation using VerifiEmail & HTMLCssToImage

https://n8nworkflows.xyz/workflows/10169

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
