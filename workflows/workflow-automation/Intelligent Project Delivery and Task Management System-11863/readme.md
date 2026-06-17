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

## 触发方式
- Daily Project Check 触发

## 统计
- 节点总数：27
- 触发节点：1
- 处理节点：22
- 输出节点：4
- 分类：workflow-automation
