# Route and analyze customer feedback with Qwen3-VL, Tally, PostgreSQL

https://n8nworkflows.xyz/workflows/13314

## 节点清单

| 节点 | 类型 |
|------|------|
| Tally Trigger | tallyTrigger |
| Field Mapping | 数据设置 |
| Sentiment Analysis | LLM Chain |
| If | IF 判断 |
| Fetch Image | HTTP Request |
| Routing LLM | OpenAI Chat Model |
| #general-inquiries | 数据设置 |
| #happy-customers | 数据设置 |
| Decision Logic | LLM Chain |
| Send Discord Notification | Discord |
| Sentiment LLM | OpenAI Chat Model |
| Sentiment Parser | 结构化输出解析器 |
| Text Classification | LLM Chain |
| Classification LLM | OpenAI Chat Model |
| Classification Parser | 结构化输出解析器 |
| Image Keyword Extraction | Code |
| Empty Keywords Handler | 数据设置 |
| Image Results Merge | 数据合并 |
| AI Results Merge | 数据合并 |
| Data Aggregation | 数据聚合 |
| Save to PostgreSQL | PostgreSQL |
| Route Parser | 结构化输出解析器 |
| Channel Router | Switch 路由 |
| #support-urgent | 数据设置 |
| Build Discord Message | 数据合并 |
| Format Embed Data | Code |

## 触发方式
- Tally Trigger 触发

## 统计
- 节点总数：26
- 触发节点：1
- 处理节点：23
- 输出节点：2
- 分类：workflow-automation
