## 简介
**Create a weekly Mealie dinner plan and generate a smart shopping list**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A-adapted（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/14095

---

# Create a weekly Mealie dinner plan and generate a smart shopping list


## 节点清单

| 节点 | 类型 |
|------|------|
| Add Ingredients To Shopping List | HTTP Request |
| Delete Random Meal Plan | HTTP Request |
| Split Removals Array | 数据拆分 |
| Generate Random Meal Plan | HTTP Request |
| Create Shopping List in Mealie | HTTP Request |
| Normalize Recipe Data | Code |
| Fetch Current Week Meal Plans | HTTP Request |
| Send Meal Plan Email | Email 发送 |
| Normalize User Response | Code |
| Check for Removals | IF 判断 |
| Generate Upcoming Week | Code |
| Weekly Schedule Trigger | 定时触发器 |
| Prepare Meal Plan Email Data | Code |
| Fetch Recipe By Slug | HTTP Request |

## 触发方式
- Weekly Schedule Trigger 触发

## 统计
- 节点总数：14
- 触发节点：1
- 处理节点：6
- 输出节点：7
- 分类：workflow-automation
