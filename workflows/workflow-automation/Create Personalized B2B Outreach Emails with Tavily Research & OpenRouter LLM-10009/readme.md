# Create Personalized B2B Outreach Emails with Tavily Research & OpenRouter LLM

https://n8nworkflows.xyz/workflows/10009

## 节点清单

| 节点 | 类型 |
|------|------|
| Add Lead to Instantly AI | HTTP Request |
| Add Company Info to Google Sheet | Google Sheets |
| Structured Output Parser1 | 结构化输出解析器 |
| Generate Outreach Message | LLM Chain |
| Company Research | AI Agent |
| Tavily | tavilyTool |
| OpenRouter Chat Model2 | OpenRouter Chat Model |
| OpenRouter Chat Model3 | OpenRouter Chat Model |
| Loop Over Items | 分批处理 |
| When clicking ‘Execute workflow’ | 手动触发 |
| Limit(Test) | 数据限制 |
| Get Business card data extraction | Google Sheets |

## 触发方式
- When clicking ‘Execute workflow’ 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：10
- 输出节点：1
- 分类：workflow-automation
