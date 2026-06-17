## 简介
**AI新闻研究团队**

24小时AI自动化新闻简报

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Gmail)（AI模型已替换为DeepSeek，部分边角节点可能仍需手动调整）
> 原始来源：https://n8nworkflows.xyz/workflows/2778

---

# AI新闻研究团队


## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Trigger | 定时触发器 |
| Markdown | Markdown |
| Title | LLM Chain |
| News Reporter | AI Agent |
| Execute Workflow Trigger | 执行工作流触发器 |
| Response | 数据设置 |
| Perplexity API | HTTP Request |
| Perplexity_tool | 工作流工具 |
| OpenAI Chat Model | OpenAI Chat Model |
| OpenAI Chat Model1 | OpenAI Chat Model |
| Settings | 数据设置 |
| Merge chapters title and text | 数据合并 |
| Final article text | Code |
| Research Leader 🔬 | AI Agent |
| Structured Output Parser | 结构化输出解析器 |
| Delegate to Research Assistants | 数据拆分 |
| Research Assistant | AI Agent |
| Project Planner | AI Agent |
| OpenAI Chat Model4 | OpenAI Chat Model |
| OpenAI Chat Model5 | OpenAI Chat Model |
| OpenAI Chat Model6 | OpenAI Chat Model |
| OpenAI Chat Model2 | OpenAI Chat Model |
| Title1 | LLM Chain |
| Gmail1 | Gmail |
| Switch | Switch 路由 |
| Editor | AI Agent |
| Gmail2 | Gmail |
| Perplexity_tool2 | 工作流工具 |
| Perplexity_tool1 | 工作流工具 |
| News to Monitor | Google Sheets |
| Loop Over Items | 分批处理 |



## 功能说明

内容管理工具，自动生成或发布内容，定时执行。

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

- 节点总数：31
- 触发方式：定时触发

## 触发方式
- Schedule Trigger 触发
- Execute Workflow Trigger 触发

## 统计
- 节点总数：31
- 触发节点：2
- 处理节点：28
- 输出节点：1
- 分类：workflow-automation
