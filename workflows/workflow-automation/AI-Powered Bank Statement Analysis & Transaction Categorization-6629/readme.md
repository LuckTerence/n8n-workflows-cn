# AI-Powered Bank Statement Analysis & Transaction Categorization

https://n8nworkflows.xyz/workflows/6629

## 节点清单

| 节点 | 类型 |
|------|------|
| Upload Statement | Webhook |
| File Handler | Code |
| Check File Type | IF 判断 |
| Extract PDF Text | 从文件提取 |
| Parse Excel/CSV | 电子表格文件 |
| AI Data Extractor | OpenAI |
| Process & Summarize | Code |
| Save to Database | PostgreSQL |
| Send Response | 响应 Webhook |

## 触发方式
- Upload Statement 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：7
- 输出节点：1
- 分类：workflow-automation
