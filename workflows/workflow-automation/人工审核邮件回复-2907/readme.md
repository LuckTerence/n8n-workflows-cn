## 简介
**人工审核邮件回复**

AI生成回复+人工确认后再发送

> 分类：工作流自动化 | 适配等级：A（需替换Gmail)（AI模型已替换为DeepSeek，部分边角节点可能仍需手动调整）
> 节点数：10 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/2907

---

# 人工审核邮件回复


## 节点清单

| 节点 | 类型 |
|------|------|
| Email Trigger (IMAP) | Email 读取 |
| Markdown | Markdown |
| Send Email | Email 发送 |
| Email Summarization Chain | chainSummarization |
| Write email | AI Agent |
| OpenAI | OpenAI Chat Model |
| Approve Email | Email 发送 |
| OpenAI Chat Model | OpenAI Chat Model |
| Set Email text | 数据设置 |
| Approved? | IF 判断 |

## 触发方式
- 手动触发

## 统计
- 节点总数：10
- 触发节点：0
- 处理节点：7
- 输出节点：3
- 分类：workflow-automation
