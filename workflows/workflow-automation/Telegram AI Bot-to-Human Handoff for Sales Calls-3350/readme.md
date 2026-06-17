## 简介
**Telegram AI Bot-to-Human Handoff for Sales Calls**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A-adapted（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3350

---

# Telegram AI Bot-to-Human Handoff for Sales Calls


## 节点清单

| 节点 | 类型 |
|------|------|
| Human Handoff using Send and Wait | Telegram |
| Set Interaction to Bot | Redis |
| Set Interaction to Human | Redis |
| Get Interaction State | Redis |
| Model | OpenAI Chat Model |
| Memory | memoryRedisChat |
| Handoff Subworkflow | 执行工作流触发器 |
| Telegram Trigger | Telegram 触发器 |
| Send Response | Telegram |
| Switch Interaction | Switch 路由 |
| Information Extractor | 信息提取器 |
| OpenAI Chat Model | OpenAI Chat Model |
| With Defaults | Code |
| Has All Criteria? | IF 判断 |
| Onboarding Agent | AI Agent |
| Get Onboarding Chat History | Redis |
| After Sales Agent | AI Agent |
| Memory1 | memoryRedisChat |
| Model1 | OpenAI Chat Model |
| Handoff Tool | 工作流工具 |
| Handoff Subworkflow1 | 执行工作流 |
| Send Response2 | Telegram |
| Memory2 | memoryRedisChat |
| Update Agent Memory | memoryManager |
| Send Response3 | Telegram |
| Get Canned Response | Telegram |
| Notify user | Telegram |
| Memory3 | memoryRedisChat |
| Update Agent Memory1 | memoryManager |
| Continue Conversation | Telegram |

## 触发方式
- Handoff Subworkflow 触发
- Telegram Trigger 触发

## 统计
- 节点总数：30
- 触发节点：2
- 处理节点：21
- 输出节点：7
- 分类：workflow-automation
