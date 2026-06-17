## 简介
**Conversing with Data: Transforming Text into SQL Queries and Visual Curves**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3497

---

# Conversing with Data: Transforming Text into SQL Queries and Visual Curves


## 节点清单

| 节点 | 类型 |
|------|------|
| Window Buffer Memory | 记忆缓冲区 |
| No Operation, do nothing | 空操作 |
| Add table name to output | 数据设置 |
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
| Prepare final output | 数据设置 |
| Combine query result and chat answer | 数据合并 |
| List all tables in a database | PostgreSQL |
| Convert data to Json | 转换为文件 |
| Schema Extractor | PostgreSQL |
| Final SQL result | PostgreSQL |
| Edit Fields | 数据设置 |
| Structured Output Parser | 结构化输出解析器 |
| Edit Fields1 | 数据设置 |
| plot agent | AI Agent |
| deepseek-chat | OpenAI Chat Model |
| Deepseek-chat | OpenAI Chat Model |



## 功能说明

表单问卷工具，自动收集和处理用户反馈。

Chat 消息触发、手动触发，通过 数据库 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com
- 数据库连接信息

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：25
- 触发方式：Chat 消息触发, 手动触发

## 触发方式
- Chat Trigger 触发
- When clicking "Test workflow" 触发

## 统计
- 节点总数：25
- 触发节点：2
- 处理节点：23
- 输出节点：0
- 分类：workflow-automation
