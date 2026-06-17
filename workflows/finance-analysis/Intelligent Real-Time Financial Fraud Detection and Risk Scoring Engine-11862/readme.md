## 简介
**Intelligent Real-Time Financial Fraud Detection and Risk Scoring Engine**

（待补充中文描述）

> 分类：金融分析 | 适配等级：B（需替换Google Sheets/Slack/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/11862

---

# Intelligent Real-Time Financial Fraud Detection and Risk Scoring Engine


## 节点清单

| 节点 | 类型 |
|------|------|
| Transaction Webhook | Webhook |
| Workflow Configuration | 数据设置 |
| Fraud Detection AI Agent | AI Agent |
| OpenAI GPT-4 | OpenAI Chat Model |
| Risk Score Output Parser | 结构化输出解析器 |
| Check Risk Level | IF 判断 |
| Hold Transaction | HTTP Request |
| Send High Risk Alert | Slack |
| Email Fraud Team | Email 发送 |
| Log High Risk Incident | Google Sheets |
| Log Low Risk Transaction | Google Sheets |
| Prepare Incident Log Data | 数据设置 |

## 触发方式
- Transaction Webhook 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：8
- 输出节点：3
- 分类：finance-analysis
