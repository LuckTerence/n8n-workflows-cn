## 简介
**Smarter RAG Agents with Enriched Retrieval and Modular Workflows**

（待补充中文描述）

> 分类：知识库 RAG | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/8008

---

# Smarter RAG Agents with Enriched Retrieval and Modular Workflows


## 节点清单

| 节点 | 类型 |
|------|------|
| Default Data Loader | 文档加载器 |
| Recursive Character Text Splitter | 文本分割器 |
| Delete Old Doc Rows | Supabase |
| When chat message received | Chat 触发器 |
| Insert into Supabase Vectorstore | Supabase 向量存储 |
| Embeddings Google Gemini1 | Google Gemini Embeddings |
| On form submission | 表单触发器 |
| Extract from File | 从文件提取 |
| Loop Over Items | 分批处理 |
| Get many rows | Supabase |
| Update a row | Supabase |
| Merge | 数据合并 |
| Wait | 等待 |
| Set File Data | 数据设置 |
| Metadata Obtention | OpenAI Chat Model |
| Schedule Trigger | 定时触发器 |
| Edit Fields | 数据设置 |
| Query Builder | OpenAI Chat Model |
| RAG Agent | AI Agent |
| Reranker | rerankerCohere |
| Google Gemini 2.0 Flash | OpenAI Chat Model |
| Postgres Chat Memory | PostgreSQL 聊天记忆 |
| Embeddings Google Gemini | Google Gemini Embeddings |
| Supabase Vector Store | Supabase 向量存储 |



## 功能说明

RAG 检索增强生成系统，基于文档向量库的知识问答，定时执行。

定时触发、Chat 消息触发，通过 数据库 实现自动化。

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

- 节点总数：24
- 触发方式：Chat 消息触发, 表单提交触发, 定时触发

## 触发方式
- When chat message received 触发
- On form submission 触发
- Schedule Trigger 触发

## 统计
- 节点总数：24
- 触发节点：3
- 处理节点：21
- 输出节点：0
- 分类：knowledge-rag
