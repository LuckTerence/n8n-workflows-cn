## 简介
**Business Model Canvas AI-Powered Generator (LLM Flexible)**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3663

---

# Business Model Canvas AI-Powered Generator (LLM Flexible)


## 节点清单

| 节点 | 类型 |
|------|------|
| When chat message received | Chat 触发器 |
| Key Partners Generator | AI Agent |
| Key Activities Generator | AI Agent |
| Value Proposition Generator | AI Agent |
| Customer Relationship Generator | AI Agent |
| Customer Segments Generator | AI Agent |
| Ollama Chat Model | Ollama Chat Model |
| Key Resources Generator | AI Agent |
| Channels Generator | AI Agent |
| Cost Structure Generator | AI Agent |
| Title Generator | AI Agent |
| Revenue Streams Generator | AI Agent |
| Key Partners HTML Transformer | Code |
| Key Activities HTML Transformer | Code |
| Values proposition HTML Transformer | Code |
| Customer Relationship HTML Transformer | Code |
| Customer Segments HTML Transformer | Code |
| Key Resources HTML Transformer | Code |
| Channels HTML Transformer | Code |
| Revenue streams HTML Transformer | Code |
| Code1 | Code |
| Cost Structure HTML Transformer | Code |
| Turn to HTML | Code |
| HTML code to HTML file | 转换为文件 |
| Merge All Data | 数据合并 |



## 功能说明

Business Model Canvas AI-Powered Generator (LLM Fl（AI 增强)Chat 消息触发，通过 n8n 内置节点实现自动化。

Chat 消息触发，通过 工作流编排 实现自动化。

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

- 节点总数：25
- 触发方式：Chat 消息触发

## 触发方式
- When chat message received 触发

## 统计
- 节点总数：25
- 触发节点：1
- 处理节点：24
- 输出节点：0
- 分类：workflow-automation
