## 简介
**Create AI Viral Videos using NanoBanana 2 PRO & VEO3.1 and Publish via Blotato**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：30 | 难度：⭐⭐⭐ 高级
> 原始来源：https://n8nworkflows.xyz/workflows/11204

---

# Create AI Viral Videos using NanoBanana 2 PRO & VEO3.1 and Publish via Blotato


## 节点清单

| 节点 | 类型 |
|------|------|
| OpenAI Chat Model | OpenAI Chat Model |
| Think | 思考工具 |
| Structured Output Parser | 结构化输出解析器 |
| Telegram Trigger: Receive Video Idea | Telegram 触发器 |
| Set Master Prompt | 数据设置 |
| AI Agent: Generate Video Script | AI Agent |
| Set: Bot Token (Placeholder) | 数据设置 |
| Telegram API: Get File URL | HTTP Request |
| OpenAI Vision: Analyze Reference Image | OpenAI |
| LLM: Structured Output Parser | 结构化输出解析器 |
| LLM: OpenAI Chat | OpenAI Chat Model |
| Generate Image Prompt | AI Agent |
| NanoBanana: Create Image | HTTP Request |
| Wait for Image Edit | 等待 |
| Download Edited Image | HTTP Request |
| Parse GPT Response | Code |
| Optimize Prompt for Veo | 数据设置 |
| Download Video | HTTP Request |
| Prepare Veo Request Body | Code |
| Veo Generation | HTTP Request |
| Wait | 等待 |
| Send Video to Telegram | Telegram |
| Upload Video to BLOTATO | Blotato |
| Youtube | Blotato |
| Tiktok | Blotato |
| Linkedin | Blotato |
| Facebook | Blotato |
| Instagram | Blotato |
| Twitter (X) | Blotato |
| Merge1 | 数据合并 |
| Send a text message | Telegram |

## 触发方式
- Telegram Trigger: Receive Video Idea 触发

## 统计
- 节点总数：31
- 触发节点：1
- 处理节点：23
- 输出节点：7
- 分类：workflow-automation
