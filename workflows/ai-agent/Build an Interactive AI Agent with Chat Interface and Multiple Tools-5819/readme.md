# Build an Interactive AI Agent with Chat Interface and Multiple Tools

https://n8nworkflows.xyz/workflows/5819

## 节点清单

| 节点 | 类型 |
|------|------|
| Simple Memory | 记忆缓冲区 |
| Gemini | OpenAI Chat Model |
| OpenAI | OpenAI Chat Model |
| Example Chat Window | Chat 触发器 |
| Your First AI Agent | AI Agent |
| get_a_joke | HTTP Request 工具 |
| days_from_now | dateTimeTool |
| wikipedia | Wikipedia 工具 |
| create_password | cryptoTool |
| calculate_loan_payment | 代码工具 |
| n8n_blog_rss_feed | rssFeedReadTool |

## 触发方式
- Example Chat Window 触发
- n8n_blog_rss_feed 触发

## 统计
- 节点总数：11
- 触发节点：2
- 处理节点：8
- 输出节点：1
- 分类：ai-agent
