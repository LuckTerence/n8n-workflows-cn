## 简介
**Local Chatbot with Retrieval Augmented Generation (RAG)**

（待补充中文描述）

> 分类：AI Agent | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5148

---

# Local Chatbot with Retrieval Augmented Generation (RAG)


## 节点清单

| 节点 | 类型 |
|------|------|
| On form submission | 表单触发器 |
| Qdrant Vector Store | Qdrant 向量存储 |
| Embeddings Ollama | Ollama Embeddings |
| Default Data Loader | 文档加载器 |
| Recursive Character Text Splitter | 文本分割器 |
| When chat message received | Chat 触发器 |
| AI Agent | AI Agent |
| Ollama Chat Model | Ollama Chat Model |
| Simple Memory | 记忆缓冲区 |
| Qdrant Vector Store1 | Qdrant 向量存储 |
| Embeddings Ollama1 | Ollama Embeddings |



## 功能说明

RAG 检索增强生成系统，基于文档向量库的知识问答（Local)表单提交触发、Chat 消息触发，通过 n8n 内置节点实现自动化。

Chat 消息触发，通过 工作流编排 实现自动化。

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

- 节点总数：11
- 触发方式：表单提交触发, Chat 消息触发

## 触发方式
- On form submission 触发
- When chat message received 触发

## 统计
- 节点总数：11
- 触发节点：2
- 处理节点：9
- 输出节点：0
- 分类：ai-agent
