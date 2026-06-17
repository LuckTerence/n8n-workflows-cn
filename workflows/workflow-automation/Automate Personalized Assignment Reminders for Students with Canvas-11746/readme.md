## 简介
**Automate Personalized Assignment Reminders for Students with Canvas**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：12 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/11746

---

# Automate Personalized Assignment Reminders for Students with Canvas


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Execute workflow’ | 手动触发 |
| Initial parameters | 数据设置 |
| Get course by name | 过滤器 |
| Get all teacher courses | HTTP Request |
| Get course ID | 数据设置 |
| Get course students | HTTP Request |
| Agregate courses pagination | Code |
| Agregate students pagination | Code |
| Get course sumbissions | HTTP Request |
| Agregate submits pagination | Code |
| Enrich Submissions with Student Data | Code |
| Group Pending Assignments per Student | Code |
| Send message in Canvas | HTTP Request |

## 触发方式
- When clicking ‘Execute workflow’ 触发

## 统计
- 节点总数：13
- 触发节点：1
- 处理节点：8
- 输出节点：4
- 分类：workflow-automation
