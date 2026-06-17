# Automatically document and backup N8N workflows

https://n8nworkflows.xyz/workflows/3354

## 节点清单

| 节点 | 类型 |
|------|------|
| Set fields | 数据设置 |
| Get notion page with workflow id | HTTP Request |
| Map fields | 数据设置 |
| Add to Notion | Notion |
| Update in Notion | Notion |
| Notify internal-infra of push | Slack |
| Notify internal-infra of update | Slack |
| Notify on workflow setup error | Slack |
| Summarize what the Workflow does | OpenAI |
| Upload changes to repo | github |
| Create new file in repo | github |
| Notify on create file in repo fail | Slack |
| Is this a new workflow (to Notion) ? | IF 判断 |
| Every Monday at 1am | 定时触发器 |
| Check if updated in last 7 days | IF 判断 |
| Get active workflows with internal-infra tag | n8n |
| Check that error workflow has been configured | IF 判断 |

## 触发方式
- Every Monday at 1am 触发

## 统计
- 节点总数：17
- 触发节点：1
- 处理节点：11
- 输出节点：5
- 分类：devops
