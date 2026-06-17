## 简介
**Fetch and enrich Apollo leads and sync verified contacts to MeldFlow-GHL**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 节点数：11 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/15684

---

# Fetch and enrich Apollo leads and sync verified contacts to MeldFlow-GHL


## 节点清单

| 节点 | 类型 |
|------|------|
| If Apollo Email Verified | IF 判断 |
| Update Page Number | Google Sheets |
| Apollo-Enrichment1 | HTTP Request |
| Wait1 | 等待 |
| Loop Over for batching limit | 分批处理 |
| Meldflow-Contacts | HTTP Request |
| Wait | 等待 |
| Schedule Trigger | 定时触发器 |
| Apollo lead search | HTTP Request |
| Data Filtering & Formatting | 数据设置 |
| Extract ID | Code |
| Get Apollo Page | Google Sheets |

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：8
- 输出节点：3
- 分类：workflow-automation
