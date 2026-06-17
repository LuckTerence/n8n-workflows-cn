## 简介
**Automatically Add Travel Time Blockers to Calendar using Google Directions API**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A-adapted（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/6700

---

# Automatically Add Travel Time Blockers to Calendar using Google Directions API


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
