## 简介
**Log errors and audit events with n8n Data Tables**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
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



## 功能说明

Log errors and audit events with n8n Data Tables。

定时触发，通过 工作流编排 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

无需额外 API Key，导入即可运行。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：12
- 触发方式：定时触发

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
