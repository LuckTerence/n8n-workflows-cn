## 简介
**Health Monitoring System with Grok-3 AI Analysis and Family-Doctor Email Alerts**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Twilio/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/10525

---

# Health Monitoring System with Grok-3 AI Analysis and Family-Doctor Email Alerts


## 节点清单

| 节点 | 类型 |
|------|------|
| Webhook - Submit Health Data | Webhook |
| Extract Health Data | 数据设置 |
| AI Health Analysis Agent | AI Agent |
| Structured Output Parser | 结构化输出解析器 |
| Check If Alert Needed | IF 判断 |
| Prepare Alert Data | 数据设置 |
| Send Email to Family | Email 发送 |
| Check If Doctor Alert Needed | IF 判断 |
| Send Email to Doctor | Email 发送 |
| Merge Alert Results | 数据设置 |
| No Alert Required | 数据设置 |
| Combine Results | 数据合并 |
| Respond to Webhook | 响应 Webhook |
| OpenRouter Chat Model | OpenRouter Chat Model |



## 功能说明

邮件自动化处理，AI 分类整理或。

定时触发、Webhook触发，通过 邮箱 + HTTP API 实现自动化。

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

- 节点总数：14
- 触发方式：Webhook 触发

## 触发方式
- Webhook - Submit Health Data 触发

## 统计
- 节点总数：14
- 触发节点：1
- 处理节点：10
- 输出节点：3
- 分类：workflow-automation
