## 简介
**Analyze Alertmanager incidents and post diagnostic reports to Mattermost**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/14347

---

# Analyze Alertmanager incidents and post diagnostic reports to Mattermost


## 节点清单

| 节点 | 类型 |
|------|------|
| AI Agent | AI Agent |
| OpenAI Chat Model | OpenAI Chat Model |
| Qdrant Vector Store | Qdrant 向量存储 |
| Embeddings Google Gemini | Google Gemini Embeddings |
| K8S mcp | MCP 客户端 |
| Grafana mcp | MCP 客户端 |
| Digitalocean MCP | MCP 客户端 |
| Github MCP | MCP 客户端 |
| Receive alerts | Webhook |
| GetAlertMessages | HTTP Request |
| Post in thread | Mattermost |
| PreProcessAlerts | Code |
| FindAlert | Code |
| SetVars | 数据设置 |



## 功能说明

监控告警系统，异常检测并发送通知，Webhook 触发。

Webhook触发，通过 Git + HTTP API 实现自动化。

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

- 节点总数：14
- 触发方式：Webhook 触发

## 触发方式
- Receive alerts 触发

## 统计
- 节点总数：14
- 触发节点：1
- 处理节点：11
- 输出节点：2
- 分类：workflow-automation
