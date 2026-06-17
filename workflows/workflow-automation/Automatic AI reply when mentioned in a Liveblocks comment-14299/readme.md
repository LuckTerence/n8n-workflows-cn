## 简介
**Automatic AI reply when mentioned in a Liveblocks comment**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/14299

---

# Automatic AI reply when mentioned in a Liveblocks comment


## 节点清单

| 节点 | 类型 |
|------|------|
| Liveblocks Trigger | liveblocksTrigger |
| Get a comment | liveblocks |
| If | IF 判断 |
| Get a thread | liveblocks |
| AI Agent | AI Agent |
| Anthropic Chat Model | OpenAI Chat Model |
| Create a comment | liveblocks |

## 触发方式
- Liveblocks Trigger 触发

## 统计
- 节点总数：7
- 触发节点：1
- 处理节点：6
- 输出节点：0
- 分类：workflow-automation
