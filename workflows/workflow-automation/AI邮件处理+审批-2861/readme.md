## 简介
**AI邮件处理+审批**

自动回复+人工审批开关

> 分类：工作流自动化 | 适配等级：B（核心链路通了，边角节点可能要自己调）
> 原始来源：https://n8nworkflows.xyz/workflows/2861

---

# AI邮件处理+审批


## 节点清单

| 节点 | 类型 |
|------|------|
| Email Trigger (IMAP) | Email 读取 |
| Markdown | Markdown |
| DeepSeek R1 | OpenAI Chat Model |
| Send Email | Email 发送 |
| Qdrant Vector Store | Qdrant 向量存储 |
| Embeddings OpenAI | OpenAI Embeddings |
| Email Summarization Chain | chainSummarization |
| Write email | AI Agent |
| OpenAI | OpenAI Chat Model |
| Set Email | 数据设置 |
| Approve? | IF 判断 |
| Send Draft | Gmail |

## 触发方式
- 手动触发

## 统计
- 节点总数：12
- 触发节点：0
- 处理节点：10
- 输出节点：2
- 分类：workflow-automation
