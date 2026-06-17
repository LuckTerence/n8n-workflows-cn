# Automate follower resource distribution on BlueSky with keyword-triggered DMs

https://n8nworkflows.xyz/workflows/12159

## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Trigger | 定时触发器 |
| BlueSky Auth | HTTP Request |
| Get Notifications | HTTP Request |
| Split Out | 数据拆分 |
| Loop Over Items | 分批处理 |
| Does Follow? | IF 判断 |
| Get Convo ID | HTTP Request |
| Check Follow Status | HTTP Request |
| Send DM | HTTP Request |
| Filter New Only | Code |
| Filter Reply contains | 过滤器 |
| Like the reply | HTTP Request |
| Configuration | 数据设置 |
| Extract Post ID | 数据设置 |

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：14
- 触发节点：1
- 处理节点：7
- 输出节点：6
- 分类：workflow-automation
