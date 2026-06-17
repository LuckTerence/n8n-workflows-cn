## 简介
**AI Real Estate Agent: End-to-End Ops Automation (Web, Data, Voice)**

（待补充中文描述）

> 分类：多模态 AI | 适配等级：B（需替换Twilio/Google Sheets/Google Docs)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4368

---

# AI Real Estate Agent: End-to-End Ops Automation (Web, Data, Voice)


## 节点清单

| 节点 | 类型 |
|------|------|
| IncomingLeadWebhook | Webhook |
| RenameInputFields | 数据设置 |
| ValidateMessageExists | IF 判断 |
| CleanUserText | Code |
| ClassifyIntentUrgency | AI Agent |
| ExtractClassification | 数据设置 |
| StandardizeFields | Code |
| PropertyCheckAPI | HTTP Request |
| IsKnownListing | IF 判断 |
| CalculateLeadScore | Code |
| CreateStructuredLeadObject | 数据设置 |
| OpenAI Chat Model | OpenAI Chat Model |
| When clicking ‘Test workflow’ | 手动触发 |
| Schedule Trigger | 定时触发器 |
| HTTP Request | HTTP Request |
| Information Extractor | 信息提取器 |
| Split Out | 数据拆分 |
| Real Estate Data | Google Sheets |
| AI Agent | AI Agent |
| OpenAI Chat Model1 | OpenAI Chat Model |
| Calculator | 计算器工具 |
| SerpAPI | SerpApi 工具 |
| Google Docs | Google Docs |
| OpenAI | OpenAI |
| OpenAI1 | OpenAI |
| OpenAI Chat Model2 | OpenAI Chat Model |
| Set Lead Variables | 数据设置 |
| Generate Intro Message | Function |
| ElevenLabs - Generate Voice | HTTP Request |
| Twilio - Place Call | HTTP Request |
| AI Agent - Extract Lead Info | AI Agent |
| Store Extracted Values | Function |
| Normalize User Data | 数据设置 |
| IF Lead Interested | IF 判断 |
| Assign Lead Score | Function |
| Format Timestamp | 日期时间 |
| Google Sheets - Log Lead | Google Sheets |
| AI Agent - Lead Summary | AI Agent |
| Google Sheets - Log Summary | Google Sheets |
| Webhook - New Lead1 | Webhook |
| OpenAI Chat Model3 | OpenAI Chat Model |
| OpenAI Chat Model4 | OpenAI Chat Model |

## 触发方式
- IncomingLeadWebhook 触发
- When clicking ‘Test workflow’ 触发
- Schedule Trigger 触发
- Webhook - New Lead1 触发

## 统计
- 节点总数：42
- 触发节点：4
- 处理节点：34
- 输出节点：4
- 分类：multimodal-ai
