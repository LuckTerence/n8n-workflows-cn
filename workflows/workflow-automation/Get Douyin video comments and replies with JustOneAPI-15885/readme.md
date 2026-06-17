# Get Douyin video comments and replies with JustOneAPI

https://n8nworkflows.xyz/workflows/15885

## 节点清单

| 节点 | 类型 |
|------|------|
| Manual Execution Trigger | 手动触发 |
| Prepare API and Comment Data | 数据设置 |
| Fetch Video Comments via API | HTTP Request |
| Output Raw Comments Data | 数据设置 |
| Select Comment with Replies | Code |
| Check for Comment ID | IF 判断 |
| Fetch Comment Replies via API | HTTP Request |
| Output Raw Replies Data | 数据设置 |
| Build Final Reply Data | Code |
| Output Final Reply Data | 数据设置 |
| Build No Replies Data | Code |
| Output No Replies Data | 数据设置 |

## 触发方式
- Manual Execution Trigger 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：9
- 输出节点：2
- 分类：workflow-automation
