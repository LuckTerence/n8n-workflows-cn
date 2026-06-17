# Build an IT Support Assistant Chatbot Leveraging Existing Support Portal

https://n8nworkflows.xyz/workflows/3498

## 节点清单

| 节点 | 类型 |
|------|------|
| When chat message received | Chat 触发器 |
| OpenAI Chat Model | OpenAI Chat Model |
| Simple Memory | 记忆缓冲区 |
| Acuity Support Search API | HTTP Request |
| Extract Relevant Fields | 数据设置 |
| Results to Items | 数据拆分 |
| Has Results? | IF 判断 |
| Empty Response | 数据设置 |
| Aggregate Response | 数据聚合 |
| Knowledgebase Tool | 工作流工具 |
| AcuityScheduling Support Chatbot | AI Agent |
| KnowledgeBase Tool Subworkflow | 执行工作流触发器 |

## 触发方式
- When chat message received 触发
- KnowledgeBase Tool Subworkflow 触发

## 统计
- 节点总数：12
- 触发节点：2
- 处理节点：9
- 输出节点：1
- 分类：ai-agent
