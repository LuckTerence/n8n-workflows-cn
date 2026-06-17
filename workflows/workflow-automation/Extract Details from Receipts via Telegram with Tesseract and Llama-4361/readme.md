## 简介
**Extract Details from Receipts via Telegram with Tesseract and Llama**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4361

---

# Extract Details from Receipts via Telegram with Tesseract and Llama


## 节点清单

| 节点 | 类型 |
|------|------|
| Format Summary Message | Code |
| Get Telegram File | HTTP Request |
| Download Image | HTTP Request |
| Telegram Trigger | Telegram 触发器 |
| AI Categorizer | LLM Chain |
| Check Invalid Input | IF 判断 |
| Extract Text Input | 数据设置 |
| Check for Image | IF 判断 |
| Receipt Parser | 结构化输出解析器 |
| AI Analyzer | OpenRouter Chat Model |
| Send Error Message | Telegram |
| Send Expense Summary | Telegram |
| Extract Value From Image | tesseractNode |



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

- 节点总数：13
- 触发方式：Telegram 消息触发

## 触发方式
- Telegram Trigger 触发

## 统计
- 节点总数：13
- 触发节点：1
- 处理节点：8
- 输出节点：4
- 分类：workflow-automation
