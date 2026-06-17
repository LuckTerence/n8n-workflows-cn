## 简介
**Generate Newsletter Images with Nano Banana & Post Human-Approved Tweets to X**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/8655

---

# Generate Newsletter Images with Nano Banana & Post Human-Approved Tweets to X


## 节点清单

| 节点 | 类型 |
|------|------|
| Image Gen (Nano Banana) | HTTP Request |
| OpenAI Chat Model | OpenAI Chat Model |
| Wait1 | 等待 |
| Get Image | HTTP Request |
| Image created | IF 判断 |
| Google Sheets Trigger | Google Sheets 触发器 |
| post media | HTTP Request |
| Add Image URL | Google Sheets |
| OpenAI Chat Model1 | OpenAI Chat Model |
| Send Tweet text for approval | Telegram |
| Send Tweet image for approval | Telegram |
| Approved | IF 判断 |
| Tweet not approved | Google Sheets |
| Download Image | HTTP Request |
| Downlaod Image again | HTTP Request |
| Create Tweet | Twitter |
| Tweet Generator | AI Agent |
| Prompt Generator | AI Agent |
| Tweet posted | Google Sheets |



## 功能说明

AI 图像生成工作流，文生图或图生图。

手动触发，通过 Telegram 通知 实现自动化。

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

- 节点总数：19
- 触发方式：手动或子流程调用

## 触发方式
- Google Sheets Trigger 触发

## 统计
- 节点总数：19
- 触发节点：1
- 处理节点：11
- 输出节点：7
- 分类：workflow-automation
