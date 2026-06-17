# Find KlickTipp tags to remove by prefix

https://n8nworkflows.xyz/workflows/13664

## 节点清单

| 节点 | 类型 |
|------|------|
| Input: Prefix + Tags to keep | 执行工作流触发器 |
| List all tags | Klicktipp |
| Match keep vs all tags | 数据合并 |
| Collect tags to remove | 数据聚合 |
| Keep only tags with prefix | 过滤器 |
| Build prefixed tag names | 数据设置 |
| Split prefixed tags | 数据拆分 |
| Set tagNamesToRemove | 数据设置 |

## 触发方式
- Input: Prefix + Tags to keep 触发

## 统计
- 节点总数：8
- 触发节点：1
- 处理节点：7
- 输出节点：0
- 分类：workflow-automation
