## 简介
**Automate Job Discovery & AI Proposals across Upwork, Freelancer, Guru & PPH with OpenRouter**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/7782

---

# Automate Job Discovery & AI Proposals across Upwork, Freelancer, Guru & PPH with OpenRouter


## 节点清单

| 节点 | 类型 |
|------|------|
| RSS Feed Trigger | rssFeedReadTrigger |
| Loop Over Items | 分批处理 |
| Extract Title & Budget | Code |
| Decode URL & Source | Code |
| Set Variables | 数据设置 |
| OpenRouter Chat Model | OpenRouter Chat Model |
| Filter | 过滤器 |
| Send a message | Email 发送 |
| Update Datatbase | Google Sheets |
| AI Proposal Agent | AI Agent |
| Append row in sheet | Google Sheets |
| Wait | 等待 |
| Aggregate | 数据聚合 |
| HTML Aggregated email | HTML |
| Limit | 数据限制 |
| Build a single HTML string | Code |



## 功能说明

Automate Job Discovery & AI Proposals across Upwor（AI 增强)手动或子流程调用，通过 邮箱 + HTTP API 实现自动化。

手动触发，通过 邮箱 + HTTP API 实现自动化。

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

- 节点总数：16
- 触发方式：手动或子流程调用

## 触发方式
- RSS Feed Trigger 触发

## 统计
- 节点总数：16
- 触发节点：1
- 处理节点：14
- 输出节点：1
- 分类：workflow-automation
