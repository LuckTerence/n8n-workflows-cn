## 简介
**Chat with PDF - MD - Text Files using GraphRAG (no vector store needed)**

（待补充中文描述）

> 分类：知识库 RAG | 适配等级：A（需替换Google Drive)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4755

---

# Chat with PDF - MD - Text Files using GraphRAG (no vector store needed)


## 节点清单

| 节点 | 类型 |
|------|------|
| Search Google Drive | Google Drive |
| Loop Over Items | 分批处理 |
| Retrieve File | Google Drive |
| Switch | Switch 路由 |
| Extract from PDF | 从文件提取 |
| Extract from Text File | 从文件提取 |
| Extract from Markdown | 从文件提取 |
| InfraNodus Save to Graph | HTTP Request |
| Map PDF to Text | 数据设置 |
| Convert File to PDF | HTTP Request |
| When chat message received | Chat 触发器 |
| AI Agent | AI Agent |
| OpenAI Chat Model | OpenAI Chat Model |
| Simple Memory | 记忆缓冲区 |
| Knowledge Base GraphRAG | HTTP Request 工具 |
| Click ‘Test workflow’ to ingest the documents | 手动触发 |



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

- 节点总数：16
- 触发方式：Chat 消息触发, 手动触发

## 触发方式
- When chat message received 触发
- Click ‘Test workflow’ to ingest the documents 触发

## 统计
- 节点总数：16
- 触发节点：2
- 处理节点：11
- 输出节点：3
- 分类：knowledge-rag
