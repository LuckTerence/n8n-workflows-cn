## 简介
**Generate Verified Gym Trial Passes with QR Code, Email & PDF Export**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：B（需替换Google Sheets/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/10768

---

# Generate Verified Gym Trial Passes with QR Code, Email & PDF Export


## 节点清单

| 节点 | 类型 |
|------|------|
| Webhook | Webhook |
| IF Email Valid | IF 判断 |
| Send Error Response | 响应 Webhook |
| Generate Pass Details | Code |
| Generate QR Code | HTTP Request |
| Build HTML Pass | 数据设置 |
| Send Email with Pass | Email 发送 |
| Log to Google Sheets | Google Sheets |
| Send Success Response | 响应 Webhook |
| Verifi Email | verifiEmail |
| HTML/CSS to Image | htmlCssToImage |
| HTML to PDF | htmlcsstopdf |
| Digital Pass | HTTP Request |

## 触发方式
- Webhook 触发

## 统计
- 节点总数：13
- 触发节点：1
- 处理节点：7
- 输出节点：5
- 分类：workflow-automation
