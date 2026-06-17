## 简介
**Scan Confluence pages with the REST API for inactive page owners**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：13 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/12238

---

# Scan Confluence pages with the REST API for inactive page owners


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Execute workflow’ | 手动触发 |
| Set Variables | 数据设置 |
| Confluence - Get Spaces | HTTP Request |
| Format Space Ids | 数据设置 |
| Confluence - Get Pages | HTTP Request |
| Confluence - Bulk User Lookup | HTTP Request |
| Merge | 数据合并 |
| Filter Inactive Owners | 过滤器 |
| Split Out Users | 数据拆分 |
| Split Out Pages | 数据拆分 |
| Format unique ownerIds | 数据设置 |
| Filter Inactive Pages | 过滤器 |
| Aggregate | 数据聚合 |
| Set Report Data | 数据设置 |

## 触发方式
- When clicking ‘Execute workflow’ 触发

## 统计
- 节点总数：14
- 触发节点：1
- 处理节点：10
- 输出节点：3
- 分类：devops
