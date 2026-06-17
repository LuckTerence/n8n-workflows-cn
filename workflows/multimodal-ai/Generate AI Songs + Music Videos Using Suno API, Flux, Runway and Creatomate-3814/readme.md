## 简介
**Generate AI Songs + Music Videos Using Suno API, Flux, Runway and Creatomate**

（待补充中文描述）

> 分类：多模态 AI | 适配等级：A（需替换Google Sheets/Google Drive)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3814

---

# Generate AI Songs + Music Videos Using Suno API, Flux, Runway and Creatomate


## 节点清单

| 节点 | 类型 |
|------|------|
| OpenAI Chat Model | OpenAI Chat Model |
| Simple Memory | 记忆缓冲区 |
| OpenAI Chat Model1 | OpenAI Chat Model |
| Structured Output Parser | 结构化输出解析器 |
| Wait | 等待 |
| Rate Limit Wait Node | 等待 |
| Wait1 | 等待 |
| get_image_url1 | HTTP Request |
| Get Image | HTTP Request |
| Structured Output Parser1 | 结构化输出解析器 |
| Google Gemini Chat Model | OpenAI Chat Model |
| Wait2 | 等待 |
| get_image_url | HTTP Request |
| Get Image1 | HTTP Request |
| 1 minute | 等待 |
| Wait3 | 等待 |
| Merge | 数据合并 |
| Rate Limit Wait Node1 | 等待 |
| Track Ideas Agent Telegram Trigger | Telegram 触发器 |
| Switch Text or Voice Input | Switch 路由 |
| Download Voice Note | Telegram |
| Transcribe Voice Note | OpenAI |
| Set Field | 数据设置 |
| Set Field to "text" | 数据设置 |
| AI Music Agent | AI Agent |
| Append Music Tracks to GSheets | Google Sheets 工具 |
| Get Rows: Confirm Tracks in GSheets | Google Sheets 工具 |
| SerpAPI: Browse the internet for Music Ideas | SerpApi 工具 |
| Send Message to User | Telegram |
| Google Sheets Trigger: Start Processing Tracks | Google Sheets 触发器 |
| Get one Pending Row | Google Sheets |
| Lyrics AI Agent | AI Agent |
| Music Generation API Request | HTTP Request |
| Get Music Generation Status | HTTP Request |
| Confirm Generation Status | Switch 路由 |
| Download Audio Track | HTTP Request |
| Upload Audio Track to Drive | Google Drive |
| Update Audio URL in GSheet | Google Sheets |
| Cover Image and Video Prompts AI Agent | AI Agent |
| Generate Cover Image 1:1 | HTTP Request |
| Generate Cover Image 3:1 | HTTP Request |
| Upload Cover Image 1:1 to Drive | Google Drive |
| Upload to kraken to get url | HTTP Request |
| Convert Cover Image 3:1 to Video | HTTP Request |
| Get Video Generation Status | HTTP Request |
| Confirm Generation Status1 | Switch 路由 |
| Download Video | HTTP Request |
| Upload Converted Video to Drive | Google Drive |
| Update Cover Photo & Video URLs | Google Sheets |
| Send Status Updates on Telegram | Telegram |
| Render Video Trigger | Google Sheets 触发器 |
| Get Pending Render Row | Google Sheets |
| Render Audio Track + Video | HTTP Request |
| Send URL to GDrive Script and Upload | HTTP Request |
| Rename Uploaded Video | Google Drive |
| Update Music Video URL + Render Status | Google Sheets |
| Send Video URL to User | Telegram |



## 功能说明

AI 图像生成工作流，文生图或图生图。

Telegram 消息触发，通过 Telegram 通知 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com
- Telegram Bot Token → @BotFather 创建
- 通义万相 API Key → https://dashscope.aliyun.com

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：57
- 触发方式：Telegram 消息触发

## 触发方式
- Track Ideas Agent Telegram Trigger 触发
- Google Sheets Trigger: Start Processing Tracks 触发
- Render Video Trigger 触发

## 统计
- 节点总数：57
- 触发节点：3
- 处理节点：35
- 输出节点：19
- 分类：multimodal-ai
