## 简介
**Check dependencies before completing Awork tasks (Workaround)**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：24 | 难度：⭐⭐⭐ 高级
> 原始来源：https://n8nworkflows.xyz/workflows/4350

---

# Check dependencies before completing Awork tasks (Workaround)


## 节点清单

| 节点 | 类型 |
|------|------|
| Load dependencies for task | HTTP Request |
| Aggregate task dependencies | 数据聚合 |
| Workflow config | 数据设置 |
| Fetch task changes | 数据设置 |
| Split out task changes | 数据拆分 |
| Filter task status change | 过滤器 |
| Check if task done | IF 判断 |
| Webhook call by Awork | Webhook |
| Check if dependencies enabled | IF 判断 |
| Load all linked tasks | HTTP Request |
| Build filter params | Code |
| Filter only open tasks | 过滤器 |
| Aggregate open task IDs | 数据聚合 |
| Check if open tasks exist | IF 判断 |
| Check if comments are enabled | IF 判断 |
| Add comment to tasks | HTTP Request |
| Check if tree structure enabled | IF 判断 |
| Check subtasks | IF 判断 |
| Roll back task status from done to previous state | HTTP Request |
| Load all open sub tasks | HTTP Request |
| Aggregate task IDs | 数据聚合 |
| Check open subtasks | IF 判断 |
| Check if comments are enabled1 | IF 判断 |
| Add comment to tasks1 | HTTP Request |
| Roll back task status from done to previous state1 | HTTP Request |

## 触发方式
- Webhook call by Awork 触发

## 统计
- 节点总数：25
- 触发节点：1
- 处理节点：17
- 输出节点：7
- 分类：workflow-automation
