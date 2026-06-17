## 简介
**Evaluation metric example: RAG document relevance**

（待补充中文描述）

> 分类：知识库 RAG | 适配等级：A（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4273

---

# Evaluation metric example: RAG document relevance


## 节点清单

| 节点 | 类型 |
|------|------|
| When fetching a dataset row | evaluationTrigger |
| Evaluating? | 条件评估 |
| When chat message received | Chat 触发器 |
| Match chat format | 数据设置 |
| Return chat response | 空操作 |
| Set metrics | 条件评估 |
| Get dataset | Google Sheets |
| Remove Duplicates | 去重 |
| Simple Vector Store | vectorStoreInMemory |
| Embeddings OpenAI | OpenAI Embeddings |
| Default Data Loader | 文档加载器 |
| Recursive Character Text Splitter | 文本分割器 |
| When clicking ‘Execute workflow’ | 手动触发 |
| Calculate doc relevance metric | OpenAI |
| AI Agent | AI Agent |
| OpenAI Chat Model | OpenAI Chat Model |
| Extract documents | 数据设置 |
| Simple Vector Store1 | vectorStoreInMemory |
| Embeddings OpenAI1 | OpenAI Embeddings |



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

- 节点总数：19
- 触发方式：Chat 消息触发, 手动触发

## 触发方式
- When fetching a dataset row 触发
- When chat message received 触发
- When clicking ‘Execute workflow’ 触发

## 统计
- 节点总数：19
- 触发节点：3
- 处理节点：16
- 输出节点：0
- 分类：knowledge-rag
