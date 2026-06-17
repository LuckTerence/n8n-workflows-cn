## 简介
**Automate Email Tracking & Generate Pixel for Lead Nurturing with Google Sheet**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Gmail)（基本改完，配置 API Key 应该就能跑）
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



## 功能说明

邮件自动化处理，AI 分类整理或。

定时触发、Webhook触发、手动触发，通过 邮箱 + HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com
- 邮箱 SMTP/IMAP 账号密码
- 通义万相 API Key → https://dashscope.aliyun.com

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：14
- 触发方式：手动触发, Webhook 触发

## 触发方式
- When clicking ‘Execute workflow’ 触发
- Webhook 触发

## 统计
- 节点总数：14
- 触发节点：2
- 处理节点：10
- 输出节点：2
- 分类：workflow-automation
