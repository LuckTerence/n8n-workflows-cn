## 简介
**Gmail客服自动回复**

Ollama+Pinecone RAG

> 分类：工作流自动化 | 适配等级：A（需替换Pinecone/Gmail)（AI模型已本地化Ollama，Pinecone/Gmail需手动替换）
> 原始来源：https://n8nworkflows.xyz/workflows/4760

---

# Gmail客服自动回复


## 节点清单

| 节点 | 类型 |
|------|------|
| Gmail Trigger | Gmail 触发器 |
| Text Classifier | 文本分类器 |
| AI Agent | AI Agent |
| Pinecone Vector Store | Pinecone 向量存储 |
| Label | Gmail |
| Send | Gmail |
| Ollama Model | lmOllama |
| Embeddings Ollama | Ollama Embeddings |
| Ollama Chat Model | Ollama Chat Model |
| Simple Memory | 记忆缓冲区 |



## 功能说明

邮件自动化处理，AI 分类整理或。

定时触发、手动触发，通过 邮箱 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com
- 邮箱 SMTP/IMAP 账号密码

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：10
- 触发方式：手动或子流程调用

## 触发方式
- Gmail Trigger 触发

## 统计
- 节点总数：10
- 触发节点：1
- 处理节点：9
- 输出节点：0
- 分类：workflow-automation
