## 简介
**Ask a human for help when the AI doesn't know the answer**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2095

---

# Ask a human for help when the AI doesn't know the answer


## 节点清单

| 节点 | 类型 |
|------|------|
| When chat message received | Chat 触发器 |
| OpenAI Chat Model | OpenAI Chat Model |
| Simple Memory | 记忆缓冲区 |
| When Executed by Another Workflow | 执行工作流触发器 |
| Check if user has provided email | IF 判断 |
| Message Slack for help | Slack |
| Confirm that we've messaged a human | Code |
| Prompt the user to provide an email | Code |
| Not sure? | 工作流工具 |
| AI Agent | AI Agent |

## 触发方式
- When chat message received 触发
- When Executed by Another Workflow 触发

## 统计
- 节点总数：10
- 触发节点：2
- 处理节点：7
- 输出节点：1
- 分类：workflow-automation
