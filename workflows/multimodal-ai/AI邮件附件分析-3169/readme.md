## 简介
**AI邮件附件分析**

分析PDF/图片附件保存到Drive+Telegram

> 分类：多模态 AI | 适配等级：A（需替换Google Sheets/Google Drive)（AI模型已替换为DeepSeek，部分边角节点可能仍需手动调整）
> 节点数：25 | 难度：⭐⭐⭐ 高级
> 原始来源：https://n8nworkflows.xyz/workflows/3169

---

# AI邮件附件分析


## 节点清单

| 节点 | 类型 |
|------|------|
| Email Trigger (IMAP) | Email 读取 |
| DeepSeek R1 | OpenAI Chat Model |
| Email Summarization Chain | chainSummarization |
| Switch | Switch 路由 |
| Structured Output Parser | 结构化输出解析器 |
| Split Out | 数据拆分 |
| Aggregate | 数据聚合 |
| OpenRouter Chat Model1 | OpenRouter Chat Model |
| Contain attachments? | IF 判断 |
| Get PDF and images attachments | Code |
| Extract from PDF | 从文件提取 |
| PDF Analyzer | LLM Chain |
| Save summary PDF | Google Sheets |
| All summaries | 数据合并 |
| Map image summaries | 数据设置 |
| Upload attachments | Google Drive |
| Email summary | 数据设置 |
| Send final summary | Telegram |
| Create final summary | LLM Chain |
| Save summary image | Google Sheets |
| Save summary text | Google Sheets |
| Convert text | Markdown |
| Gemini 2.0 Flash | OpenRouter Chat Model |
| Parsing | Code |
| Analyze image | OpenAI |

## 触发方式
- 手动触发

## 统计
- 节点总数：25
- 触发节点：0
- 处理节点：23
- 输出节点：2
- 分类：multimodal-ai
