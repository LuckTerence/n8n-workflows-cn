# Store variables between workflow runs using data tables as a key-value store

https://n8nworkflows.xyz/workflows/13442

## 节点清单

| 节点 | 类型 |
|------|------|
| Create Globals table | 数据表 |
| Stop and Error | 停止并报错 |
| If not the expected error | IF 判断 |
| Global found | IF 判断 |
| When clicking ‘Execute workflow’ | 手动触发 |
| Get Global "your_variable_name" | 数据表 |
| Set default value | 数据设置 |
| Format value | 数据设置 |
| Do something | 空操作 |
| Upsert Global "your_variable_name" | 数据表 |

## 触发方式
- When clicking ‘Execute workflow’ 触发

## 统计
- 节点总数：10
- 触发节点：1
- 处理节点：9
- 输出节点：0
- 分类：workflow-automation
