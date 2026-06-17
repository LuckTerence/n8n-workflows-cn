# Email Assistant: Convert Natural Language to SQL Queries with Phi4-mini and PostgreSQL

https://n8nworkflows.xyz/workflows/3761

## 节点清单

| 节点 | 类型 |
|------|------|
| Add table name to output | 数据设置 |
| Convert data to binary | 转换为文件 |
| Save file locally | 读写文件 |
| Extract data from file | 从文件提取 |
| Chat Trigger | Chat 触发器 |
| When clicking "Test workflow" | 手动触发 |
| Combine schema data and chat input | 数据设置 |
| Load the schema from the local file | 读写文件 |
| Extract SQL query | 数据设置 |
| Check if query exists | IF 判断 |
| Format query results | 数据设置 |
| Combine query result and chat answer | 数据合并 |
| List all columns in a table | PostgreSQL |
| List all tables in a database | PostgreSQL |
| Ollama Chat Model | Ollama Chat Model |
| Postgres | PostgreSQL |
| Add trailing semicolon | 数据设置 |
| Check for trailing semicolon | IF 判断 |
| WorkflowTrigger | 执行工作流触发器 |
| If ran manually | IF 判断 |
| If file exists or already retried generating it | IF 判断 |
| AI Agent | AI Agent |
| Format empty output | 数据设置 |

## 触发方式
- Chat Trigger 触发
- When clicking "Test workflow" 触发
- WorkflowTrigger 触发

## 统计
- 节点总数：23
- 触发节点：3
- 处理节点：20
- 输出节点：0
- 分类：workflow-automation
