## 简介
**Build a PDF Search System with Mistral OCR and Weaviate DB**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/7339

---

# Build a PDF Search System with Mistral OCR and Weaviate DB


## 节点清单

| 节点 | 类型 |
|------|------|
| Cohere Embeddings | Cohere Embeddings |
| Document Loader | 文档加载器 |
| Cohere Reranker | rerankerCohere |
| MCP Knowledge Server | MCP 触发器 |
| Search Knowledge Base | vectorStoreWeaviate |
| Text Splitter | 文本分割器 |
| Upload PDF | 表单触发器 |
| Extract Text from PDF | mistralAi |
| Prepare Document Data | 数据设置 |
| Store in Vector Database | vectorStoreWeaviate |



## 功能说明

联网搜索工具，AI 驱动的信息检索和分析（Pdf)表单提交触发，通过 n8n 内置节点实现自动化。

，通过 工作流编排 实现自动化。

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

- 节点总数：10
- 触发方式：表单提交触发

## 触发方式
- MCP Knowledge Server 触发
- Upload PDF 触发

## 统计
- 节点总数：10
- 触发节点：2
- 处理节点：8
- 输出节点：0
- 分类：workflow-automation
