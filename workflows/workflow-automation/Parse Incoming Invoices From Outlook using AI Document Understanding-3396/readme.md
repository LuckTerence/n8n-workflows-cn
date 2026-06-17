# Parse Incoming Invoices From Outlook using AI Document Understanding

https://n8nworkflows.xyz/workflows/3396

## 节点清单

| 节点 | 类型 |
|------|------|
| Split Attachments | Code |
| Download Attachments | Outlook |
| Parse Output | 数据设置 |
| For Each Message | 分批处理 |
| Message Ref | 空操作 |
| Message Classifier | 文本分类器 |
| Extract from File | 从文件提取 |
| Markdown | Markdown |
| Empty Response | 数据设置 |
| Wait | 等待 |
| Filter Invoices | 过滤器 |
| Has Invoice? | IF 判断 |
| Schedule Trigger | 定时触发器 |
| Get Recent Messages | Outlook |
| Model | OpenAI Chat Model |
| Microsoft Excel 365 | microsoftExcel |
| Invoice Classifier With Gemini 2.0 | HTTP Request |
| File-Based OCR with Gemini 2.0 | HTTP Request |

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：18
- 触发节点：1
- 处理节点：13
- 输出节点：4
- 分类：workflow-automation
