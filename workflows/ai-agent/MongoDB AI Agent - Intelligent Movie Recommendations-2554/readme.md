## 简介
**MongoDB AI Agent - Intelligent Movie Recommendations**

（待补充中文描述）

> 分类：AI Agent | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2554

---

# MongoDB AI Agent - Intelligent Movie Recommendations


## 节点清单

| 节点 | 类型 |
|------|------|
| OpenAI Chat Model | OpenAI Chat Model |
| MongoDBAggregate | mongoDbTool |
| Window Buffer Memory | 记忆缓冲区 |
| When chat message received | Chat 触发器 |
| insertFavorite | 工作流工具 |
| AI Agent - Movie Recommendation | AI Agent |

## 触发方式
- When chat message received 触发

## 统计
- 节点总数：6
- 触发节点：1
- 处理节点：5
- 输出节点：0
- 分类：ai-agent
