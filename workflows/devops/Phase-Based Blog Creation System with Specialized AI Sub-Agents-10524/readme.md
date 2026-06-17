## 简介
**Phase-Based Blog Creation System with Specialized AI Sub-Agents**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/10524

---

# Phase-Based Blog Creation System with Specialized AI Sub-Agents


## 节点清单

| 节点 | 类型 |
|------|------|
| Orchestrator | AI Agent |
| Call Headline Writer Agent | 工作流工具 |
| Call Hook Writer Agent | 工作流工具 |
| Call Intro Writer Agent | 工作流工具 |
| Call Outline Writer Agent | 工作流工具 |
| Call Blog Writer Agent | 工作流工具 |
| Simple Memory | 记忆缓冲区 |
| Call Final Draft Editor Agent | 工作流工具 |
| Call Sources and Quotes Agent | 工作流工具 |
| Return Output | 空操作 |
| Research w/ Perplexity | HTTP Request |
| Headlines Writer | AI Agent |
| Get Research | Google Sheets 工具 |
| Save Research | Google Sheets |
| Do Research | 工作流工具 |
| When Executed by Another Workflow | 执行工作流触发器 |
| Headlines Writer (Tool) | agentTool |
| Chat | Chat 触发器 |
| Slack Message Received | slackTrigger |
| Slack Message Response | Slack |
| Claude | OpenAI Chat Model |

## 触发方式
- When Executed by Another Workflow 触发
- Chat 触发
- Slack Message Received 触发

## 统计
- 节点总数：21
- 触发节点：3
- 处理节点：16
- 输出节点：2
- 分类：devops
