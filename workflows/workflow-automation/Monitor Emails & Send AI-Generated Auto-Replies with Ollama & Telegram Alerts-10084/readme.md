## 简介
**Monitor Emails & Send AI-Generated Auto-Replies with Ollama & Telegram Alerts**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/10084

---

# Monitor Emails & Send AI-Generated Auto-Replies with Ollama & Telegram Alerts


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
