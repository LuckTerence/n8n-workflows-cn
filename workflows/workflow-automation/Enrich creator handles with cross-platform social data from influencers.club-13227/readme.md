# Enrich creator handles with cross-platform social data from influencers.club

https://n8nworkflows.xyz/workflows/13227

## 节点清单

| 节点 | 类型 |
|------|------|
| Daily Refresh Schedule | 定时触发器 |
| Process in Batches | 分批处理 |
| Wait 5 Second | 等待 |
| Update Null Values Only | HTTP Request |
| Update a row | Supabase |
| List Influencers Without Enrichment | Supabase |
| Influencers.club Enrichment API By Handle | HTTP Request |
| Normalize Creator Enrichment Payload | Code |

## 触发方式
- Daily Refresh Schedule 触发

## 统计
- 节点总数：8
- 触发节点：1
- 处理节点：5
- 输出节点：2
- 分类：workflow-automation
