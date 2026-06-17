## 简介
**Automate RSS-to-Social Media with AI Summaries and Image Generation**

（待补充中文描述）

> 分类：多模态 AI | 适配等级：A-adapted（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/9208

---

# Automate RSS-to-Social Media with AI Summaries and Image Generation


## 节点清单

| 节点 | 类型 |
|------|------|
| RSS Feed Trigger | rssFeedReadTrigger |
| Get row(s) in sheet | Google Sheets |
| If | IF 判断 |
| HTTP Request | HTTP Request |
| HTML | HTML |
| Basic LLM Chain | LLM Chain |
| Append row in sheet | Google Sheets |
| Post to Instagram | HTTP Request |
| Post to Instagram1 | HTTP Request |
| Get Post URL | HTTP Request |
| Send a photo message | Telegram |
| Basic LLM Chain1 | LLM Chain |
| Anthropic Chat Model | OpenAI Chat Model |
| Google Gemini Chat Model | OpenAI Chat Model |
| Post to Facebook | HTTP Request |
| Merge | 数据合并 |
| Send a text message | Telegram |
| Generate an image | OpenAI |
| Edit Fields | 数据设置 |
| Upload to Supabase (uses credentials) | HTTP Request |
| Supabase Config | 数据设置 |
| Supabase Public URL | 数据设置 |
| Build Facebook URL | Code |
| Build Instagram URL | Code |
| Collect Important Data | Code |

## 触发方式
- RSS Feed Trigger 触发

## 统计
- 节点总数：25
- 触发节点：1
- 处理节点：16
- 输出节点：8
- 分类：multimodal-ai
