## 简介
**Build an On-Premises AI Kaggle Competition Assistant with Qdrant RAG and Ollama**

（待补充中文描述）

> 分类：知识库 RAG | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3967

---

# Build an On-Premises AI Kaggle Competition Assistant with Qdrant RAG and Ollama


## 节点清单

| 节点 | 类型 |
|------|------|
| Local File Trigger | localFileTrigger |
| Default Data Loader | 文档加载器 |
| Recursive Character Text Splitter | 文本分割器 |
| Settings | 数据设置 |
| Merge | 数据合并 |
| Get FileType | Switch 路由 |
| Import File | 读写文件 |
| Extract from TEXT | 从文件提取 |
| Summarization Chain | chainSummarization |
| Qdrant Vector Store | Qdrant 向量存储 |
| Markdown | Markdown |
| Embeddings Ollama | Ollama Embeddings |
| Ollama Summarizer | lmOllama |
| When chat message received | Chat 触发器 |
| AI Agent | AI Agent |
| Vector Store Tool | 向量存储工具 |
| Window Buffer Memory | 记忆缓冲区 |
| Qdrant Vector Store2 | Qdrant 向量存储 |
| Ollama Chat Model3 | Ollama Chat Model |
| Embeddings Ollama2 | Ollama Embeddings |
| Ollama Chat Model4 | Ollama Chat Model |



## 功能说明

RAG 检索增强生成系统，基于文档向量库的知识问答。

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

- 节点总数：21
- 触发方式：Chat 消息触发

## 触发方式
- Local File Trigger 触发
- When chat message received 触发

## 统计
- 节点总数：21
- 触发节点：2
- 处理节点：19
- 输出节点：0
- 分类：knowledge-rag
