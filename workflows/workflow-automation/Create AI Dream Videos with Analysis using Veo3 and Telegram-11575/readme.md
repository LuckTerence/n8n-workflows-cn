## 简介
**Create AI Dream Videos with Analysis using Veo3 and Telegram**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/11575

---

# Create AI Dream Videos with Analysis using Veo3 and Telegram


## 节点清单

| 节点 | 类型 |
|------|------|
| Telegram Trigger | Telegram 触发器 |
| Parse Dream Command | Code |
| Route: Style Help Request | IF 判断 |
| Send Available Styles | Telegram |
| Route: Valid Dream Input | IF 判断 |
| Send Usage Instructions | Telegram |
| Send Processing Status | Telegram |
| Set API Configuration | 数据设置 |
| AI Dream Analyzer Agent | AI Agent |
| OpenRouter LLM | OpenRouter Chat Model |
| Extract Video Prompt & Analysis | Code |
| Generate Dream Video (Veo3) | HTTP Request |
| Wait for Video Generation | 等待 |
| Poll Generation Status | HTTP Request |
| Route: Generation Complete | IF 判断 |
| Log to Google Sheets | Google Sheets |
| Send Dream Video to User | Telegram |

## 触发方式
- Telegram Trigger 触发

## 统计
- 节点总数：17
- 触发节点：1
- 处理节点：10
- 输出节点：6
- 分类：workflow-automation
