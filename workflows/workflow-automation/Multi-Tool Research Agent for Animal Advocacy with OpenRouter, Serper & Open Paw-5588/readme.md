## 简介
**Multi-Tool Research Agent for Animal Advocacy with OpenRouter, Serper & Open Paws DB**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：21 | 难度：⭐⭐⭐ 高级
> 原始来源：https://n8nworkflows.xyz/workflows/5588

---

# Multi-Tool Research Agent for Animal Advocacy with OpenRouter, Serper & Open Paws DB


## 节点清单

| 节点 | 类型 |
|------|------|
| Serper API | HTTP 工具 |
| OpenRouter Chat Model | OpenRouter Chat Model |
| AI Agent | AI Agent |
| Database Retrieval | HTTP 工具 |
| When Executed by Another Workflow | 执行工作流触发器 |
| When chat message received | Chat 触发器 |
| Think | 思考工具 |
| Email Finder | hunterTool |
| Email Verifier | hunterTool |
| Set Fields | 数据设置 |
| Web Scraper Tool | HTTP 工具 |
| Twitter Post Scraper | HTTP 工具 |
| Twitter Profile Scraper | HTTP 工具 |
| Instagram Profile Scraper | HTTP 工具 |
| Linkedin Person and Company Scraper | HTTP 工具 |
| If | IF 判断 |
| Simple Memory | 记忆缓冲区 |
| Fix Empty Response | LLM Chain |
| OpenRouter Chat Model1 | OpenRouter Chat Model |
| Set Output (If Empty) | 数据设置 |
| Set Output (If Not Empty) | 数据设置 |
| Score Text | 工作流工具 |

## 触发方式
- When Executed by Another Workflow 触发
- When chat message received 触发

## 统计
- 节点总数：22
- 触发节点：2
- 处理节点：13
- 输出节点：7
- 分类：workflow-automation
