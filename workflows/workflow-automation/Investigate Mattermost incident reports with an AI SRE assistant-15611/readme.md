## 简介
**Investigate Mattermost incident reports with an AI SRE assistant**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/15611

---

# Investigate Mattermost incident reports with an AI SRE assistant


## 节点清单

| 节点 | 类型 |
|------|------|
| When Executed by Another Workflow | 执行工作流触发器 |
| AI Agent | AI Agent |
| OpenRouter Chat Model | OpenRouter Chat Model |
| Grafana | MCP 客户端 |
| DigitalOcean | MCP 客户端 |
| K8S | MCP 客户端 |
| Qdrant Vector Store | Qdrant 向量存储 |
| Embeddings Google Gemini | Google Gemini Embeddings |
| Github | MCP 客户端 |
| Post a message | Mattermost |
| ReadIncidentContext | Code |
| SetVars | 数据设置 |
| Mattermost | MCP 客户端 |
| Set: empty attachments | 数据设置 |
| Merge | 数据合并 |
| Call 'attachmentsAnalyzer' | 执行工作流 |



## 功能说明

Investigate Mattermost incident reports with an AI（AI 增强)手动或子流程调用，通过 Git 实现自动化。

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

- 节点总数：16
- 触发方式：手动或子流程调用

## 触发方式
- When Executed by Another Workflow 触发

## 统计
- 节点总数：16
- 触发节点：1
- 处理节点：14
- 输出节点：1
- 分类：workflow-automation
