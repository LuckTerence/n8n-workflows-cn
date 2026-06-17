# Automatic Eventbrite Attendance Tagging in KlickTipp

https://n8nworkflows.xyz/workflows/10028

## 节点清单

| 节点 | 类型 |
|------|------|
| Trigger every 15min | 定时触发器 |
| Tag contact for non attendance | Klicktipp |
| Attendance check | Switch 路由 |
| Split attendee list | 数据拆分 |
| List Evenbrite attendees from event | HTTP Request |
| Tag contact for attendance | Klicktipp |

## 触发方式
- Trigger every 15min 触发

## 统计
- 节点总数：6
- 触发节点：1
- 处理节点：4
- 输出节点：1
- 分类：workflow-automation
