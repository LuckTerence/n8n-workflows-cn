## 简介
**Research topics using OpenRouter AI agents with Serper search and Jina AI reports**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 节点数：35 | 难度：⭐⭐⭐ 高级
> 原始来源：https://n8nworkflows.xyz/workflows/12504

---

# Research topics using OpenRouter AI agents with Serper search and Jina AI reports


## 节点清单

| 节点 | 类型 |
|------|------|
| Read URL content in Jina AI | jinaAiTool |
| Think1 | 思考工具 |
| OpenRouter Chat Model | OpenRouter Chat Model |
| Think Tool Analysis | 思考工具 |
| Retry if Tools Not Used | IF 判断 |
| Retry if Response Empty1 | IF 判断 |
| Auto Fallback3 | OpenRouter Chat Model |
| Serper API 2 | HTTP Request 工具 |
| Semantic Scholar 2 | HTTP Request 工具 |
| LinkedinScraper 2 | HTTP Request 工具 |
| InstagramScraper 2 | HTTP Request 工具 |
| XPostScraper 2 | HTTP Request 工具 |
| XProfileScraper 2 | HTTP Request 工具 |
| Qwen3 | OpenRouter Chat Model |
| Opus | OpenRouter Chat Model |
| Set Prompt | 数据设置 |
| Searching For Information | AI Agent |
| Writing Report | AI Agent |
| Trigger research request (Webhook) | Webhook |
| Trigger research from another workflow | 执行工作流触发器 |
| Structured Output Parser | 结构化输出解析器 |
| If hallucinations present | IF 判断 |
| Set Report | 数据设置 |
| Set Output | 数据设置 |
| Auto Fallback4 | OpenRouter Chat Model |
| Auto Fallback5 | OpenRouter Chat Model |
| Think Tool Analysis2 | 思考工具 |
| If Empty Output | IF 判断 |
| If Empty Output1 | IF 判断 |
| Opus1 | OpenRouter Chat Model |
| Sonnet | OpenRouter Chat Model |
| Respond to Webhook | 响应 Webhook |
| If Source is Webhook | IF 判断 |
| Set Report1 | 数据设置 |
| Verifying Report | LLM Chain |
| Fixing Hallucinations | AI Agent |

## 触发方式
- Trigger research request (Webhook) 触发
- Trigger research from another workflow 触发

## 统计
- 节点总数：36
- 触发节点：2
- 处理节点：27
- 输出节点：7
- 分类：workflow-automation
