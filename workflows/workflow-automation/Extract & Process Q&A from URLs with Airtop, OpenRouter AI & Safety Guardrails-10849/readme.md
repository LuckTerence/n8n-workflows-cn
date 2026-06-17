## 简介
**Extract & Process Q&A from URLs with Airtop, OpenRouter AI & Safety Guardrails**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：8 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/10849

---

# Extract & Process Q&A from URLs with Airtop, OpenRouter AI & Safety Guardrails


## 节点清单

| 节点 | 类型 |
|------|------|
| Filter Only URLs | 过滤器 |
| Extract Q&A from URL | Airtop |
| Apply Safety Guardrails | guardrails |
| OpenRouter Model | OpenRouter Chat Model |
| Send Safe Response | Telegram |
| Send Violation Alert | Telegram |
| Tavily Web Search | tavilyTool |
| Telegram Trigger1 | Telegram 触发器 |
| Main agent | AI Agent |

## 触发方式
- Telegram Trigger1 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：6
- 输出节点：2
- 分类：workflow-automation
