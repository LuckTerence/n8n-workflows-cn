## 简介
**AI Telegram Bot Agent: Smart Assistant & Content Summarizer**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4457

---

# AI Telegram Bot Agent: Smart Assistant & Content Summarizer


## 节点清单

| 节点 | 类型 |
|------|------|
| Listener | Telegram 触发器 |
| Command Router | IF 判断 |
| Help Responder | Telegram |
| Summary Checker | IF 判断 |
| Fetcher | HTTP Request |
| Text Extractor | HTML |
| Summarizer | OpenAI |
| Summary Sender | Telegram |
| Image Prompt Checker | IF 判断 |
| Image Generator | OpenAI |
| Image Acknowledger | Telegram |

## 触发方式
- Listener 触发

## 统计
- 节点总数：11
- 触发节点：1
- 处理节点：6
- 输出节点：4
- 分类：workflow-automation
