## 简介
**Assign Requests Using AI and Send Reminders Based On NocoDB Kanban Board Status**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：B（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3784

---

# Assign Requests Using AI and Send Reminders Based On NocoDB Kanban Board Status


## 节点清单

| 节点 | 类型 |
|------|------|
| Incident Form | 表单触发器 |
| Assign Category | AI Agent |
| OpenAI Chat Model1 | OpenAI Chat Model |
| Structure Output Todoist Ready1 | 结构化输出解析器 |
| Get incident definitions | NocoDB |
| Insert Incident | NocoDB |
| Aggregate for AI parsing | 数据聚合 |
| On schedule or during flow | 空操作 |
| When clicking ‘Test workflow’ | 手动触发 |
| Task is not picked up after expected response | IF 判断 |
| Send email to client | Email 发送 |
| Check status every day | 定时触发器 |
| Send email to asignee | Email 发送 |
| Get Unpicked Tasks | NocoDB |
| Get Unfinished Tasks | NocoDB |
| Task is not complete in expected time | IF 判断 |
| Send email to client1 | Email 发送 |
| If there is asignee email | IF 判断 |
| If there is assignee slack | IF 判断 |
| Slack to assignee | Slack |
| Send another email to asignee | Email 发送 |
| Format for Noco | 数据设置 |

## 触发方式
- Incident Form 触发
- When clicking ‘Test workflow’ 触发
- Check status every day 触发

## 统计
- 节点总数：22
- 触发节点：3
- 处理节点：14
- 输出节点：5
- 分类：workflow-automation
