## 简介
**多级网页搜索**

多阶段AI搜索和研究套件

> 分类：AI Agent | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2539

---

# 多级网页搜索


## 节点清单

| 节点 | 类型 |
|------|------|
| Google Gemini Chat Model14 | Google Gemini |
| Google Gemini Chat Model | Google Gemini |
| Google Gemini Chat Model15 | Google Gemini |
| Auto-fixing Output Parser6 | 自动修复输出解析器 |
| Structured Output Parser3 | 结构化输出解析器 |
| Query 2 | HTTP Request |
| Query 1 | HTTP Request |
| Respond to Webhook | 响应 Webhook |
| Date & Time | 日期时间 |
| Auto-fixing Output Parser | 自动修复输出解析器 |
| Structured Output Parser1 | 结构化输出解析器 |
| Auto-fixing Output Parser7 | 自动修复输出解析器 |
| Structured Output Parser4 | 结构化输出解析器 |
| Query Maker - 1 | LLM Chain |
| Google Gemini Chat Model16 | Google Gemini |
| Article Extractor1 | HTTP Request |
| Analyst Emulator | LLM Chain |
| Webhook | Webhook |
| Query 1 Ranker & Query 2 Maker | LLM Chain |
| Date & Time1 | 日期时间 |
| Query-1 Combined | Code |
| Query-2 Combined | Code |
| Query 2 - Ranker | LLM Chain |
| Code | Code |
| Loop Over Items | 分批处理 |
| Delay-to-Avoid-Request-Per-Minute-Cap | 等待 |
| Research Reporter | LLM Chain |
| Code1 | Code |
| Webhook Call | HTTP Request |



## 功能说明

联网搜索工具，AI 驱动的信息检索和分析，Webhook 触发。

Webhook触发，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：29
- 触发方式：Webhook 触发

## 触发方式
- Webhook 触发

## 统计
- 节点总数：29
- 触发节点：1
- 处理节点：23
- 输出节点：5
- 分类：ai-agent
