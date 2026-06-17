## 简介
**Migrate large Hugging Face datasets to MongoDB with a looping subworkflow**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：14 | 难度：⭐⭐ 进阶
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

## 触发方式
- SubTrigger 触发
- Trigger_Manual 触发

## 统计
- 节点总数：15
- 触发节点：2
- 处理节点：12
- 输出节点：1
- 分类：workflow-automation
