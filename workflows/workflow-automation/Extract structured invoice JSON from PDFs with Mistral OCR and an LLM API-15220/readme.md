# Extract structured invoice JSON from PDFs with Mistral OCR and an LLM API

https://n8nworkflows.xyz/workflows/15220

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
