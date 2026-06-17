## 简介
**Generate branded PDF reports from incoming emails using Autype and OpenRouter**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/14184

---

# Generate branded PDF reports from incoming emails using Autype and OpenRouter


## 节点清单

| 节点 | 类型 |
|------|------|
| Set Company Config | 数据设置 |
| New Email Received | Email 读取 |
| Extract & Split PDFs | Code |
| Has PDFs? | IF 判断 |
| Loop Over PDFs | 分批处理 |
| Upload PDF to Autype | autype |
| Wait for OCR | 等待 |
| Poll OCR Status | HTTP Request |
| Extract OCR Text | Code |
| Combine All OCR Results | Code |
| Prepare Text Only | Code |
| Download Markdown Syntax | HTTP Request |
| Merge Context | Code |
| AI Document Assistant | AI Agent |
| Prepare Render Payload | Code |
| Render Branded PDF | autype |
| Send Report via Email | Email 发送 |
| /scrape in Firecrawl | Firecrawl 工具 |
| OpenRouter Chat Model | OpenRouter Chat Model |
| SerpAPI | SerpApi 工具 |
| Autype Lens OCR | HTTP Request |



## 功能说明

邮件自动化处理，AI 分类整理或。

定时触发、手动触发，通过 邮箱 + HTTP API 实现自动化。

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

- 节点总数：21
- 触发方式：手动或子流程调用

## 触发方式
- 手动触发

## 统计
- 节点总数：21
- 触发节点：0
- 处理节点：16
- 输出节点：5
- 分类：workflow-automation
