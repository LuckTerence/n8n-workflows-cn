## 简介
**Auto-Sync Easy Redmine Tasks to Microsoft To-Do**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/8628

---

# Auto-Sync Easy Redmine Tasks to Microsoft To-Do


## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Trigger | 定时触发器 |
| Get To-Do in Specific List | microsoftToDo |
| Clean To-Do List | microsoftToDo |
| Just One Output after Deletion | Code |
| Get Easy Redmine Task by Filter | easyRedmine |
| Split Out Tasks | 数据拆分 |
| Add Easy Redmine Task Link to To-Do Description | Code |
| Create To-Do Tasks | microsoftToDo |



## 功能说明

Auto-Sync Easy Redmine Tasks to Microsoft To-Do。

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

- 节点总数：8
- 触发方式：定时触发

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：8
- 触发节点：1
- 处理节点：7
- 输出节点：0
- 分类：workflow-automation
