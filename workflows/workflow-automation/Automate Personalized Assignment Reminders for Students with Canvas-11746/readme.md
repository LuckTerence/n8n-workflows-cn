## 简介
**Automate Personalized Assignment Reminders for Students with Canvas**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
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



## 功能说明

Automate Personalized Assignment Reminders for Stu。

手动触发，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

无需额外 API Key，导入即可运行。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：13
- 触发方式：手动触发

## 触发方式
- When clicking ‘Execute workflow’ 触发

## 统计
- 节点总数：13
- 触发节点：1
- 处理节点：8
- 输出节点：4
- 分类：workflow-automation
