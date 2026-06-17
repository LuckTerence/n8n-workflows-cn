## 简介
**AI expense tracker: Telegram voice-photo-text to sheets**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：B（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/12006

---

# AI expense tracker: Telegram voice-photo-text to sheets


## 节点清单

| 节点 | 类型 |
|------|------|
| Google Sheets: Get Rows (Dedup lookup) | Google Sheets |
| IF (Is Duplicate?) | IF 判断 |
| Switch (Voice/Photo/Text) | Switch 路由 |
| Code (Restore Telegram Payload) | Code |
| Set (Text Context) | 数据设置 |
| Google Gemini Chat (Text → JSON) | OpenAI Chat Model |
| Code (Parse Gemini JSON) | Code |
| Code (Split expenses to items) | Code |
| Google Sheets → Append row(s) | Google Sheets |
| IF (Has expenses?) | IF 判断 |
| Set (Photo Context) | 数据设置 |
| Code (Pick Best Photo) | Code |
| Code (Normalize Gemini Image Output) | Code |
| Telegram → Send Error Message and wait for response | Telegram |
| Telegram → Send Final Message | Telegram |
| Google Gemini (Analyze Image) | OpenAI Chat Model |
| Set (Voice Context) | 数据设置 |
| Telegram → Get Voice File | Telegram |
| Telegram → Get Image File | Telegram |
| Google Gemini (Analyze Audio) | OpenAI Chat Model |
| Code (Normalize Gemini Audio Output) | Code |
| Code (Normalize Gemini Text Output) | Code |
| Switch (Command Router) | Switch 路由 |
| Code (Parse Budget Amount) | Code |
| IF (Budget ok?) | IF 判断 |
| Telegram → Budget Error | Telegram |
| Google Sheets → Append or update row in sheet | Google Sheets |
| Telegram → Budget Updated | Telegram |
| GS - Get Daily Report Range | Google Sheets |
| Code - Build Daily Report | Code |
| TG - Send Daily Report | Telegram |
| Code (Schedule Report Token) | Code |
| Telegram Trigger | Telegram 触发器 |
| Code - Check Latest Token | Code |
| If | IF 判断 |
| ReportTokens | 数据表 |
| Data table → Get row(s) | 数据表 |
| Data table → Delete row(s) | 数据表 |
| Wait | 等待 |
| CONFIG - User Settings | 数据设置 |

## 触发方式
- Telegram Trigger 触发

## 统计
- 节点总数：40
- 触发节点：1
- 处理节点：32
- 输出节点：7
- 分类：workflow-automation
