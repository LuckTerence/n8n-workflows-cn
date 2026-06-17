# Dynamically switch between LLMs for AI Agents using LangChain Code

https://n8nworkflows.xyz/workflows/3820

## 节点清单

| 节点 | 类型 |
|------|------|
| When chat message received | Chat 触发器 |
| Switch Model | Code |
| Set LLM index | 数据设置 |
| Increase LLM index | 数据设置 |
| No Operation, do nothing | 空操作 |
| Check for expected error | IF 判断 |
| Loop finished without results | 数据设置 |
| Unexpected error | 数据设置 |
| Return result | 数据设置 |
| OpenAI 4o-mini | OpenAI Chat Model |
| OpenAI 4o | OpenAI Chat Model |
| OpenAI o1 | OpenAI Chat Model |
| OpenAI Chat Model | OpenAI Chat Model |
| Validate response | sentimentAnalysis |
| Generate response | LLM Chain |

## 触发方式
- When chat message received 触发

## 统计
- 节点总数：15
- 触发节点：1
- 处理节点：14
- 输出节点：0
- 分类：ai-agent
