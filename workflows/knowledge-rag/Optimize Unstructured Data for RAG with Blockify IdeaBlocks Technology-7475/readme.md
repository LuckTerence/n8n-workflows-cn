## 简介
**Optimize Unstructured Data for RAG with Blockify IdeaBlocks Technology**

（待补充中文描述）

> 分类：知识库 RAG | 适配等级：A（需替换Google Drive)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/7475

---

# Optimize Unstructured Data for RAG with Blockify IdeaBlocks Technology


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Execute workflow’ | 手动触发 |
| Query Data Tool | vectorStoreInMemory |
| AI Agent | AI Agent |
| RAG Chatbot | Chat 触发器 |
| Chunk Text | Code |
| Loop Over Chunks | 分批处理 |
| Simple IdeaBlock Vector Store | vectorStoreInMemory |
| Default Data Loader | 文档加载器 |
| Embed Individual IdeaBlocks (Already Separated) | textSplitterCharacterTextSplitter |
| Embeddings OpenAI | OpenAI Embeddings |
| OpenAI Chat Model | OpenAI Chat Model |
| Extract Text from .TXT File | 从文件提取 |
| Download .TXT File for Ingest | Google Drive |
| Blockify Ingest API | HTTP Request |
| Extract IdeaBlocks from API Response | 数据设置 |



## 功能说明

RAG 检索增强生成系统，基于文档向量库的知识问答。

Chat 消息触发、手动触发，通过 HTTP API 实现自动化。

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

- 节点总数：15
- 触发方式：手动触发, Chat 消息触发

## 触发方式
- When clicking ‘Execute workflow’ 触发
- RAG Chatbot 触发

## 统计
- 节点总数：15
- 触发节点：2
- 处理节点：12
- 输出节点：1
- 分类：knowledge-rag
