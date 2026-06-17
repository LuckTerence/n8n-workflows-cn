## 简介
**Chat with PDF - MD - Text Files using GraphRAG (no vector store needed)**

（待补充中文描述）

> 分类：知识库 RAG | 适配等级：A（需替换Google Drive)（基本改完，配置 API Key 应该就能跑）
> 节点数：14 | 难度：⭐⭐ 进阶
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

## 触发方式
- When chat message received 触发
- Click ‘Test workflow’ to ingest the documents 触发

## 统计
- 节点总数：16
- 触发节点：2
- 处理节点：11
- 输出节点：3
- 分类：knowledge-rag
