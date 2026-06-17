## 简介
**Generate images on Telegram from text and voice using Grok Imagine via Kie AI**

（待补充中文描述）

> 分类：多模态 AI | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/13367

---

# Generate images on Telegram from text and voice using Grok Imagine via Kie AI


## 节点清单

| 节点 | 类型 |
|------|------|
| Grok 4.1 Fast | OpenRouter Chat Model |
| Code | Code |
| Get Message | Telegram 触发器 |
| Send a text message | Telegram |
| Get Text | 数据设置 |
| Switch2 | Switch 路由 |
| Run text to image | 工作流工具 |
| Wait1 | 等待 |
| Run image to image | 工作流工具 |
| Wait2 | 等待 |
| Switch | Switch 路由 |
| Run Kei AI | 执行工作流触发器 |
| Run text to image1 | HTTP Request |
| Run image to image1 | HTTP Request |
| Result text to image | HTTP Request |
| Result image to image | HTTP Request |
| Get voice message | Telegram |
| Transcribe recording | OpenAI |
| Get image file | Telegram |
| Upload image | FTP |
| Set Image Url | 数据设置 |
| Get input text from voice | 数据设置 |
| Grok Imagine Agent | AI Agent |
| Simple Memory1 | 记忆缓冲区 |



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

- 节点总数：24
- 触发方式：Telegram 消息触发

## 触发方式
- Get Message 触发
- Run Kei AI 触发

## 统计
- 节点总数：24
- 触发节点：2
- 处理节点：15
- 输出节点：7
- 分类：multimodal-ai
