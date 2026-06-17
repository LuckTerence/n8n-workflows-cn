# Automated Press Pass Verification & Badge Creation with QR Codes & Multi-Channel Distribution

https://n8nworkflows.xyz/workflows/10793

## 节点清单

| 节点 | 类型 |
|------|------|
| Webhook Trigger | Webhook |
| Validate Required Fields | IF 判断 |
| Stop: Incomplete Data | 停止并报错 |
| Check Domain Verified | IF 判断 |
| Stop: Domain Not Verified | 停止并报错 |
| Generate Press ID & QR | Code |
| Send Press Pass Email | Email 发送 |
| Notify Organizers (Slack) | Slack |
| Log to Google Sheets | Google Sheets |
| Respond to Webhook | 响应 Webhook |
| Verifi Email | verifiEmail |
| HTML/CSS to Image | htmlCssToImage |

## 触发方式
- Webhook Trigger 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：8
- 输出节点：3
- 分类：workflow-automation
