## 简介
**Clone NocoDB tables and data to another base**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/15373

---

# Clone NocoDB tables and data to another base


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Execute workflow’ | 手动触发 |
| Config | 数据设置 |
| Create NocoDB Table | HTTP Request |
| Create Tables | 分批处理 |
| Prepare fields data for Insert | 数据设置 |
| Copy rows to new tables | 分批处理 |
| Fetch tables records | HTTP Request |
| Get Source Table Metadata | HTTP Request |
| Split tables | 数据拆分 |
| Fetch tables records1 | HTTP Request |
| Copy data over? | Switch 路由 |



## 功能说明

Clone NocoDB tables and data to another base。

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

- 节点总数：11
- 触发方式：手动触发

## 触发方式
- When clicking ‘Execute workflow’ 触发

## 统计
- 节点总数：11
- 触发节点：1
- 处理节点：6
- 输出节点：4
- 分类：workflow-automation
