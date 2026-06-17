# Extract Details from Receipts via Telegram with Tesseract and Llama

https://n8nworkflows.xyz/workflows/4361

## 节点清单

| 节点 | 类型 |
|------|------|
| Format Summary Message | Code |
| Get Telegram File | HTTP Request |
| Download Image | HTTP Request |
| Telegram Trigger | Telegram 触发器 |
| AI Categorizer | LLM Chain |
| Check Invalid Input | IF 判断 |
| Extract Text Input | 数据设置 |
| Check for Image | IF 判断 |
| Receipt Parser | 结构化输出解析器 |
| AI Analyzer | OpenRouter Chat Model |
| Send Error Message | Telegram |
| Send Expense Summary | Telegram |
| Extract Value From Image | tesseractNode |

## 触发方式
- Telegram Trigger 触发

## 统计
- 节点总数：13
- 触发节点：1
- 处理节点：8
- 输出节点：4
- 分类：workflow-automation
