## 简介
**Real Estate Chatbot with AI Property Matching and Automated Calendar Scheduling**

（待补充中文描述）

> 分类：AI Agent | 适配等级：A（需替换Supabase/Gmail)（基本改完，配置 API Key 应该就能跑）
> 节点数：31 | 难度：⭐⭐⭐ 高级
> 原始来源：https://n8nworkflows.xyz/workflows/7250

---

# Real Estate Chatbot with AI Property Matching and Automated Calendar Scheduling


## 节点清单

| 节点 | 类型 |
|------|------|
| LLM conversation | AI Agent |
| PostgreSQL Memory | PostgreSQL 聊天记忆 |
| Parse Data | Code |
| Save Personal Info | PostgreSQL |
| Query Properties | PostgreSQL |
| Ready Check | IF 判断 |
| OpenAI Chat Model | OpenAI Chat Model |
| Format Results with AI | AI Agent |
| Format Response | 数据设置 |
| Send Formatted Response | 响应 Webhook |
| Webhook | Webhook |
| SerpAPI | SerpApi 工具 |
| update_Calendar | Google Calendar 工具 |
| OpenAI Chat Model1 | OpenAI Chat Model |
| Gmail1 | Gmail 工具 |
| AI Agent | AI Agent |
| Google Calendar | Google Calendar 工具 |
| Gmail Trigger | Gmail 触发器 |
| Google Calendar1 | Google Calendar 工具 |
| Gmail | Gmail 工具 |
| get_Calendar | Google Calendar 工具 |
| create_Calendar1 | Google Calendar 工具 |
| Human agent | Gmail 工具 |
| Code | Code |
| If | IF 判断 |
| Postgres | PostgreSQL |
| Code1 | Code |
| Get Property Media | PostgreSQL |
| construct_image_url | Code |
| Merge | 数据合并 |
| If1 | IF 判断 |
| OpenAI Chat Model3 | OpenAI Chat Model |

## 触发方式
- Webhook 触发
- Gmail Trigger 触发

## 统计
- 节点总数：32
- 触发节点：2
- 处理节点：29
- 输出节点：1
- 分类：ai-agent
