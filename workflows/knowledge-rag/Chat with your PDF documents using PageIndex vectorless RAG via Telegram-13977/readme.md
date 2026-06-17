## 简介
**Chat with your PDF documents using PageIndex vectorless RAG via Telegram**

（待补充中文描述）

> 分类：知识库 RAG | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/13977

---

# Chat with your PDF documents using PageIndex vectorless RAG via Telegram


## 节点清单

| 节点 | 类型 |
|------|------|
| Receive PDF Document | Telegram 触发器 |
| Download PDF File | Telegram |
| Index PDF on PageIndex | HTTP Request |
| Receive User Question | Telegram 触发器 |
| Fetch All Indexed Documents | HTTP Request |
| Extract Document IDs | 数据设置 |
| LLM Reasoning over Document Tree | HTTP Request |
| Send Answer to User | Telegram |

## 触发方式
- Receive PDF Document 触发
- Receive User Question 触发

## 统计
- 节点总数：8
- 触发节点：2
- 处理节点：1
- 输出节点：5
- 分类：knowledge-rag
