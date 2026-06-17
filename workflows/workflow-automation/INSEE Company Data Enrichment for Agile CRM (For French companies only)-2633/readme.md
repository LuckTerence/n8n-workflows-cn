## 简介
**INSEE Company Data Enrichment for Agile CRM (For French companies only)**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2633

---

# INSEE Company Data Enrichment for Agile CRM (For French companies only)


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Test workflow’ | 手动触发 |
| Find Company in SIREN database | HTTP Request |
| Request all data from SIREN database | HTTP Request |
| FilterOut all Company that have the ReadOnly Key set | Code |
| Set Insee API Key | 数据设置 |
| Schedule Trigger | 定时触发器 |
| clean_route | 空操作 |
| Get all Compagnies from Agile CRM | agileCrm |
| Enrich CRM with INSEE Data | agileCrm |
| Merge data from CRM and SIREN database with enriched for the CRM | 数据合并 |



## 功能说明

客户关系管理工具，自动管理销售线索和客户数据，定时执行。

定时触发、手动触发，通过 HTTP API 实现自动化。

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
- 触发方式：手动触发, 定时触发

## 触发方式
- When clicking ‘Test workflow’ 触发
- Schedule Trigger 触发

## 统计
- 节点总数：10
- 触发节点：2
- 处理节点：6
- 输出节点：2
- 分类：workflow-automation
