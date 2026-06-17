# Automated Referral Reward System with Email Verification and Visual Coupons

https://n8nworkflows.xyz/workflows/10161

## 节点清单

| 节点 | 类型 |
|------|------|
| Webhook Trigger | Webhook |
| IF Email Valid? | IF 判断 |
| Set Coupon Template | 数据设置 |
| Send Reward Email (Gmail) | Email 发送 |
| Log to Google Sheets (Success) | Google Sheets |
| Send Invalid Email Notice | Email 发送 |
| Log to Google Sheets (Failed) | Google Sheets |
| Verifi Email | verifiEmail |
| HTML/CSS to Image | htmlCssToImage |

## 触发方式
- Webhook Trigger 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：6
- 输出节点：2
- 分类：workflow-automation
