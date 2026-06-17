## 简介
**Automate Email Tracking & Generate Pixel for Lead Nurturing with Google Sheet**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A-adapted（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/11248

---

# Automate Email Tracking & Generate Pixel for Lead Nurturing with Google Sheet


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Execute workflow’ | 手动触发 |
| Webhook | Webhook |
| Respond to Webhook | 响应 Webhook |
| OpenAI Chat Model | OpenAI Chat Model |
| Loop Over Items | 分批处理 |
| Get CRM | Google Sheets |
| Generate Pixel | 数据设置 |
| Email Agent | AI Agent |
| Send email | Email 发送 |
| Update CRM | Google Sheets |
| Create data pixel in base64 | 数据设置 |
| Create pixel image | 转换为文件 |
| Get vars | 数据设置 |
| Update Open email 1 | Google Sheets |

## 触发方式
- When clicking ‘Execute workflow’ 触发
- Webhook 触发

## 统计
- 节点总数：14
- 触发节点：2
- 处理节点：10
- 输出节点：2
- 分类：workflow-automation
