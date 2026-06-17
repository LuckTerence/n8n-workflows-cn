# Receive and process incoming direct messages in Rocket.Chat

https://n8nworkflows.xyz/workflows/15775

## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Trigger | 定时触发器 |
| Split Out | 数据拆分 |
| Loop Over Items | 分批处理 |
| Subscription.get | HTTP Request |
| IM.Messages | HTTP Request |
| Split Out1 | 数据拆分 |
| Get last | Code |
| Only Users Prompt | 过滤器 |
| Sort | 数据排序 |
| Unread and Direct Messages | 过滤器 |
| Mark as Read | HTTP Request |
| No Operation, do nothing | 空操作 |
| RocketChat | rocketchat |

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：13
- 触发节点：1
- 处理节点：9
- 输出节点：3
- 分类：workflow-automation
