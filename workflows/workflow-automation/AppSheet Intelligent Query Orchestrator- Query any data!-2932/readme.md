## 简介
**AppSheet Intelligent Query Orchestrator- Query any data!**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2932

---

# AppSheet Intelligent Query Orchestrator- Query any data!


## 节点清单

| 节点 | 类型 |
|------|------|
| Structured Output Parser | 结构化输出解析器 |
| Limit | 数据限制 |
| AppSheet | appSheet |
| Aggregate | 数据聚合 |
| AggregateRanked | 数据设置 |
| Final Reranked Output | 数据设置 |
| Cohere Rerank | HTTP Request |
| Google Gemini Chat Model | OpenAI Chat Model |
| GetListOfWorksheets | Google Sheets 工具 |
| GetHeaders | Google Sheets 工具 |
| CallAppsheetAPI | 工作流工具 |
| Appsheet Schema Analyser | AI Agent |
| Anthropic Chat Model | OpenAI Chat Model |
| When Executed by Another Workflow | 执行工作流触发器 |
| When chat message received | Chat 触发器 |
| Cleanup and structure the input | LLM Chain |

## 触发方式
- When Executed by Another Workflow 触发
- When chat message received 触发

## 统计
- 节点总数：16
- 触发节点：2
- 处理节点：13
- 输出节点：1
- 分类：workflow-automation
