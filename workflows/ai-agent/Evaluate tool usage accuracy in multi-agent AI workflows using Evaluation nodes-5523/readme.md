## 简介
**Evaluate tool usage accuracy in multi-agent AI workflows using Evaluation nodes**

（待补充中文描述）

> 分类：AI Agent | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5523

---

# Evaluate tool usage accuracy in multi-agent AI workflows using Evaluation nodes


## 节点清单

| 节点 | 类型 |
|------|------|
| Calculator | 计算器工具 |
| Check if tool called | 数据设置 |
| When chat message received | Chat 触发器 |
| Match chat format | 数据设置 |
| Return chat response | 空操作 |
| When fetching a dataset row | evaluationTrigger |
| Evaluation | 条件评估 |
| Evaluating? | 条件评估 |
| Set Outputs | 条件评估 |
| Search Agent | AI Agent |
| Summarizer | 工作流工具 |
| Web search | HTTP Request 工具 |
| OpenRouter Chat Model | OpenRouter Chat Model |
| Embeddings OpenAI | OpenAI Embeddings |
| Search_db | Qdrant 向量存储 |

## 触发方式
- When chat message received 触发
- When fetching a dataset row 触发

## 统计
- 节点总数：15
- 触发节点：2
- 处理节点：12
- 输出节点：1
- 分类：ai-agent
