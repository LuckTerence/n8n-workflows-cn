# Generate weekly dinner meal plans and shopping lists using Mealie

https://n8nworkflows.xyz/workflows/13815

## 节点清单

| 节点 | 类型 |
|------|------|
| Generate Random Meal in Mealie | HTTP Request |
| Get Recipe From Mealie By Slug | HTTP Request |
| Normalize Mealie Recipe Data | Code |
| Schedule Trigger | 定时触发器 |
| Create New Shopping List in Mealie | HTTP Request |
| Add Recipe(s) Ingredients To Shopping List in Mealie | HTTP Request |
| Generate Next 7 Days | Code |

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：7
- 触发节点：1
- 处理节点：2
- 输出节点：4
- 分类：workflow-automation
