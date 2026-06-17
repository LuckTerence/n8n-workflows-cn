## 简介
**Extract and self-correct meeting action items with OpenRouter and webhooks**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：9 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/15995

---

# Extract and self-correct meeting action items with OpenRouter and webhooks


## 节点清单

| 节点 | 类型 |
|------|------|
| Webhook - Meeting Notes | Webhook |
| Normalize Request | Code |
| Extraction Agent | AI Agent |
| Window Buffer Memory | 记忆缓冲区 |
| Parse + Validate | Code |
| Validated or Max Attempts? | IF 判断 |
| Finalize Response | Code |
| Respond to Client | 响应 Webhook |
| Increment + Feedback | Code |
| OpenRouter Chat Model | OpenRouter Chat Model |

## 触发方式
- Webhook - Meeting Notes 触发

## 统计
- 节点总数：10
- 触发节点：1
- 处理节点：8
- 输出节点：1
- 分类：workflow-automation
