## 简介
**Build Your Own Counseling Chatbot on LINE to Support Mental Health Conversations**

（待补充中文描述）

> 分类：AI Agent | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：7 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/2975

---

# Build Your Own Counseling Chatbot on LINE to Support Mental Health Conversations


## 节点清单

| 节点 | 类型 |
|------|------|
| Loading Animation | HTTP Request |
| ReplyMessage - Not supported | HTTP Request |
| AI Agent | AI Agent |
| Azure OpenAI Chat Model | Azure OpenAI Chat Model |
| ReplyMessage - Line | HTTP Request |
| Line Chatbot | Webhook |
| Check Message Type IsText? | IF 判断 |
| Format Reply | 数据设置 |

## 触发方式
- Line Chatbot 触发

## 统计
- 节点总数：8
- 触发节点：1
- 处理节点：4
- 输出节点：3
- 分类：ai-agent
