## 简介
**Selectively import workflows between instances using the n8n API and forms**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：39 | 难度：⭐⭐⭐ 高级
> 原始来源：https://n8nworkflows.xyz/workflows/13425

---

# Selectively import workflows between instances using the n8n API and forms


## 节点清单

| 节点 | 类型 |
|------|------|
| On form submission | 表单触发器 |
| Strip Incompatible API Fields | Code |
| Filter Our Archived Items | 过滤器 |
| Aggregate Workflows | 数据聚合 |
| Select Workflows | 表单 |
| Select Matching Workflows | 数据合并 |
| Split Out Workflows | 数据拆分 |
| Create JSON Workflow Options | Code |
| Split Out | 数据拆分 |
| Route Mode | Switch 路由 |
| Strip Incompatible API Fields1 | Code |
| Filter Our Archived Items1 | 过滤器 |
| Select Workflows1 | 表单 |
| Select Matching Workflows1 | 数据合并 |
| Split Out Workflows1 | 数据拆分 |
| Create JSON Workflow Options1 | Code |
| Get Instance Information | Notion |
| Create JSON Workflow Options2 | Code |
| Set Source Name and URL | 数据设置 |
| Select Workflows2 | 表单 |
| Set Source | 数据设置 |
| Set Target | 数据设置 |
| Merge Source and Target | 数据合并 |
| Source and Target | 数据聚合 |
| Merge Source Instance | 数据合并 |
| Merge Target Instance | 数据合并 |
| Create Workflow(s) | HTTP Request |
| Create Workflow(s)1 | n8n |
| Set Workflow Display Name (Dynamic) | 数据设置 |
| Set Workflow Display Name (Static) | 数据设置 |
| Aggregate Workflows (Dynamic) | 数据聚合 |
| Aggregate Workflows (Static) | 数据聚合 |
| Results (Dynamic) | 表单 |
| Results (Static) | 表单 |
| Aggregate Workflow Options (Static) | 数据聚合 |
| Aggregate Workflow Options (Dynamic) | 数据聚合 |
| Get All Source Instance Workflows | n8n |
| Get Source Workflows With Pagination | HTTP Request |
| Get Workflow JSON(s) | n8n |
| Get Workflow JSON(s)1 | HTTP Request |

## 触发方式
- On form submission 触发

## 统计
- 节点总数：40
- 触发节点：1
- 处理节点：36
- 输出节点：3
- 分类：devops
