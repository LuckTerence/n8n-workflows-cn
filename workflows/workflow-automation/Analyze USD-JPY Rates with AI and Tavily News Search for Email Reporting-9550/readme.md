## 简介
**Analyze USD-JPY Rates with AI and Tavily News Search for Email Reporting**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/9550

---

# Analyze USD-JPY Rates with AI and Tavily News Search for Email Reporting


## 节点清单

| 节点 | 类型 |
|------|------|
| Run every 4 hours | 定时触发器 |
| Analyze USD/JPY (AI agent) | AI Agent |
| LLM provider (configure) | OpenRouter Chat Model |
| Tool: Search Forex News (Tavily) | HTTP 工具 |
| Tool: Structured Output Parser | 结构化输出解析器 |
| Send results via Gmail | Email 发送 |
| Set (Fields) — Configure me | 数据设置 |
| Fetch USD/JPY rate (HTTP) | HTTP Request |



## 功能说明

邮件自动化处理，AI 分类整理或。

定时触发，通过 邮箱 + HTTP API 实现自动化。

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

- 节点总数：8
- 触发方式：定时触发

## 触发方式
- Run every 4 hours 触发

## 统计
- 节点总数：8
- 触发节点：1
- 处理节点：4
- 输出节点：3
- 分类：workflow-automation
