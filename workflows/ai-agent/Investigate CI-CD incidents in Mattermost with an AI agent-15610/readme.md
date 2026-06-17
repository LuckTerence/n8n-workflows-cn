# Investigate CI-CD incidents in Mattermost with an AI agent

https://n8nworkflows.xyz/workflows/15610

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

## 触发方式
- When Executed by Another Workflow 触发

## 统计
- 节点总数：15
- 触发节点：1
- 处理节点：13
- 输出节点：1
- 分类：ai-agent
