# Learn Data Synchronization: Warehouse Inventory Audit Tutorial

https://n8nworkflows.xyz/workflows/5999

## 节点清单

| 节点 | 类型 |
|------|------|
| Start Audit | 手动触发 |
| ➕ Add to Warehouse B | 空操作 |
| Warehouse A (Source of Truth) | 数据设置 |
| ✅ All Good (Do Nothing) | 空操作 |
| 🔄 Update in Warehouse B | 空操作 |
| ❌ Remove from Warehouse B | 空操作 |
| The Auditor | compareDatasets |
| Warehouse B (To be Synced) | 数据设置 |
| Split Out Prducts (B) | 数据拆分 |
| Split Out Prducts (A) | 数据拆分 |

## 触发方式
- Start Audit 触发

## 统计
- 节点总数：10
- 触发节点：1
- 处理节点：9
- 输出节点：0
- 分类：workflow-automation
