## 简介
**Check dependencies before completing Awork tasks (Workaround)**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4350

---

# Check dependencies before completing Awork tasks (Workaround)


## 节点清单

| 节点 | 类型 |
|------|------|
| Load dependencies for task | HTTP Request |
| Aggregate task dependencies | 数据聚合 |
| Workflow config | 数据设置 |
| Fetch task changes | 数据设置 |
| Split out task changes | 数据拆分 |
| Filter task status change | 过滤器 |
| Check if task done | IF 判断 |
| Webhook call by Awork | Webhook |
| Check if dependencies enabled | IF 判断 |
| Load all linked tasks | HTTP Request |
| Build filter params | Code |
| Filter only open tasks | 过滤器 |
| Aggregate open task IDs | 数据聚合 |
| Check if open tasks exist | IF 判断 |
| Check if comments are enabled | IF 判断 |
| Add comment to tasks | HTTP Request |
| Check if tree structure enabled | IF 判断 |
| Check subtasks | IF 判断 |
| Roll back task status from done to previous state | HTTP Request |
| Load all open sub tasks | HTTP Request |
| Aggregate task IDs | 数据聚合 |
| Check open subtasks | IF 判断 |
| Check if comments are enabled1 | IF 判断 |
| Add comment to tasks1 | HTTP Request |
| Roll back task status from done to previous state1 | HTTP Request |



## 功能说明

Check dependencies before completing Awork tasks (。

Webhook触发，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

无需额外 API Key，导入即可运行。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：25
- 触发方式：Webhook 触发

## 触发方式
- Webhook call by Awork 触发

## 统计
- 节点总数：25
- 触发节点：1
- 处理节点：17
- 输出节点：7
- 分类：workflow-automation
