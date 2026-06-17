## 简介
**Create and publish AI videos from Telegram with VEED and Blotato**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/14290

---

# Create and publish AI videos from Telegram with VEED and Blotato


## 节点清单

| 节点 | 类型 |
|------|------|
| 📩 Telegram Trigger | Telegram 触发器 |
| 🤖 AI Video Agent | AI Agent |
| 🧠 OpenAI Chat Model | OpenAI Chat Model |
| 💾 Conversation Memory | 记忆缓冲区 |
| 🎬 VEED MCP Tools | MCP 客户端 |
| 📤 Send Agent Response | Telegram |
| 📋 Extract Video URL | Code |
| ✅ Has Video URL? | IF 判断 |
| 📩 Publish to Social Media? | Telegram |
| ✅ Approved? | IF 判断 |
| 📤 Send Skipped Message | Telegram |
| ⚙️ Set Caption | 数据设置 |
| 📤 Upload Video to Blotato | Blotato |
| TikTok | Blotato |
| YouTube | Blotato |
| Instagram | Blotato |
| LinkedIn | Blotato |
| Facebook | Blotato |
| Twitter (X) | Blotato |
| Threads | Blotato |
| Bluesky | Blotato |
| Pinterest | Blotato |
| Merge | 数据合并 |
| 📤 Send Publish Summary | Telegram |



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
- 📩 Telegram Trigger 触发

## 统计
- 节点总数：24
- 触发节点：1
- 处理节点：19
- 输出节点：4
- 分类：workflow-automation
