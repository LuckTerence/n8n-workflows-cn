## 简介
**Migrate large Hugging Face datasets to MongoDB with a looping subworkflow**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/12338

---

# Migrate large Hugging Face datasets to MongoDB with a looping subworkflow


## 节点清单

| 节点 | 类型 |
|------|------|
| Aggregate | 数据聚合 |
| setOffset | 数据设置 |
| SubTrigger | 执行工作流触发器 |
| HF_FetchRows | HTTP Request |
| Extract_Rows | 数据设置 |
| HasRows? | IF 判断 |
| Row_Splitter | 数据拆分 |
| Transform_RemoveId_AddMeta | Code |
| Mongo_InsertOrUpsert | MongoDB |
| Config_Start | 数据设置 |
| Trigger_Manual | 手动触发 |
| ContinueLoop? | IF 判断 |
| Stop | 空操作 |
| InsertBatch | 执行工作流 |
| NoRows_Offset | 数据设置 |



## 功能说明

n8n 工作流管理工具，编排控制工作流的启停。

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

- 节点总数：15
- 触发方式：手动触发

## 触发方式
- SubTrigger 触发
- Trigger_Manual 触发

## 统计
- 节点总数：15
- 触发节点：2
- 处理节点：12
- 输出节点：1
- 分类：workflow-automation
