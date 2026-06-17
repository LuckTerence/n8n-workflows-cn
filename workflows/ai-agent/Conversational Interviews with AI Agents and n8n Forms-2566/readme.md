## 简介
**Conversational Interviews with AI Agents and n8n Forms**

（待补充中文描述）

> 分类：AI Agent | 适配等级：A（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2566

---

# Conversational Interviews with AI Agents and n8n Forms


## 节点清单

| 节点 | 类型 |
|------|------|
| Stop Interview? | IF 判断 |
| Generate Row | 数据设置 |
| Generate Row1 | 数据设置 |
| Clear For Next Interview | memoryManager |
| Send Reply To Agent | 数据设置 |
| Start Interview | 表单触发器 |
| Get Answer | 表单 |
| Set Interview Topic | 数据设置 |
| UUID | 加密 |
| Generate Row2 | 数据设置 |
| Create Session | Redis |
| Update Session | Redis |
| Update Session1 | Redis |
| Update Session2 | Redis |
| Valid Session? | IF 判断 |
| Respond to Webhook | 响应 Webhook |
| Window Buffer Memory2 | 记忆缓冲区 |
| Window Buffer Memory | 记忆缓冲区 |
| Redirect to Completion Screen | 表单 |
| Webhook | Webhook |
| 404 Not Found | HTML |
| AI Researcher | AI Agent |
| Parse Response | 数据设置 |
| Groq Chat Model | Groq Chat Model |
| Show Transcript | HTML |
| Save to Google Sheet | Google Sheets |
| Session to List | 数据拆分 |
| Messages To JSON | 数据设置 |
| Query By Session | Redis |
| Get Session | Redis |

## 触发方式
- Start Interview 触发
- Webhook 触发

## 统计
- 节点总数：30
- 触发节点：2
- 处理节点：27
- 输出节点：1
- 分类：ai-agent
