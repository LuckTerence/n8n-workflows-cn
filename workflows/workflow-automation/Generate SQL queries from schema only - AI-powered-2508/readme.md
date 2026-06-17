## 简介
**Generate SQL queries from schema only - AI-powered**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：18 | 难度：⭐⭐⭐ 高级
> 原始来源：https://n8nworkflows.xyz/workflows/2508

---

# Generate SQL queries from schema only - AI-powered


## 节点清单

| 节点 | 类型 |
|------|------|
| OpenAI Chat Model | OpenAI Chat Model |
| Window Buffer Memory | 记忆缓冲区 |
| No Operation, do nothing | 空操作 |
| List all tables in a database | MySQL |
| Extract database schema | MySQL |
| Add table name to output | 数据设置 |
| Convert data to binary | 转换为文件 |
| Save file locally | 读写文件 |
| Extract data from file | 从文件提取 |
| Chat Trigger | Chat 触发器 |
| AI Agent | AI Agent |
| When clicking "Test workflow" | 手动触发 |
| Combine schema data and chat input | 数据设置 |
| Load the schema from the local file | 读写文件 |
| Extract SQL query | 数据设置 |
| Check if query exists | IF 判断 |
| Format query results | 数据设置 |
| Run SQL query | MySQL |
| Prepare final output | 数据设置 |
| Combine query result and chat answer | 数据合并 |

## 触发方式
- Chat Trigger 触发
- When clicking "Test workflow" 触发

## 统计
- 节点总数：20
- 触发节点：2
- 处理节点：18
- 输出节点：0
- 分类：workflow-automation
