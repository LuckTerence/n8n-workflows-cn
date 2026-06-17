## 简介
**Create Viral Multimedia Ads with AI: NanoBanana, Seedance & Suno for Social Media**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/8428

---

# Create Viral Multimedia Ads with AI: NanoBanana, Seedance & Suno for Social Media


## 节点清单

| 节点 | 类型 |
|------|------|
| Telegram: Get Image File | Telegram |
| Google Drive: Upload Image | Google Drive |
| LLM: Structured Output Parser | 结构化输出解析器 |
| LLM: OpenAI Chat | OpenAI Chat Model |
| Generate Image Prompt | AI Agent |
| NanoBanana: Create Image | HTTP Request |
| Wait for Image Edit | 等待 |
| Download Edited Image | HTTP Request |
| Wait for Rendering | 等待 |
| Download Video from Seedance | HTTP Request |
| Send Video URL via Telegram | Telegram |
| Send Final Video Preview | Telegram |
| Telegram: Send notification | Telegram |
| Trigger: Receive Idea via Telegram | Telegram 触发器 |
| Parse Idea Into Prompts | Code |
| Rewrite Caption (TikTok/Instagram) | OpenAI |
| Post Image to Instagram + X | uploadPost |
| Seedance: Generate Video from Image | HTTP Request |
| Set: Video URL | 数据设置 |
| Suno: Generate Music | HTTP Request |
| Set: Audio URL | 数据设置 |
| Download Music File | HTTP Request |
| Wait: Music Rendering | 等待 |
| Merge Audio + Video | HTTP Request |
| Wait: Merge Process | 等待 |
| Check Merge Status | HTTP Request |
| If Merge Completed | IF 判断 |
| Download Final Video | HTTP Request |
| Check Merge Status II | HTTP Request |
| Upload Final Video to Google Drive | Google Drive |
| Read Brand Settings | Google Sheets |
| Extract Brand Info | Code |
| Ads Copywriter Generator (AI) | OpenAI |
| Save Ad Data to Google Sheets | Google Sheets |
| Post Video on Social Media (FB, TikTok, YT) | uploadPost |
| Save Publishing Status to Google Sheets | Google Sheets |
| Think | 思考工具 |

## 触发方式
- Trigger: Receive Idea via Telegram 触发

## 统计
- 节点总数：37
- 触发节点：1
- 处理节点：22
- 输出节点：14
- 分类：workflow-automation
