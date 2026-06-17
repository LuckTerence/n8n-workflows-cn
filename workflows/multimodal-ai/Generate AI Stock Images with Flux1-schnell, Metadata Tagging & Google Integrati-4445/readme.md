## 简介
**Generate AI Stock Images with Flux1-schnell, Metadata Tagging & Google Integration**

（待补充中文描述）

> 分类：多模态 AI | 适配等级：A（需替换Google Sheets/Google Drive)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4445

---

# Generate AI Stock Images with Flux1-schnell, Metadata Tagging & Google Integration


## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Trigger | 定时触发器 |
| Set Date Info | Code |
| Google Sheets | Google Sheets |
| Edit Fields | 数据设置 |
| Generate Image | HTTP Request |
| Create Folder for images | Google Drive |
| Create New Sheet | Google Drive |
| Set Folder ID sheet | Code |
| Set Folder ID drive folder | Code |
| Sheet Exists? | IF 判断 |
| Folder Exists? | IF 判断 |
| Check the folder | Google Drive |
| Check sheet | Google Drive |
| Comp Images | 图片编辑 |
| Analyze images | OpenAI |
| Split Out data | 数据拆分 |
| Resize Image X2 | 图片编辑 |
| Numbering | Code |
| Parse OpenAI Response | Code |
| Telegram | Telegram |
| Google Sheets3 | Google Sheets |
| Code4 | Code |
| Google Sheets4 | Google Sheets |
| Merge2 | 数据合并 |
| filter data date | Code |
| Select Prompt | Code |
| Get Images | HTTP Request |
| Wait | 等待 |
| Check if it has data? | IF 判断 |
| Split Out | 数据拆分 |
| Download Images | HTTP Request |
| Merge | 数据合并 |
| Upload Images | Google Drive |
| 20 seconds | 等待 |
| Log Error | Google Sheets |
| Split Prompts | Function |
| Create Loop Indexes | Function |
| Merge Batches | 数据合并 |
| Set Topic | 数据设置 |
| Google Sheets1 | Google Sheets |
| Google Sheets2 | Google Sheets |
| Prompt Generator | LLM Chain |
| OpenAI | OpenAI Chat Model |
| Schedule Trigger1 | 定时触发器 |
| Telegram1 | Telegram |
| Error Trigger | 错误触发器 |

## 触发方式
- Schedule Trigger 触发
- Schedule Trigger1 触发
- Error Trigger 触发

## 统计
- 节点总数：46
- 触发节点：3
- 处理节点：38
- 输出节点：5
- 分类：multimodal-ai
