## 简介
**Entra Contacts to Zammad User Sync**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2599

---

# Entra Contacts to Zammad User Sync


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Test workflow’ | 手动触发 |
| Zammad Univeral User Object | 数据设置 |
| Get Zammad Users | zammad |
| Merge | 数据合并 |
| Find new Zammad Users | compareDatasets |
| Update Zammad User | zammad |
| Create Zammad User | zammad |
| Deactivate Zammad User | zammad |
| Find removed Users | compareDatasets |
| Get Contacts from Entra | HTTP Request |
| Entra Contacts | 数据拆分 |
| Filter contacts if needed | IF 判断 |
| Filter if needed | IF 判断 |

## 触发方式
- When clicking ‘Test workflow’ 触发

## 统计
- 节点总数：13
- 触发节点：1
- 处理节点：11
- 输出节点：1
- 分类：workflow-automation
