## 简介
**Automated Task Generation from Blueprints with Baserow & Weekend-Aware Scheduling**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：8 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/8602

---

# Automated Task Generation from Blueprints with Baserow & Weekend-Aware Scheduling


## 节点清单

| 节点 | 类型 |
|------|------|
| Generate tasks in batch | HTTP Request |
| Aggregate tasks for insert | 数据聚合 |
| Error response | 响应 Webhook |
| Get all template steps | baserow |
| Trigger task creation | Webhook |
| Avoid scheduling during the weekend | Code |
| Calculate deadlines for each step | 数据设置 |
| Configure settings and ids | 数据设置 |
| Success response | 响应 Webhook |

## 触发方式
- Trigger task creation 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：5
- 输出节点：3
- 分类：workflow-automation
