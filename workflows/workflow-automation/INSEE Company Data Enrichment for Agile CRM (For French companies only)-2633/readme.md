## 简介
**INSEE Company Data Enrichment for Agile CRM (For French companies only)**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：8 | 难度：⭐⭐ 进阶
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

## 触发方式
- When clicking ‘Test workflow’ 触发
- Schedule Trigger 触发

## 统计
- 节点总数：10
- 触发节点：2
- 处理节点：6
- 输出节点：2
- 分类：workflow-automation
