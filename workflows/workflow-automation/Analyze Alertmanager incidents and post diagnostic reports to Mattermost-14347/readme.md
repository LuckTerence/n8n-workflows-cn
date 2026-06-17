# Analyze Alertmanager incidents and post diagnostic reports to Mattermost

https://n8nworkflows.xyz/workflows/14347

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
