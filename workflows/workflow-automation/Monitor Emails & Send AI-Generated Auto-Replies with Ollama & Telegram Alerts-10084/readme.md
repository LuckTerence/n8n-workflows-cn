# Monitor Emails & Send AI-Generated Auto-Replies with Ollama & Telegram Alerts

https://n8nworkflows.xyz/workflows/10084

## 节点清单

| 节点 | 类型 |
|------|------|
| No Operation | 空操作 |
| Send Notification from Incoming Email | Telegram |
| Dedicate Filtering As No-Response | IF 判断 |
| Check Incoming Emails - IMAP (example: SOGo) | Email 读取 |
| Ollama Model | lmOllama |
| Basic LLM Chain | LLM Chain |
| Send Auto-Response in SMTP (example POSTFIX) | Email 发送 |
| Send Notification from Response | Telegram |

## 触发方式
- 手动触发

## 统计
- 节点总数：8
- 触发节点：0
- 处理节点：4
- 输出节点：4
- 分类：workflow-automation
