# Chat with your PDF documents using PageIndex vectorless RAG via Telegram

https://n8nworkflows.xyz/workflows/13977

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
