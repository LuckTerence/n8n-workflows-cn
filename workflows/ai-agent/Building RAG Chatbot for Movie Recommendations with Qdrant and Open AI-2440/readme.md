## 简介
**Building RAG Chatbot for Movie Recommendations with Qdrant and Open AI**

（待补充中文描述）

> 分类：AI Agent | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2440

---

# Building RAG Chatbot for Movie Recommendations with Qdrant and Open AI


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Test workflow’ | 手动触发 |
| GitHub | github |
| Extract from File | 从文件提取 |
| Embeddings OpenAI | OpenAI Embeddings |
| Default Data Loader | 文档加载器 |
| Token Splitter | textSplitterTokenSplitter |
| Qdrant Vector Store | Qdrant 向量存储 |
| When chat message received | Chat 触发器 |
| OpenAI Chat Model | OpenAI Chat Model |
| Call n8n Workflow Tool | 工作流工具 |
| Window Buffer Memory | 记忆缓冲区 |
| Execute Workflow Trigger | 执行工作流触发器 |
| Merge | 数据合并 |
| Split Out | 数据拆分 |
| Split Out1 | 数据拆分 |
| Merge1 | 数据合并 |
| Aggregate | 数据聚合 |
| AI Agent | AI Agent |
| Embedding Recommendation Request with Open AI | HTTP Request |
| Embedding Anti-Recommendation Request with Open AI | HTTP Request |
| Extracting Embedding | 数据设置 |
| Extracting Embedding1 | 数据设置 |
| Calling Qdrant Recommendation API | HTTP Request |
| Retrieving Recommended Movies Meta Data | HTTP Request |
| Selecting Fields Relevant for Agent | 数据设置 |



## 功能说明

RAG 检索增强生成系统，基于文档向量库的知识问答。

Chat 消息触发、手动触发，通过 Git + HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：25
- 触发方式：手动触发, Chat 消息触发

## 触发方式
- When clicking ‘Test workflow’ 触发
- When chat message received 触发
- Execute Workflow Trigger 触发

## 统计
- 节点总数：25
- 触发节点：3
- 处理节点：18
- 输出节点：4
- 分类：ai-agent
