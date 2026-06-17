## 简介
**Get Colombian Peso to USD Exchange Rate with Telegram Bot and AI Date Recognition**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
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



## 功能说明

Telegram 机器人，消息驱动自动化流程。

Telegram 消息触发，通过 Telegram 通知 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com
- Telegram Bot Token → @BotFather 创建
- 通义万相 API Key → https://dashscope.aliyun.com

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：29
- 触发方式：Telegram 消息触发

## 触发方式
- Once a Telegram Message is received 触发

## 统计
- 节点总数：29
- 触发节点：1
- 处理节点：21
- 输出节点：7
- 分类：workflow-automation
