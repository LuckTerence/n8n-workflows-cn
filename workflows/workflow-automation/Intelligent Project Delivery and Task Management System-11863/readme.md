## 简介
**Intelligent Project Delivery and Task Management System**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/11863

---

# Intelligent Project Delivery and Task Management System


## 节点清单

| 节点 | 类型 |
|------|------|
| Daily Project Check | 定时触发器 |
| Workflow Configuration | 数据设置 |
| Fetch Project Data | HTTP Request |
| Fetch Team Profiles | HTTP Request |
| Merge Project and Team Data | Code |
| Project Orchestrator Agent | AI Agent |
| Anthropic Model - Orchestrator | OpenAI Chat Model |
| Task Breakdown Output Parser | 结构化输出解析器 |
| Task Breakdown Agent Tool | agentTool |
| Anthropic Model - Task Breakdown | OpenAI Chat Model |
| Task List Parser | 结构化输出解析器 |
| Effort Estimation Agent Tool | agentTool |
| Anthropic Model - Effort Estimation | OpenAI Chat Model |
| Effort Estimates Parser | 结构化输出解析器 |
| Task Assignment Agent Tool | agentTool |
| Anthropic Model - Task Assignment | OpenAI Chat Model |
| Task Assignments Parser | 结构化输出解析器 |
| Progress Monitoring Tool | 代码工具 |
| Delay Detection Tool | 代码工具 |
| Parse Agent Output | Code |
| Check for Delays | IF 判断 |
| Reallocation Agent | AI Agent |
| Anthropic Model - Reallocation | OpenAI Chat Model |
| Reallocation Output Parser | 结构化输出解析器 |
| Update Task Assignments | HTTP Request |
| Generate Milestone Report | Code |
| Send Report Notification | HTTP Request |



## 功能说明

Intelligent Project Delivery and Task Management S（AI 增强)定时触发，通过 HTTP API 实现自动化。

定时触发，通过 HTTP API 实现自动化。

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

- 节点总数：27
- 触发方式：定时触发

## 触发方式
- Daily Project Check 触发

## 统计
- 节点总数：27
- 触发节点：1
- 处理节点：22
- 输出节点：4
- 分类：workflow-automation
