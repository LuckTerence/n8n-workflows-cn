## 简介
**Document Parsing & Data Extraction with Mistral OCR, AI Processing, and Multi-Channel Delivery**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：B（需替换Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4933

---

# Document Parsing & Data Extraction with Mistral OCR, AI Processing, and Multi-Channel Delivery


## 节点清单

| 节点 | 类型 |
|------|------|
| send pdf to Mistral | HTTP Request |
| mistral - get signed url | HTTP Request |
| Mistral Cloud Chat Model1 | Mistral Chat Model |
| Edit Fields | 数据设置 |
| Get Parsed Invoice | HTTP Request |
| AI Agent | AI Agent |
| Markdown | Markdown |
| Edit Fields2 | 数据设置 |
| Gmail | Email 发送 |
| AI Agent1 | AI Agent |
| OpenAI Chat Model | OpenAI Chat Model |
| Telegram Trigger | Telegram 触发器 |
| Download File | HTTP Request |
| Send Confirmation | Telegram |
| Telegram | Telegram |
| Telegram1 | Telegram |
| Code | Code |
| On form submission | 表单触发器 |

## 触发方式
- Telegram Trigger 触发
- On form submission 触发

## 统计
- 节点总数：18
- 触发节点：2
- 处理节点：8
- 输出节点：8
- 分类：workflow-automation
