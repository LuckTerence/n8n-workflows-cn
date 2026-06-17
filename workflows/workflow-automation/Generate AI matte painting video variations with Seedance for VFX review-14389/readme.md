## 简介
**Generate AI matte painting video variations with Seedance for VFX review**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Slack/Gmail)（基本改完，配置 API Key 应该就能跑）
> 节点数：18 | 难度：⭐⭐⭐ 高级
> 原始来源：https://n8nworkflows.xyz/workflows/14389

---

# Generate AI matte painting video variations with Seedance for VFX review


## 节点清单

| 节点 | 类型 |
|------|------|
| Build Request Body | Code |
| Merge Job ID + Metadata | Code |
| Webhook: Matte Painting Request2 | Webhook |
| Validate & Extract Input2 | Code |
| Fan-Out: 4 Atmosphere Variations2 | Code |
| Seedance: Generate Variation1 | HTTP Request |
| Poll: Check Job Status1 | HTTP Request |
| Wait 20s1 | 等待 |
| Render Complete?2 | IF 判断 |
| Build Asset Metadata3 | Code |
| Generate Nuke Comp Template1 | Code |
| Jira: Create Review Task | jira |
| Aggregate All Variations3 | Code |
| Slack: Notify Supervisor | Slack |
| Send a message | Email 发送 |
| Slack: Error Alert | Slack |
| On Workflow Error | 错误触发器 |
| Download File | HTTP Request |
| Add Record in Clickup | clickUp |

## 触发方式
- Webhook: Matte Painting Request2 触发
- On Workflow Error 触发

## 统计
- 节点总数：19
- 触发节点：2
- 处理节点：11
- 输出节点：6
- 分类：workflow-automation
