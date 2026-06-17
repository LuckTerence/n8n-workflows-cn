## 简介
**Log errors and audit events with n8n Data Tables**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：11 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/15347

---

# Log errors and audit events with n8n Data Tables


## 节点清单

| 节点 | 类型 |
|------|------|
| Error Trigger - Global | 错误触发器 |
| Normalize Error Event | Code |
| Insert ErrorLog | 数据表 |
| Execute Workflow Trigger - Audit API | 执行工作流触发器 |
| Normalize Audit Event | Code |
| Insert AuditLog | 数据表 |
| Schedule Trigger - Daily Purge | 定时触发器 |
| Build Purge Config | Code |
| Delete old ErrorLog rows | 数据表 |
| Delete old AuditLog rows | 数据表 |
| Build Purge Audit Event | Code |
| Insert Purge AuditLog | 数据表 |

## 触发方式
- Error Trigger - Global 触发
- Execute Workflow Trigger - Audit API 触发
- Schedule Trigger - Daily Purge 触发

## 统计
- 节点总数：12
- 触发节点：3
- 处理节点：9
- 输出节点：0
- 分类：devops
