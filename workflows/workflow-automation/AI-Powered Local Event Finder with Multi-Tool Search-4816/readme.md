## 简介
**AI-Powered Local Event Finder with Multi-Tool Search**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4816

---

# AI-Powered Local Event Finder with Multi-Tool Search


## 节点清单

| 节点 | 类型 |
|------|------|
| Google Gemini Chat Model | OpenAI Chat Model |
| Simple Memory | 记忆缓冲区 |
| brave_web_search | MCP 客户端 |
| brave_local_search | MCP 客户端 |
| find_events | 工作流工具 |
| even_finder_workflow | 执行工作流触发器 |
| event_finder_agent | AI Agent |
| local_event_finder | MCP 触发器 |
| google_gemini_event_search | geminiSearchToolTool |
| jina_ai_web_page_scraper | jinaAiTool |



## 功能说明

联网搜索工具，AI 驱动的信息检索和分析。

手动触发，通过 工作流编排 实现自动化。

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

- 节点总数：10
- 触发方式：手动或子流程调用

## 触发方式
- even_finder_workflow 触发
- local_event_finder 触发

## 统计
- 节点总数：10
- 触发节点：2
- 处理节点：8
- 输出节点：0
- 分类：workflow-automation
