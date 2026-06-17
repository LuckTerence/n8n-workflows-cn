# Pattern for Multiple Triggers Combined to Continue Workflow

https://n8nworkflows.xyz/workflows/2857

## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Test workflow’ | 手动触发 |
| Wait | 等待 |
| HTTP Request - Initiate Independent Process | HTTP Request |
| HTTP Request - Resume Other Workflow Execution | HTTP Request |
| This Node Can Access Primary and Secondary | 数据设置 |
| Set Primary Execution Context | 数据设置 |
| Receive Input from External, Independent Process | Webhook |
| Respond to Webhook | 响应 Webhook |
| Simulate Event that Hits the 2nd Trigger/Flow | HTTP Request |
| Simulate some Consumed Service Time | 等待 |
| HTTP Request - Get A Random Joke | HTTP Request |
| Demo "Trigger" Callback Setup | 数据设置 |
| Webhook | Webhook |

## 触发方式
- When clicking ‘Test workflow’ 触发
- Receive Input from External, Independent Process 触发
- Webhook 触发

## 统计
- 节点总数：13
- 触发节点：3
- 处理节点：5
- 输出节点：5
- 分类：workflow-automation
