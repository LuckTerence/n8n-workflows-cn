## 简介
**Learn Data Synchronization: Warehouse Inventory Audit Tutorial**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5999

---

# Learn Data Synchronization: Warehouse Inventory Audit Tutorial


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



## 功能说明

AI 招聘助手，简历筛选或面试流程自动化。

手动触发，通过 工作流编排 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

无需额外 API Key，导入即可运行。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：10
- 触发方式：手动触发

## 触发方式
- Start Audit 触发

## 统计
- 节点总数：10
- 触发节点：1
- 处理节点：9
- 输出节点：0
- 分类：workflow-automation
