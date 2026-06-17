## 简介
**Bulk enrich CSV contact lists with Lusha**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/13345

---

# Bulk enrich CSV contact lists with Lusha


## 节点清单

| 节点 | 类型 |
|------|------|
| Start Manually | 手动触发 |
| Read CSV File | 电子表格文件 |
| Batch into Groups of 100 | 分批处理 |
| Format Batch for Lusha | Code |
| Enrich contacts in bulk | lusha |
| Format Enriched Results | Code |
| Export Enriched CSV | 电子表格文件 |

## 触发方式
- Start Manually 触发

## 统计
- 节点总数：7
- 触发节点：1
- 处理节点：6
- 输出节点：0
- 分类：workflow-automation
