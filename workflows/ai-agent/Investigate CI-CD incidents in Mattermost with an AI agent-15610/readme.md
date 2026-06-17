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

## 触发方式
- When Executed by Another Workflow 触发

## 统计
- 节点总数：15
- 触发节点：1
- 处理节点：13
- 输出节点：1
- 分类：ai-agent
