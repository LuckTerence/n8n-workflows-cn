# Orchestrate iterative content drafting with research, writer and reviewer flows

https://n8nworkflows.xyz/workflows/15994

## 节点清单

| 节点 | 类型 |
|------|------|
| Webhook - Content Request | Webhook |
| Normalize Request | Code |
| Call Research Subworkflow | 执行工作流 |
| Call Writer Subworkflow | 执行工作流 |
| Call Reviewer Subworkflow | 执行工作流 |
| Evaluate Review | Code |
| Approved or Max Revisions? | IF 判断 |
| Finalize Response | Code |
| Respond to Client | 响应 Webhook |

## 触发方式
- Webhook - Content Request 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：7
- 输出节点：1
- 分类：workflow-automation
