# Create a Lookio RAG assistant from a CSV text corpus

https://n8nworkflows.xyz/workflows/11877

## 节点清单

| 节点 | 类型 |
|------|------|
| Convert to txt | 转换为文件 |
| Loop Over Items | 分批处理 |
| Convert CSV to JSON | 从文件提取 |
| Upload a CSV | 表单触发器 |
| Aggregate success messages | 数据聚合 |
| Convert IDs into an Array | 数据设置 |
| Success message form ending | 表单 |
| Create Lookio assistant | HTTP Request |
| Import resource to Lookio | HTTP Request |

## 触发方式
- Upload a CSV 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：6
- 输出节点：2
- 分类：knowledge-rag
