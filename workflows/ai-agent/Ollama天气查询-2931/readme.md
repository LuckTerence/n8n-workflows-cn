## 简介
**Ollama天气查询**

本地Ollama+天气查询+维基百科

> 分类：AI Agent | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2931

---

# Ollama天气查询


## 节点清单

| 节点 | 类型 |
|------|------|
| On new manual Chat Message | 手动聊天触发 |
| Wikipedia | Wikipedia 工具 |
| Window Buffer Memory | 记忆缓冲区 |
| AI Agent | AI Agent |
| Weather HTTP Request | HTTP 工具 |
| Ollama Chat Model | Ollama Chat Model |

## 触发方式
- On new manual Chat Message 触发

## 统计
- 节点总数：6
- 触发节点：1
- 处理节点：4
- 输出节点：1
- 分类：ai-agent
