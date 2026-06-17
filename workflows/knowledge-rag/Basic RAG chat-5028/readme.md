## 简介
**Basic RAG chat**

（待补充中文描述）

> 分类：知识库 RAG | 适配等级：A（需替换Pinecone/Google Drive)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5028

---

# Basic RAG chat


## 节点清单

| 节点 | 类型 |
|------|------|
| Recursive Character Text Splitter | 文本分割器 |
| Default Data Loader | 文档加载器 |
| Question and Answer Chain | chainRetrievalQa |
| Vector Store Retriever | retrieverVectorStore |
| When clicking 'Test Workflow' button | 手动触发 |
| When clicking 'Chat' button below | Chat 触发器 |
| Read/Write Files from Disk | 读写文件 |
| In-Memory Vector Store1 | vectorStoreInMemory |
| In-Memory Vector Store | vectorStoreInMemory |
| Embeddings Cohere | Cohere Embeddings |
| Groq Chat Model | Groq Chat Model |
| Embeddings Cohere1 | Cohere Embeddings |



## 功能说明

RAG 检索增强生成系统，基于文档向量库的知识问答。

Chat 消息触发、手动触发，通过 工作流编排 实现自动化。

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

- 节点总数：12
- 触发方式：手动触发, Chat 消息触发

## 触发方式
- When clicking 'Test Workflow' button 触发
- When clicking 'Chat' button below 触发

## 统计
- 节点总数：12
- 触发节点：2
- 处理节点：10
- 输出节点：0
- 分类：knowledge-rag
