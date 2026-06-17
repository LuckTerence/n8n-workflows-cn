## 简介
**Create Consistent AI Characters with Google Nano Banana & Upscaling via Kie.ai**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/8492

---

# Create Consistent AI Characters with Google Nano Banana & Upscaling via Kie.ai


## 节点清单

| 节点 | 类型 |
|------|------|
| Poll Task | HTTP Request |
| Set TaskId | 数据设置 |
| Create Task (no callback) | HTTP Request |
| When clicking ‘Execute workflow’ | 手动触发 |
| Switch | Switch 路由 |
| Create folder | Google Drive |
| Edit Fields | 数据设置 |
| Add Fields | Google Sheets |
| Create spreadsheet | Google Sheets |
| Move Sheet | Google Drive |
| Update Image Status | Google Sheets |
| Wait 1 Min | 等待 |
| Story Status Update | Google Sheets |
| Code1 | Code |
| Json parser4 | 结构化输出解析器 |
| OpenAI Chat Model3 | OpenAI Chat Model |
| Story Creator Agent | LLM Chain |
| Folder Name | Code |
| Upscale Image | HTTP Request |
| Wait 1 Min1 | 等待 |
| Switch1 | Switch 路由 |
| Set TaskId for upscale | 数据设置 |
| Get Upscaled Image | HTTP Request |
| Get ResultUrls | Code |
| Get ResultUrls from UpScale | Code |
| Upload file | Google Drive |
| Move Images | Google Drive |
| Get Binary | HTTP Request |

## 触发方式
- When clicking ‘Execute workflow’ 触发

## 统计
- 节点总数：28
- 触发节点：1
- 处理节点：22
- 输出节点：5
- 分类：workflow-automation
