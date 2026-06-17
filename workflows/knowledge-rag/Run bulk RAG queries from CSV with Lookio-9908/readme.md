# Run bulk RAG queries from CSV with Lookio

https://n8nworkflows.xyz/workflows/9908

## 节点清单

| 节点 | 类型 |
|------|------|
| On form submission | 表单触发器 |
| Valid Query column? | IF 判断 |
| Error message | 表单 |
| Isolate the Query column | 数据设置 |
| Lookio API call | HTTP Request |
| Prepare output | 数据设置 |
| Generate enriched CSV | 转换为文件 |
| Form ending and file download | 表单 |
| Loop Over Queries | 分批处理 |
| Split Out | 数据拆分 |
| Aggregate rows | 数据聚合 |
| Extract all rows | 从文件提取 |

## 触发方式
- On form submission 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：10
- 输出节点：1
- 分类：knowledge-rag
