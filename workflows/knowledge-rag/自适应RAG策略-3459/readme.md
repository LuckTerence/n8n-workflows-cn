## 简介
**自适应RAG策略**

查询分类+Qdrant

> 分类：知识库 RAG | 适配等级：A（AI模型已适配，部分外服节点需手动替换为国内服务）
> 原始来源：https://n8nworkflows.xyz/workflows/3459

---

# 自适应RAG策略


## 节点清单

| 节点 | 类型 |
|------|------|
| Query Classification | AI Agent |
| Switch | Switch 路由 |
| Factual Strategy - Focus on Precision | AI Agent |
| Analytical Strategy - Comprehensive Coverage | AI Agent |
| Opinion Strategy - Diverse Perspectives | AI Agent |
| Contextual Strategy - User Context Integration | AI Agent |
| Chat | Chat 触发器 |
| Factual Prompt and Output | 数据设置 |
| Contextual Prompt and Output | 数据设置 |
| Opinion Prompt and Output | 数据设置 |
| Analytical Prompt and Output | 数据设置 |
| Gemini Classification | Google Gemini |
| Gemini Factual | Google Gemini |
| Gemini Analytical | Google Gemini |
| Chat Buffer Memory Analytical | 记忆缓冲区 |
| Chat Buffer Memory Factual | 记忆缓冲区 |
| Gemini Opinion | Google Gemini |
| Chat Buffer Memory Opinion | 记忆缓冲区 |
| Gemini Contextual | Google Gemini |
| Chat Buffer Memory Contextual | 记忆缓冲区 |
| Embeddings | Google Gemini Embeddings |
| Concatenate Context | 文本摘要 |
| Retrieve Documents from Vector Store | Qdrant 向量存储 |
| Set Prompt and Output | 数据设置 |
| Gemini Answer | Google Gemini |
| Answer | AI Agent |
| Chat Buffer Memory | 记忆缓冲区 |
| Respond to Webhook | 响应 Webhook |
| When Executed by Another Workflow | 执行工作流触发器 |
| Combined Fields | 数据设置 |

## 触发方式
- Chat 触发
- When Executed by Another Workflow 触发

## 统计
- 节点总数：30
- 触发节点：2
- 处理节点：27
- 输出节点：1
- 分类：knowledge-rag
