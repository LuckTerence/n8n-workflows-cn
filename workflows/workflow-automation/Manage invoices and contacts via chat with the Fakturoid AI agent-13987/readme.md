## 简介
**Manage invoices and contacts via chat with the Fakturoid AI agent**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：13 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/13987

---

# Manage invoices and contacts via chat with the Fakturoid AI agent


## 节点清单

| 节点 | 类型 |
|------|------|
| Simple Memory | 记忆缓冲区 |
| INVOICE_PAYMENT | 工作流工具 |
| UPDATE_SUBJECT | 工作流工具 |
| CREATE_SUBJECT | 工作流工具 |
| GET_SUBJECT | 工作流工具 |
| ARES LOOKUP | 工作流工具 |
| CREATE_INVOICE | 工作流工具 |
| GET_INVOICE | 工作流工具 |
| DELETE_INVOICE | 工作流工具 |
| UPDATE_INVOICE | 工作流工具 |
| DELETE_SUBJECT | 工作流工具 |
| AI Agent1 | AI Agent |
| When chat message received | Chat 触发器 |
| GPT-5-mini | OpenAI Chat Model |

## 触发方式
- When chat message received 触发

## 统计
- 节点总数：14
- 触发节点：1
- 处理节点：13
- 输出节点：0
- 分类：workflow-automation
