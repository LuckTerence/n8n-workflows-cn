# Extract Text from Images & PDFs via Telegram with Mistral OCR to Markdown

https://n8nworkflows.xyz/workflows/6209

## 节点清单

| 节点 | 类型 |
|------|------|
| Image / PDF | IF 判断 |
| Mistral OCR | HTTP Request |
| Settings | 数据设置 |
| Telegram Event Handler | Switch 路由 |
| Status “Typing…” | Telegram |
| Notification about correct commands | Telegram |
| Maximum file size exceeded | Telegram |
| Checking file size | IF 判断 |
| File classifier | Code |
| Generating temporary file link | Telegram |
| Invalid file | Telegram |
| Markdown converter | Code |
| Converting Markdown to File | 转换为文件 |
| Manual Webhook Setup Trigger | 手动触发 |
| Telegram Webhook Configuration | 数据设置 |
| Check Production Mode | IF 判断 |
| Set Production Webhook | HTTP Request |
| Set Development Webhook | HTTP Request |
| Return Webhook Status | HTTP Request |
| Check Whitelist Status | IF 判断 |
| Whitelist Logic | Code |
| Access Denied | Telegram |
| Determine Message Type | Switch 路由 |
| Inform Bot Capabilities | Telegram |
| Command Router | Switch 路由 |
| Send Markdown File to Telegram | Telegram |
| Respond with attachment | 响应 Webhook |
| Determine Incoming Request Source Type | Switch 路由 |
| Is Whitelist Disabled? | IF 判断 |
| Get a file | Telegram |
| Incoming request | Webhook |
| Problem with file recognition | Telegram |

## 触发方式
- Manual Webhook Setup Trigger 触发
- Incoming request 触发

## 统计
- 节点总数：32
- 触发节点：2
- 处理节点：15
- 输出节点：15
- 分类：workflow-automation
