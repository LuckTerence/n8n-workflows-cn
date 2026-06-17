# Resolve and create KlickTipp tags from names with optional prefixes

https://n8nworkflows.xyz/workflows/13699

## 节点清单

| 节点 | 类型 |
|------|------|
| Find tags to create | 数据合并 |
| Find existing tags | 数据合并 |
| Combine existing & new tags | 数据合并 |
| Split tagNames into items | 数据拆分 |
| Map tagNames -> value | 数据设置 |
| Get tag list | Klicktipp |
| Create new tag | Klicktipp |
| Aggregate tag names | 数据聚合 |
| Extract tag name | 数据设置 |
| Input: Prefix + tag names | 执行工作流触发器 |
| Set the created tag | 数据设置 |

## 触发方式
- Input: Prefix + tag names 触发

## 统计
- 节点总数：11
- 触发节点：1
- 处理节点：10
- 输出节点：0
- 分类：workflow-automation
