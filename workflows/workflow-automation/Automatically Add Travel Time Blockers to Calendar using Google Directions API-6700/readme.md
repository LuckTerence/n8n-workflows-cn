# Automatically Add Travel Time Blockers to Calendar using Google Directions API

https://n8nworkflows.xyz/workflows/6700

## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Trigger | 定时触发器 |
| AI Agent | AI Agent |
| OpenAI Chat Model | OpenAI Chat Model |
| Simple Memory | 记忆缓冲区 |
| get_calendar_events | Google Calendar 工具 |
| create_calendar_event | Google Calendar 工具 |
| travel_directions | 工作流工具 |
| set Travel_time | 数据设置 |
| Call Google Directions API | HTTP Request |
| Sub: travel_directions | 执行工作流触发器 |
| Set Defaults | 数据设置 |

## 触发方式
- Schedule Trigger 触发
- Sub: travel_directions 触发

## 统计
- 节点总数：11
- 触发节点：2
- 处理节点：8
- 输出节点：1
- 分类：workflow-automation
