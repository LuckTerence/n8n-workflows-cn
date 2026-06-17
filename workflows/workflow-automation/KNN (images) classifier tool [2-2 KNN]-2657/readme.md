# KNN (images) classifier tool [2-2 KNN]

https://n8nworkflows.xyz/workflows/2657

## 节点清单

| 节点 | 类型 |
|------|------|
| Embed image | HTTP Request |
| Query Qdrant | HTTP Request |
| Majority Vote | Code |
| Increase limitKNN | 数据设置 |
| Propagate loop variables | 数据设置 |
| Image Test URL | 数据设置 |
| Return class | 数据设置 |
| Check tie | IF 判断 |
| Qdrant variables + embedding + KNN neigbours | 数据设置 |
| Execute Workflow Trigger | 执行工作流触发器 |

## 触发方式
- Execute Workflow Trigger 触发

## 统计
- 节点总数：10
- 触发节点：1
- 处理节点：7
- 输出节点：2
- 分类：workflow-automation
