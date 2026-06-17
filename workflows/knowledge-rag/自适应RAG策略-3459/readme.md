## 简介
**自适应RAG策略**

查询分类+Qdrant

> 分类：知识库 RAG | 适配等级：A（AI模型已适配，部分外服节点需手动替换为国内服务）
> 原始来源：https://n8nworkflows.xyz/workflows/3459

---

# 自适应RAG策略


## 节点清单

| 节点 | 类型 |
|------|------|
| Query Classification | AI Agent |
| Switch | Switch 路由 |
| Factual Strategy - Focus on Precision | AI Agent |
| Analytical Strategy - Comprehensive Coverage | AI Agent |
| Opinion Strategy - Diverse Perspectives | AI Agent |
| Contextual Strategy - User Context Integration | AI Agent |
| Chat | Chat 触发器 |
| Factual Prompt and Output | 数据设置 |
| Contextual Prompt and Output | 数据设置 |
| Opinion Prompt and Output | 数据设置 |
| Analytical Prompt and Output | 数据设置 |
| Gemini Classification | Google Gemini |
| Gemini Factual | Google Gemini |
| Gemini Analytical | Google Gemini |
| Chat Buffer Memory Analytical | 记忆缓冲区 |
| Chat Buffer Memory Factual | 记忆缓冲区 |
| Gemini Opinion | Google Gemini |
| Chat Buffer Memory Opinion | 记忆缓冲区 |
| Gemini Contextual | Google Gemini |
| Chat Buffer Memory Contextual | 记忆缓冲区 |
| Embeddings | Google Gemini Embeddings |
| Concatenate Context | 文本摘要 |
| Retrieve Documents from Vector Store | Qdrant 向量存储 |
| Set Prompt and Output | 数据设置 |
| Gemini Answer | Google Gemini |
| Answer | AI Agent |
| Chat Buffer Memory | 记忆缓冲区 |
| Respond to Webhook | 响应 Webhook |
| When Executed by Another Workflow | 执行工作流触发器 |
| Combined Fields | 数据设置 |



## 功能说明

RAG 检索增强生成系统，基于文档向量库的知识问答。

Chat 消息触发，通过 HTTP API 实现自动化。

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

- 节点总数：30
- 触发方式：Chat 消息触发

## 触发方式
- Chat 触发
- When Executed by Another Workflow 触发

## 统计
- 节点总数：30
- 触发节点：2
- 处理节点：27
- 输出节点：1
- 分类：knowledge-rag
