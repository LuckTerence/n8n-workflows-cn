## 简介
**Auto-Sync Easy Redmine Tasks to Microsoft To-Do**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/8628

---

# Auto-Sync Easy Redmine Tasks to Microsoft To-Do


## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Trigger | 定时触发器 |
| Get To-Do in Specific List | microsoftToDo |
| Clean To-Do List | microsoftToDo |
| Just One Output after Deletion | Code |
| Get Easy Redmine Task by Filter | easyRedmine |
| Split Out Tasks | 数据拆分 |
| Add Easy Redmine Task Link to To-Do Description | Code |
| Create To-Do Tasks | microsoftToDo |

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：8
- 触发节点：1
- 处理节点：7
- 输出节点：0
- 分类：workflow-automation
