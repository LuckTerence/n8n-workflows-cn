## 简介
**Investigate CI-CD incidents in Mattermost with an AI agent**

（待补充中文描述）

> 分类：AI Agent | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/15610

---

# Investigate CI-CD incidents in Mattermost with an AI agent


## 节点清单

| 节点 | 类型 |
|------|------|
| When Executed by Another Workflow | 执行工作流触发器 |
| SetVars | 数据设置 |
| AI Agent | AI Agent |
| OpenRouter Chat Model | OpenRouter Chat Model |
| Github | MCP 客户端 |
| Grafana | MCP 客户端 |
| probe_url | 工作流工具 |
| k8s | MCP 客户端 |
| Mattermost | MCP 客户端 |
| Validate Output | Code |
| Post a message | Mattermost |
| Set: empty attachments | 数据设置 |
| Merge | 数据合并 |
| ReadIncidentContext | Code |
| attachmentsAnalyzer | 执行工作流 |



## 功能说明

Investigate CI-CD incidents in Mattermost with an （AI 增强)手动或子流程调用，通过 Git 实现自动化。

手动触发，通过 Git 实现自动化。

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

- 节点总数：15
- 触发方式：手动或子流程调用

## 触发方式
- When Executed by Another Workflow 触发

## 统计
- 节点总数：15
- 触发节点：1
- 处理节点：13
- 输出节点：1
- 分类：ai-agent
