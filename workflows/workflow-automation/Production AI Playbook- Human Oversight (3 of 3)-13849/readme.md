# Production AI Playbook: Human Oversight (3 of 3)

https://n8nworkflows.xyz/workflows/13849

## 节点清单

| 节点 | 类型 |
|------|------|
| On form submission1 | 表单触发器 |
| AI Agent1 | AI Agent |
| OpenAI Chat Model | OpenAI Chat Model |
| Route by Channel | Switch 路由 |
| Slack Approval Request | Slack |
| Slack Decision | Switch 路由 |
| Publish Content | Code |
| Handle Rejection | Code |
| Escalate to Manager | Email 发送 |
| Email Decision | Switch 路由 |
| Email Approval Request | Email 发送 |

## 触发方式
- On form submission1 触发

## 统计
- 节点总数：11
- 触发节点：1
- 处理节点：7
- 输出节点：3
- 分类：workflow-automation
