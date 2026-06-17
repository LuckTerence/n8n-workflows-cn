## 简介
**Generate stale page reports for Confluence spaces with REST API v1 and v2**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/12237

---

# Generate stale page reports for Confluence spaces with REST API v1 and v2


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Execute workflow’ | 手动触发 |
| Set Variables | 数据设置 |
| Confluence - Get Spaces | HTTP Request |
| Format Space Ids | 数据设置 |
| Confluence - Get Outdated Spaces via CQL | HTTP Request |
| Filter Version by cutoffDate | 过滤器 |
| Switch API Version | Switch 路由 |
| Set Report Data V2 | 数据设置 |
| Set Report Data V1 | 数据设置 |
| Split Out Pages V1 | 数据拆分 |
| Split Out Pages V2 | 数据拆分 |
| Aggregate | 数据聚合 |
| Confluence - Get Pages | HTTP Request |

## 触发方式
- When clicking ‘Execute workflow’ 触发

## 统计
- 节点总数：13
- 触发节点：1
- 处理节点：9
- 输出节点：3
- 分类：workflow-automation
