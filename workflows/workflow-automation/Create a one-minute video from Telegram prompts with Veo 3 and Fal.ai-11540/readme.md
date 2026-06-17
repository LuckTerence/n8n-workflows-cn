## 简介
**Create a one-minute video from Telegram prompts with Veo 3 and Fal.ai**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/11540

---

# Create a one-minute video from Telegram prompts with Veo 3 and Fal.ai


## 节点清单

| 节点 | 类型 |
|------|------|
| Generate a video1 | OpenAI Chat Model |
| Telegram Trigger | Telegram 触发器 |
| Generate a video2 | OpenAI Chat Model |
| HTTP Request | HTTP Request |
| HTTP Request1 | HTTP Request |
| If | IF 判断 |
| HTTP Request2 | HTTP Request |
| Send a video | Telegram |
| Upload video1 | Google Drive |
| Label URL 1 | 数据设置 |
| Label URL 2 | 数据设置 |
| Merge | 数据合并 |
| Wait | 等待 |
| Generate a video3 | OpenAI Chat Model |
| Label URL 3 | 数据设置 |
| Upload video4 | Google Drive |
| Label URL 4 | 数据设置 |
| Generate a video4 | OpenAI Chat Model |
| Upload video5 | Google Drive |
| Label URL 5 | 数据设置 |
| Generate a video5 | OpenAI Chat Model |
| Upload video | Google Drive |
| Upload video3 | Google Drive |
| Upload video6 | Google Drive |
| Generate a video | OpenAI Chat Model |
| Label URL 6 | 数据设置 |
| Label URL 7 | 数据设置 |
| Upload video7 | Google Drive |
| Generate a video6 | OpenAI Chat Model |
| Wait3 | 等待 |
| Wait5 | 等待 |
| Wait4 | 等待 |
| Send a text message | Telegram |
| Send a text message2 | Telegram |
| Send a text message3 | Telegram |
| Send a text message4 | Telegram |
| Send a text message5 | Telegram |
| Send a text message6 | Telegram |
| Send a text message7 | Telegram |
| Send a text message8 | Telegram |
| AI Agent | AI Agent |
| Structured Output Parser | 结构化输出解析器 |
| OpenAI Chat Model | OpenAI Chat Model |
| If1 | IF 判断 |
| Save to Google Sheets | Google Sheets |
| Send message and wait for response | Telegram |

## 触发方式
- Telegram Trigger 触发

## 统计
- 节点总数：46
- 触发节点：1
- 处理节点：32
- 输出节点：13
- 分类：workflow-automation
