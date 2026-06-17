# Generate product demo highlight reels using WayinVideo Find Moments API

https://n8nworkflows.xyz/workflows/14712

## 节点清单

| 节点 | 类型 |
|------|------|
| 1. Form — Demo URL + Query + Email | 表单触发器 |
| 2. WayinVideo — Submit Find Moments | HTTP Request |
| 3. Wait — 90 Seconds | 等待 |
| 4. WayinVideo — Get Moments Result | HTTP Request |
| 5. IF — Status SUCCEEDED? | IF 判断 |
| 6. Wait — 30 Seconds Retry | 等待 |
| 7. Gmail — Send Review Email | Email 发送 |

## 触发方式
- 1. Form — Demo URL + Query + Email 触发

## 统计
- 节点总数：7
- 触发节点：1
- 处理节点：3
- 输出节点：3
- 分类：workflow-automation
