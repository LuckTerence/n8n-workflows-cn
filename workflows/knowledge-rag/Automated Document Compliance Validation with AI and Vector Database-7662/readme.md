## 简介
**Automated Document Compliance Validation with AI and Vector Database**

（待补充中文描述）

> 分类：知识库 RAG | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/7662

---

# Automated Document Compliance Validation with AI and Vector Database


## 节点清单

| 节点 | 类型 |
|------|------|
| Audit Document Upload | Webhook |
| Procedure Submission | Webhook |
| Fetch Document (Microsoft Graph) | HTTP Request |
| Delete Old Document Vectors | Code |
| Extract PDF Text | 从文件提取 |
| Generate Document Embeddings | Ollama Embeddings |
| Insert Vectors into Qdrant | Qdrant 向量存储 |
| Load Document Metadata | 文档加载器 |
| Split Text into Chunks | 文本分割器 |
| Format Procedure Payload | Code |
| AI Compliance Validator | AI Agent |
| Language Model (AI Agent) | Ollama Chat Model |
| Retrieve Relevant Document Chunks | Qdrant 向量存储 |
| Generate Query Embeddings | Ollama Embeddings |
| Language Model (Structured Output) | Ollama Chat Model |
| Parse AI Response | 结构化输出解析器 |
| Return Compliance Report | 响应 Webhook |



## 功能说明

数据库操作工具，自动查询或写入数据库，Webhook 触发。

Webhook触发，通过 HTTP API 实现自动化。

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

- 节点总数：17
- 触发方式：Webhook 触发

## 触发方式
- Audit Document Upload 触发
- Procedure Submission 触发

## 统计
- 节点总数：17
- 触发节点：2
- 处理节点：13
- 输出节点：2
- 分类：knowledge-rag
