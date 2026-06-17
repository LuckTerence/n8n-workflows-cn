# Extract sitemap URLs in bulk via chat and export them to a CSV download link

https://n8nworkflows.xyz/workflows/15444

## 节点清单

| 节点 | 类型 |
|------|------|
| Listen for Bulk URLs | Chat 触发器 |
| Fetch XML Data | HTTP Request |
| Parse & Validate URLs | Code |
| Check for Validation Errors | IF 判断 |
| Alert User: Invalid URLs | 聊天 |
| Cache Validated URLs | Code |
| Format Successful Data | Code |
| Aggregate Successful Data | 数据聚合 |
| Delay Chat Sequence | 等待 |
| Alert User: Accessible URLs | 聊天 |
| Isolate Failed URLs | 数据拆分 |
| Aggregate Failed URLs | 数据聚合 |
| Alert User: Failed URLs | 聊天 |
| Process Each Sitemap | 分批处理 |
| Parse XML Data | XML |
| Scan for Sitemap Indexes | Code |
| Check if Nested Index | IF 判断 |
| Alert User: Nested Index Found | 聊天 |
| Isolate Individual URLs | 数据拆分 |
| Standardize URL Data | 数据设置 |
| Generate CSV File | 转换为文件 |
| Upload CSV to Host | HTTP Request |
| Extract Download URL | Code |
| Send Download Link | 聊天 |

## 触发方式
- Listen for Bulk URLs 触发

## 统计
- 节点总数：24
- 触发节点：1
- 处理节点：16
- 输出节点：7
- 分类：workflow-automation
