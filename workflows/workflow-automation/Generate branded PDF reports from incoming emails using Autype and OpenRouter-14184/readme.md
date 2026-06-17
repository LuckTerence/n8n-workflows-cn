# Generate branded PDF reports from incoming emails using Autype and OpenRouter

https://n8nworkflows.xyz/workflows/14184

## 节点清单

| 节点 | 类型 |
|------|------|
| Set Company Config | 数据设置 |
| New Email Received | Email 读取 |
| Extract & Split PDFs | Code |
| Has PDFs? | IF 判断 |
| Loop Over PDFs | 分批处理 |
| Upload PDF to Autype | autype |
| Wait for OCR | 等待 |
| Poll OCR Status | HTTP Request |
| Extract OCR Text | Code |
| Combine All OCR Results | Code |
| Prepare Text Only | Code |
| Download Markdown Syntax | HTTP Request |
| Merge Context | Code |
| AI Document Assistant | AI Agent |
| Prepare Render Payload | Code |
| Render Branded PDF | autype |
| Send Report via Email | Email 发送 |
| /scrape in Firecrawl | Firecrawl 工具 |
| OpenRouter Chat Model | OpenRouter Chat Model |
| SerpAPI | SerpApi 工具 |
| Autype Lens OCR | HTTP Request |

## 触发方式
- 手动触发

## 统计
- 节点总数：21
- 触发节点：0
- 处理节点：16
- 输出节点：5
- 分类：workflow-automation
