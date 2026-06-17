## 简介
**Automate Lead Generation with Apollo, AI Parsing, and Timed Email Follow-ups**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Zoom/Gmail/Google Sheets/Stripe/Slack)（基本改完，配置 API Key 应该就能跑）
> 节点数：33 | 难度：⭐⭐⭐ 高级
> 原始来源：https://n8nworkflows.xyz/workflows/9034

---

# Automate Lead Generation with Apollo, AI Parsing, and Timed Email Follow-ups


## 节点清单

| 节点 | 类型 |
|------|------|
| Wait | 等待 |
| Get row(s) in sheet | Google Sheets |
| AI Agent | AI Agent |
| OpenAI Chat Model | OpenAI Chat Model |
| Send a message | Email 发送 |
| Update row in sheet | Google Sheets |
| Limit | 数据限制 |
| Add to Google Sheet1 | Google Sheets |
| Parse Lead Data1 | LLM Chain |
| OpenAI Chat Model3 | OpenAI Chat Model |
| Structured Output Parser1 | 结构化输出解析器 |
| When clicking ‘Execute workflow’ | 手动触发 |
| Add to Google Sheet | Google Sheets |
| On form submission | 表单触发器 |
| Apollo URL Generator | LLM Chain |
| Run Apify | HTTP Request |
| OpenAI Chat Model1 | OpenAI Chat Model |
| Structured Output Parser | 结构化输出解析器 |
| Parse Lead Data | LLM Chain |
| OpenAI Chat Model2 | OpenAI Chat Model |
| Schedule Trigger | 定时触发器 |
| Wait1 | 等待 |
| Get row(s) in sheet1 | Google Sheets |
| AI Agent1 | AI Agent |
| Send a message1 | Email 发送 |
| Update row in sheet1 | Google Sheets |
| Schedule Trigger1 | 定时触发器 |
| OpenAI Chat Model4 | OpenAI Chat Model |
| If1 | IF 判断 |
| Get row(s) in sheet2 | Google Sheets |
| If | IF 判断 |
| Loop Over Items | 分批处理 |
| If2 | IF 判断 |
| Delay generator | Code |
| Time checker | Code |
| Delay generator1 | Code |
| proper json | Code |

## 触发方式
- When clicking ‘Execute workflow’ 触发
- On form submission 触发
- Schedule Trigger 触发
- Schedule Trigger1 触发

## 统计
- 节点总数：37
- 触发节点：4
- 处理节点：30
- 输出节点：3
- 分类：workflow-automation
