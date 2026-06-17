## 简介
**Document Parsing & Data Extraction with Mistral OCR, AI Processing, and Multi-Channel Delivery**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4933

---

# Document Parsing & Data Extraction with Mistral OCR, AI Processing, and Multi-Channel Delivery


## 节点清单

| 节点 | 类型 |
|------|------|
| send pdf to Mistral | HTTP Request |
| mistral - get signed url | HTTP Request |
| Mistral Cloud Chat Model1 | Mistral Chat Model |
| Edit Fields | 数据设置 |
| Get Parsed Invoice | HTTP Request |
| AI Agent | AI Agent |
| Markdown | Markdown |
| Edit Fields2 | 数据设置 |
| Gmail | Email 发送 |
| AI Agent1 | AI Agent |
| OpenAI Chat Model | OpenAI Chat Model |
| Telegram Trigger | Telegram 触发器 |
| Download File | HTTP Request |
| Send Confirmation | Telegram |
| Telegram | Telegram |
| Telegram1 | Telegram |
| Code | Code |
| On form submission | 表单触发器 |



## 功能说明

数据采集工具，自动抓取网页或 API 数据。

Telegram 消息触发，通过 Telegram 通知 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com
- Telegram Bot Token → @BotFather 创建
- 邮箱 SMTP/IMAP 账号密码
- 通义万相 API Key → https://dashscope.aliyun.com

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：18
- 触发方式：Telegram 消息触发, 表单提交触发

## 触发方式
- Telegram Trigger 触发
- On form submission 触发

## 统计
- 节点总数：18
- 触发节点：2
- 处理节点：8
- 输出节点：8
- 分类：workflow-automation
