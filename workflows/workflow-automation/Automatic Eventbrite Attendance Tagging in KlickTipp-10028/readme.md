## 简介
**Automatic Eventbrite Attendance Tagging in KlickTipp**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：5 | 难度：⭐ 入门
> 原始来源：https://n8nworkflows.xyz/workflows/10028

---

# Automatic Eventbrite Attendance Tagging in KlickTipp


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
