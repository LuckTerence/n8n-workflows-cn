## 简介
**Orchestrate iterative content drafting with research, writer and reviewer flows**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/15994

---

# Orchestrate iterative content drafting with research, writer and reviewer flows


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
