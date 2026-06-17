# Run Multiple Tasks in Parallel with Asynchronous Processing and Webhooks

https://n8nworkflows.xyz/workflows/8578

## 节点清单

| 节点 | 类型 |
|------|------|
| Start | 手动触发 |
| Call Entry Point | 执行工作流触发器 |
| Wait Seconds | 等待 |
| Call 1 | 执行工作流 |
| Request Webhook | HTTP Request |
| Wait for Webhook 1 | 等待 |
| Wait for Webhook 2 | 等待 |
| Wait 1 Second | 等待 |
| Call 2 | 执行工作流 |
| Merge | 数据合并 |
| Sum | 文本摘要 |

## 触发方式
- Start 触发
- Call Entry Point 触发

## 统计
- 节点总数：11
- 触发节点：2
- 处理节点：8
- 输出节点：1
- 分类：workflow-automation
