## 简介
**Generate AI Videos from Scripts with DeepSeek, TTS, and Together.ai**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：B（需替换Zoom/Google Sheets/Google Drive)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/6777

---

# Generate AI Videos from Scripts with DeepSeek, TTS, and Together.ai


## 节点清单

| 节点 | 类型 |
|------|------|
| Set Idea | 数据设置 |
| Create Clips | HTTP Request |
| Combine Clips | HTTP Request |
| Aggregate1 | 数据聚合 |
| Loop Over Items3 | 分批处理 |
| Video url to array | Code |
| Combine Clips3 | HTTP Request |
| Add Music | HTTP Request |
| Get Captions | HTTP Request |
| Generate TTS | HTTP Request |
| Aggregate | 数据聚合 |
| Split Out | 数据拆分 |
| Fixer | Code |
| Split into 5s Scenes | Code |
| Create Captions | HTTP Request |
| On form submission | 表单触发器 |
| Structured Output Parser1 | 结构化输出解析器 |
| Structured Output Parser2 | 结构化输出解析器 |
| Script Writier 🧠 | LLM Chain |
| Output Parser 🛠 | LLM Chain |
| Switch | Switch 路由 |
| Image Prompter V2 📷 | LLM Chain |
| Loop Over Items | 分批处理 |
| Wait1 | 等待 |
| Long form to Script Writier 🧠 | LLM Chain |
| Open Router - Deepseek v3.1 | OpenRouter Chat Model |
| Open Router - Deepseek v3. | OpenRouter Chat Model |
| Combine | 数据设置 |
| Format Cleanup | 数据设置 |
| Base64 To String | 数据设置 |
| Convert String to binary | moveBinaryData |
| IDs To Array1 | Code |
| Aggregate3 | 数据聚合 |
| HTTP - Together.ai | HTTP Request |
| Google Sheets1 | Google Sheets |
| Google Sheets | Google Sheets |
| Google Drive | Google Drive |
| Google Drive1 | Google Drive |
| Google Sheets2 | Google Sheets |
| Google Sheets3 | Google Sheets |
| Google Drive2 | Google Drive |
| Extract from File | 从文件提取 |
| Google Sheets4 | Google Sheets |
| Google Sheets5 | Google Sheets |
| Google Sheets6 | Google Sheets |
| Google Drive3 | Google Drive |
| Google Sheets7 | Google Sheets |
| Google Sheets8 | Google Sheets |
| Google Sheets9 | Google Sheets |
| Code | Code |
| Split Out2 | 数据拆分 |
| Google Sheets10 | Google Sheets |
| Google Sheets12 | Google Sheets |
| Code1 | Code |
| Split Out3 | 数据拆分 |
| Google Sheets11 | Google Sheets |
| Google Sheets13 | Google Sheets |
| Google Sheets14 | Google Sheets |
| Google Sheets15 | Google Sheets |
| Google Sheets16 | Google Sheets |
| Code2 | Code |
| Google Sheets17 | Google Sheets |
| Google Sheets18 | Google Sheets |
| Google Sheets19 | Google Sheets |
| Google Sheets20 | Google Sheets |
| Telegram | Telegram |
| HTTP Request | HTTP Request |
| Telegram1 | Telegram |
| Google Drive4 | Google Drive |
| Google Drive6 | Google Drive |
| Telegram2 | Telegram |

## 触发方式
- On form submission 触发

## 统计
- 节点总数：71
- 触发节点：1
- 处理节点：58
- 输出节点：12
- 分类：workflow-automation
