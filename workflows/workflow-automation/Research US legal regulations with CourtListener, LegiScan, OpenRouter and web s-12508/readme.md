## 简介
**Research US legal regulations with CourtListener, LegiScan, OpenRouter and web search**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/12508

---

# Research US legal regulations with CourtListener, LegiScan, OpenRouter and web search


## 节点清单

| 节点 | 类型 |
|------|------|
| Court Listener Discovery | HTTP Request 工具 |
| Google Search Discovery | HTTP 工具 |
| LegiScan Discovery | HTTP Request 工具 |
| Court Listener Retrieveal | HTTP Request 工具 |
| Think Tool Prioritization | 思考工具 |
| LegiScan Retrieval | HTTP Request 工具 |
| DocumentCloud Retrieval | HTTP Request 工具 |
| Jina URL Text Extraction | jinaAiTool |
| Think Tool Analysis | 思考工具 |
| Step 5: Verification | LLM Chain |
| Structured Output Parser | 结构化输出解析器 |
| If hallucinations present | IF 判断 |
| Think Tool Analysis1 | 思考工具 |
| Set Report | 数据设置 |
| Set Output | 数据设置 |
| Retry if Tools Not Used | IF 判断 |
| Retry if Tools Not Used1 | IF 判断 |
| Retry if Response Empty | IF 判断 |
| Retry if Response Empty1 | IF 判断 |
| Step 1: Discovery | AI Agent |
| Auto Fallback | OpenRouter Chat Model |
| Auto Fallback1 | OpenRouter Chat Model |
| Step 2: Prioritization | AI Agent |
| Auto Fallback2 | OpenRouter Chat Model |
| Step 3: Retrieval | AI Agent |
| Auto Fallback3 | OpenRouter Chat Model |
| Step 4: Report Writing | AI Agent |
| Auto Fallback4 | OpenRouter Chat Model |
| Auto Fallback5 | OpenRouter Chat Model |
| Step 6: Fixing Hallucinations | AI Agent |
| If Empty Output | IF 判断 |
| If Empty Output1 | IF 判断 |
| Plural Retrieval | HTTP Request 工具 |
| Plural Discovery1 | HTTP Request 工具 |
| Qwen3 | OpenRouter Chat Model |
| Qwen4 | OpenRouter Chat Model |
| Sonnet 4.5 | OpenRouter Chat Model |
| Sonnet 4. | OpenRouter Chat Model |
| Opus | OpenRouter Chat Model |
| Opus1 | OpenRouter Chat Model |
| Document Cloud Discovery | HTTP Request 工具 |
| Trigger legal research request (Webhook) | Webhook |

## 触发方式
- Trigger legal research request (Webhook) 触发

## 统计
- 节点总数：42
- 触发节点：1
- 处理节点：32
- 输出节点：9
- 分类：workflow-automation
