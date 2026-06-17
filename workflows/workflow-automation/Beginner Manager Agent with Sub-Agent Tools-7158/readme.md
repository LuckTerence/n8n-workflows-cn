## 简介
**Beginner Manager Agent with Sub-Agent Tools**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/7158

---

# Beginner Manager Agent with Sub-Agent Tools


## 节点清单

| 节点 | 类型 |
|------|------|
| OpenAI Chat Model | OpenAI Chat Model |
| Simple Memory | 记忆缓冲区 |
| Simple Memory1 | 记忆缓冲区 |
| OpenAI Chat Model1 | OpenAI Chat Model |
| OpenAI Chat Model2 | OpenAI Chat Model |
| DataAgent (Insight Generator) | agentTool |
| Simple Memory2 | 记忆缓冲区 |
| ManagerAgent (Routing + Instruction Generator) | AI Agent |
| EmailAgent (Communication Specialist) | agentTool |

## 触发方式
- 手动触发

## 统计
- 节点总数：9
- 触发节点：0
- 处理节点：9
- 输出节点：0
- 分类：workflow-automation
