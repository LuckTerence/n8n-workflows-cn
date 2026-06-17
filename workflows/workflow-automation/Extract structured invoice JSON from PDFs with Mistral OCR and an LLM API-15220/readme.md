## 简介
**Extract structured invoice JSON from PDFs with Mistral OCR and an LLM API**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/15220

---

# Extract structured invoice JSON from PDFs with Mistral OCR and an LLM API


## 节点清单

| 节点 | 类型 |
|------|------|
| Webhook | Webhook |
| Mistral OCR | mistralAi |
| Normalize OCR Text | Code |
| LLM Extract JSON | HTTP Request |
| Clean JSON | Code |
| Confidence >= 0.5? | IF 判断 |
| Respond OK | 响应 Webhook |
| Respond Review | 响应 Webhook |

## 触发方式
- Webhook 触发

## 统计
- 节点总数：8
- 触发节点：1
- 处理节点：4
- 输出节点：3
- 分类：workflow-automation
