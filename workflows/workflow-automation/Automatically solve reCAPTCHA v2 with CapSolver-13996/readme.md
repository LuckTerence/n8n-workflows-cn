# Automatically solve reCAPTCHA v2 with CapSolver

https://n8nworkflows.xyz/workflows/13996

## 节点清单

| 节点 | 类型 |
|------|------|
| Receive Solver Request | Webhook |
| CapSolver [Webhook] | capSolver |
| Return Solver Result | 响应 Webhook |
| Schedule Trigger (Every 1h) | 定时触发器 |
| Set Target Params | 数据设置 |
| CapSolver [Schedule] | capSolver |
| Submit Token | HTTP Request |
| Check Result | IF 判断 |
| Monitor Passed | 数据设置 |
| Monitor Failed | 数据设置 |
| Manual Trigger (Test) | 手动触发 |
| CapSolver [Manual] | capSolver |
| Format Result | 数据设置 |

## 触发方式
- Receive Solver Request 触发
- Schedule Trigger (Every 1h) 触发
- Manual Trigger (Test) 触发

## 统计
- 节点总数：13
- 触发节点：3
- 处理节点：8
- 输出节点：2
- 分类：workflow-automation
