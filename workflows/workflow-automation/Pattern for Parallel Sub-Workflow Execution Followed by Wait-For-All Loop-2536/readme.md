# Pattern for Parallel Sub-Workflow Execution Followed by Wait-For-All Loop

https://n8nworkflows.xyz/workflows/2536

## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Test workflow’ | 手动触发 |
| Loop Over Items | 分批处理 |
| Webhook Callback Wait | 等待 |
| Update finishedSet | Code |
| Initialize finishedSet | 数据设置 |
| Simulate Multi-Item for Parallel Processing | Code |
| If All Finished | IF 判断 |
| Start Sub-Workflow via Webhook | HTTP Request |
| Acknowledge Finished | 响应 Webhook |
| Continue Workflow (noop) | 空操作 |
| Wait | 等待 |
| Call Resume on Parent Workflow | HTTP Request |
| Respond to Webhook | 响应 Webhook |
| Webhook | Webhook |

## 触发方式
- When clicking ‘Test workflow’ 触发
- Webhook 触发

## 统计
- 节点总数：14
- 触发节点：2
- 处理节点：8
- 输出节点：4
- 分类：workflow-automation
