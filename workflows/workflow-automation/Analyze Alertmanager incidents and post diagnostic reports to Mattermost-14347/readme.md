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

## 触发方式
- Receive alerts 触发

## 统计
- 节点总数：14
- 触发节点：1
- 处理节点：11
- 输出节点：2
- 分类：workflow-automation
