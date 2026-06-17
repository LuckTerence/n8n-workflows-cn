# Generate Fact-Checked Research Reports with Llama AI and Web Search

https://n8nworkflows.xyz/workflows/11116

## 节点清单

| 节点 | 类型 |
|------|------|
| Form Trigger | 表单触发器 |
| Parse Form Input | Code |
| Research Agent - Plan | HTTP Request |
| Extract Search Queries | Code |
| SERP Search | HTTP Request |
| Merge Research | 数据合并 |
| Aggregate Research | Code |
| Merge All Agents | 数据合并 |
| Return Results | 响应 Webhook |
| Groq Chat Model | Groq Chat Model |
| Fact-Checker Agent | LLM Chain |
| Editor Agent | LLM Chain |
| PM Agent - Final Review1 | LLM Chain |
| Code | Code |
| Writer Agent | LLM Chain |

## 触发方式
- Form Trigger 触发

## 统计
- 节点总数：15
- 触发节点：1
- 处理节点：11
- 输出节点：3
- 分类：workflow-automation
