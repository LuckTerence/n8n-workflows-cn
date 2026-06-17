## 简介
**Generate B2B Lead Opportunities from Websites with Brightdata & OpenRouter AI**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/8076

---

# Generate B2B Lead Opportunities from Websites with Brightdata & OpenRouter AI


## 节点清单

| 节点 | 类型 |
|------|------|
| parameters | 数据设置 |
| extract url | Code |
| scrap urls | brightData |
| OpenRouter Chat Model1 | OpenRouter Chat Model |
| Structured Output Parser1 | 结构化输出解析器 |
| scrap urls1 | brightData |
| HTML cleaner | HTML |
| OpenRouter Chat Model2 | OpenRouter Chat Model |
| Structured Output Parser2 | 结构化输出解析器 |
| OpenRouter Chat Model3 | OpenRouter Chat Model |
| merge pages | Code |
| clean list | Code |
| When chat message received | Chat 触发器 |
| Find best pages | AI Agent |
| Identify business opportunities | AI Agent |
| de-dupe | AI Agent |



## 功能说明

客户关系管理工具，自动管理销售线索和客户数据。

Chat 消息触发，通过 工作流编排 实现自动化。

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

- 节点总数：16
- 触发方式：Chat 消息触发

## 触发方式
- When chat message received 触发

## 统计
- 节点总数：16
- 触发节点：1
- 处理节点：15
- 输出节点：0
- 分类：workflow-automation
