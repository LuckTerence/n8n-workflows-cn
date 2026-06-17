## 简介
**Distribute Workflow Execution with Round-Robin Logic using Data Tables**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：8 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/10048

---

# Distribute Workflow Execution with Round-Robin Logic using Data Tables


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Execute workflow’ | 手动触发 |
| Code in JavaScript | Code |
| Route 2 | 空操作 |
| Round Robin Router | Switch 路由 |
| Route 1 | 空操作 |
| Route 3 | 空操作 |
| Calculate the next route to use | 数据表 |
| Update last_used in the datatable | 数据表 |
| Merge trigger data to pass to subworkflow if needed | 数据合并 |

## 触发方式
- When clicking ‘Execute workflow’ 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：8
- 输出节点：0
- 分类：devops
