## 简介
**Deep Research - Sales Lead Magnet Agent**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Docs/Google Drive)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4721

---

# Deep Research - Sales Lead Magnet Agent


## 节点清单

| 节点 | 类型 |
|------|------|
| Query Builder | AI Agent |
| Structured Output Parser | 结构化输出解析器 |
| Research Leader | AI Agent |
| Perplexity tool | 工作流工具 |
| Project Planner | AI Agent |
| Structured Output Parser1 | 结构化输出解析器 |
| Split Out | 数据拆分 |
| Team of Research Assistants | AI Agent |
| Merge | 数据合并 |
| Code | Code |
| Editor | AI Agent |
| Google Docs | Google Docs |
| When chat message received | Chat 触发器 |
| Trigify knowledge hub | HTTP 工具 |
| Anthropic Chat Model1 | OpenAI Chat Model |
| Share URL | 数据设置 |
| Google Drive | Google Drive |
| Google Docs1 | Google Docs |
| Trigify knowledge hub2 | HTTP 工具 |
| OpenRouter Chat Model1 | OpenRouter Chat Model |
| Anthropic Chat Model | OpenAI Chat Model |



## 功能说明

客户关系管理工具，自动管理销售线索和客户数据。

Chat 消息触发，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：21
- 触发方式：Chat 消息触发

## 触发方式
- When chat message received 触发

## 统计
- 节点总数：21
- 触发节点：1
- 处理节点：18
- 输出节点：2
- 分类：workflow-automation
