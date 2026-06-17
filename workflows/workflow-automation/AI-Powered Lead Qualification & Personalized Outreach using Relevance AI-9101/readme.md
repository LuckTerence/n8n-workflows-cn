# AI-Powered Lead Qualification & Personalized Outreach using Relevance AI

https://n8nworkflows.xyz/workflows/9101

## 节点清单

| 节点 | 类型 |
|------|------|
| Form | 表单触发器 |
| Router | Switch 路由 |
| Edit Fields | 数据设置 |
| score individual (Relevance) | HTTP Request |
| score company (Relevance) | HTTP Request |
| Summarize_N_score | LLM Chain |
| Structured Output | Code |
| Deepseek | OpenRouter Chat Model |
| Gemini | OpenAI Chat Model |
| Deepseek R1 | OpenRouter Chat Model |
| Structured Output Parser | 结构化输出解析器 |
| Email Personalizer (HOT) | LLM Chain |
| Email Personalizer (WARM) | LLM Chain |
| Email Personalizer (COLD) | LLM Chain |
| Create a draft | Email 发送 |
| Update CRM | Google Sheets |
| Notify team | Slack |
| Set data | 数据设置 |
| Merge data | 数据合并 |
| Send email | Email 发送 |
| Merge data+mail | 数据合并 |

## 触发方式
- Form 触发

## 统计
- 节点总数：21
- 触发节点：1
- 处理节点：15
- 输出节点：5
- 分类：workflow-automation
