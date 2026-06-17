## 简介
**Generate AI viral videos with NanoBanana & VEO3, shared on socials via Blotato**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Notion/Google Sheets/Google Drive)（基本改完，配置 API Key 应该就能跑）
> 节点数：40 | 难度：⭐⭐⭐ 高级
> 原始来源：https://n8nworkflows.xyz/workflows/8270

---

# Generate AI viral videos with NanoBanana & VEO3, shared on socials via Blotato


## 节点清单

| 节点 | 类型 |
|------|------|
| Upload Video to BLOTATO | Blotato |
| Youtube | Blotato |
| Tiktok | Blotato |
| Merge | 数据合并 |
| Update Status to "DONE" | Google Sheets |
| Linkedin | Blotato |
| Facebook | Blotato |
| Instagram | Blotato |
| Threads | Blotato |
| Bluesky | Blotato |
| Pinterest | Blotato |
| Twitter (X) | Blotato |
| OpenAI Chat Model | OpenAI Chat Model |
| Think | 思考工具 |
| Structured Output Parser | 结构化输出解析器 |
| Send Video URL via Telegram | Telegram |
| Send Final Video Preview | Telegram |
| Telegram Trigger: Receive Video Idea | Telegram 触发器 |
| Set Master Prompt | 数据设置 |
| AI Agent: Generate Video Script | AI Agent |
| Generate Video with VEO3 | HTTP Request |
| Wait for VEO3 Rendering | 等待 |
| Download Video from VEO3 | HTTP Request |
| Rewrite Caption with GPT-4o | OpenAI |
| Save Caption Video to Google Sheets | Google Sheets |
| Format Prompt | Code |
| Telegram: Get Image File | Telegram |
| Google Drive: Upload Image | Google Drive |
| Google Sheets: Log Image & Caption | Google Sheets |
| Set: Bot Token (Placeholder) | 数据设置 |
| Telegram API: Get File URL | HTTP Request |
| OpenAI Vision: Analyze Reference Image | OpenAI |
| Google Sheets: Update Image Description | Google Sheets |
| LLM: Structured Output Parser | 结构化输出解析器 |
| LLM: OpenAI Chat | OpenAI Chat Model |
| Generate Image Prompt | AI Agent |
| NanoBanana: Create Image | HTTP Request |
| Wait for Image Edit | 等待 |
| Download Edited Image | HTTP Request |
| Google Sheets: Read Video Parameters (CONFIG) | Google Sheets |
| Telegram: Send notification | Telegram |

## 触发方式
- Telegram Trigger: Receive Video Idea 触发

## 统计
- 节点总数：41
- 触发节点：1
- 处理节点：31
- 输出节点：9
- 分类：workflow-automation
