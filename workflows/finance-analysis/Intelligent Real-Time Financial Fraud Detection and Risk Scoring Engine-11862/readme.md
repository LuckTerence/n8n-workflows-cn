## 简介
**Intelligent Real-Time Financial Fraud Detection and Risk Scoring Engine**

（待补充中文描述）

> 分类：金融分析 | 适配等级：A（需替换Google Sheets/Slack/Gmail)（基本改完，配置 API Key 应该就能跑）
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



## 功能说明

Intelligent Real-Time Financial Fraud Detection an（AI 增强)Webhook 触发，通过 邮箱 + HTTP API 实现自动化。

Webhook触发，通过 邮箱 + HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com
- 邮箱 SMTP/IMAP 账号密码

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：12
- 触发方式：Webhook 触发

## 触发方式
- Transaction Webhook 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：8
- 输出节点：3
- 分类：finance-analysis
