# Simple Google indexing Workflow in N8N

https://n8nworkflows.xyz/workflows/2123

## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking "Execute Workflow" | 手动触发 |
| Schedule Trigger | 定时触发器 |
| loop | 分批处理 |
| sitemap_set | HTTP Request |
| sitemap_convert | XML |
| sitemap_parse | 数据拆分 |
| url_set | 数据设置 |
| url_index | HTTP Request |
| index_check | IF 判断 |
| wait | 等待 |
| Stop and Error | 停止并报错 |

## 触发方式
- When clicking "Execute Workflow" 触发
- Schedule Trigger 触发

## 统计
- 节点总数：11
- 触发节点：2
- 处理节点：7
- 输出节点：2
- 分类：workflow-automation
