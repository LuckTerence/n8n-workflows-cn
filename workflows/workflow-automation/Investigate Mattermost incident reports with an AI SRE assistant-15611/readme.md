# Investigate Mattermost incident reports with an AI SRE assistant

https://n8nworkflows.xyz/workflows/15611

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

## 触发方式
- When Executed by Another Workflow 触发

## 统计
- 节点总数：16
- 触发节点：1
- 处理节点：14
- 输出节点：1
- 分类：workflow-automation
