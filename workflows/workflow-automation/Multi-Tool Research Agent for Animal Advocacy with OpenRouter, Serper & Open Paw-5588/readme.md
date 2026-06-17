## 简介
**Multi-Tool Research Agent for Animal Advocacy with OpenRouter, Serper & Open Paws DB**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5588

---

# Multi-Tool Research Agent for Animal Advocacy with OpenRouter, Serper & Open Paws DB


## 节点清单

| 节点 | 类型 |
|------|------|
| Serper API | HTTP 工具 |
| OpenRouter Chat Model | OpenRouter Chat Model |
| AI Agent | AI Agent |
| Database Retrieval | HTTP 工具 |
| When Executed by Another Workflow | 执行工作流触发器 |
| When chat message received | Chat 触发器 |
| Think | 思考工具 |
| Email Finder | hunterTool |
| Email Verifier | hunterTool |
| Set Fields | 数据设置 |
| Web Scraper Tool | HTTP 工具 |
| Twitter Post Scraper | HTTP 工具 |
| Twitter Profile Scraper | HTTP 工具 |
| Instagram Profile Scraper | HTTP 工具 |
| Linkedin Person and Company Scraper | HTTP 工具 |
| If | IF 判断 |
| Simple Memory | 记忆缓冲区 |
| Fix Empty Response | LLM Chain |
| OpenRouter Chat Model1 | OpenRouter Chat Model |
| Set Output (If Empty) | 数据设置 |
| Set Output (If Not Empty) | 数据设置 |
| Score Text | 工作流工具 |



## 功能说明

多智能体协作系统，多个 AI Agent 协同完成任务。

Chat 消息触发，通过 邮箱 实现自动化。

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

- 节点总数：22
- 触发方式：Chat 消息触发

## 触发方式
- When Executed by Another Workflow 触发
- When chat message received 触发

## 统计
- 节点总数：22
- 触发节点：2
- 处理节点：13
- 输出节点：7
- 分类：workflow-automation
