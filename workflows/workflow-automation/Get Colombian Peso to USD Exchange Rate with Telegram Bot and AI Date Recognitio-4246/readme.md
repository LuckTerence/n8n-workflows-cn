## 简介
**Get Colombian Peso to USD Exchange Rate with Telegram Bot and AI Date Recognition**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：28 | 难度：⭐⭐⭐ 高级
> 原始来源：https://n8nworkflows.xyz/workflows/4246

---

# Get Colombian Peso to USD Exchange Rate with Telegram Bot and AI Date Recognition


## 节点清单

| 节点 | 类型 |
|------|------|
| OpenAI Chat Model | OpenAI Chat Model |
| Once a Telegram Message is received | Telegram 触发器 |
| Local Current Date and Time | Code |
| Validate if Date is in the past | IF 判断 |
| Notify past date | Telegram |
| Get TRM | HTTP Request |
| Check if Valor exists | IF 判断 |
| Send message to user | Telegram |
| Generate an array with 10 numbers | Code |
| Split Items for the loop | 数据拆分 |
| Get the last 10 responses | 分批处理 |
| Get TRM for past date | HTTP Request |
| Convert date | Code |
| Get non-empty rows | 过滤器 |
| Sort most recent data | 数据排序 |
| Get the last data | 数据限制 |
| Send current TRM | Telegram |
| If | IF 判断 |
| Send no data | Telegram |
| Calculator | 计算器工具 |
| Think | 思考工具 |
| Extractor Agent | AI Agent |
| Text only | 数据设置 |
| Audio Text | 数据设置 |
| Edit Fields | 数据设置 |
| Structured Output Parser | 结构化输出解析器 |
| Validate Text or Audio | Switch 路由 |
| Download Audio | Telegram |
| Transcribe Audio | OpenAI |

## 触发方式
- Once a Telegram Message is received 触发

## 统计
- 节点总数：29
- 触发节点：1
- 处理节点：21
- 输出节点：7
- 分类：workflow-automation
