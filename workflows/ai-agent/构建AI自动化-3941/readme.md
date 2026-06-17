## 简介
**构建AI自动化**

AI自动化和Agent的构建与销售

> 分类：AI Agent | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3941

---

# 构建AI自动化


## 节点清单

| 节点 | 类型 |
|------|------|
| Ideator 🧠 | OpenAI |
| Chunk Script | HTTP Request |
| Image Prompter 📷 | OpenAI |
| Split Out | 数据拆分 |
| Get Final Video | HTTP Request |
| Set JSON Variable | 数据设置 |
| Upload to Cloudinary | HTTP Request |
| OpenAI Chat Model | OpenAI Chat Model |
| Input Variables | 数据设置 |
| Merge Video Variables | 数据合并 |
| Telegram Trigger | Telegram 触发器 |
| Set API Keys | 数据设置 |
| If No Video Idea | IF 判断 |
| If Message From User | IF 判断 |
| Telegram: Approve Idea | Telegram |
| Telegram: Conversational Response | Telegram |
| Structure Model Output | 结构化输出解析器 |
| Track Conversation Memory | 记忆缓冲区 |
| Idea Denied | 数据设置 |
| Telegram: Processing Started | Telegram |
| If All API Keys Set | IF 判断 |
| Telegram: API Keys Missing | Telegram |
| Discuss Ideas 💡 | AI Agent |
| Missing API Keys | 停止并报错 |
| Script | 数据设置 |
| Convert Script to Audio | HTTP Request |
| Generating Images | 等待 |
| Generating Videos | 等待 |
| Request Images | HTTP Request |
| Get Images | HTTP Request |
| Request Videos | HTTP Request |
| Get Videos | HTTP Request |
| Aggregate Prompts | 数据聚合 |
| Aggregate Videos | 数据聚合 |
| Generate Render JSON | HTTP Request |
| Merge Videos and Audio | 数据合并 |
| Send to Creatomate | HTTP Request |
| Generating Final Video | 等待 |
| Telegram: Approve Final Video | Telegram |
| If Final Video Approved | IF 判断 |
| If Idea Approved | IF 判断 |
| Telegram: Video Declined | Telegram |
| Decode Base64 to File | 转换为文件 |
| Convert Video to Base64 | HTTP Request |
| Upload to YouTube | youTube |
| Telegram: Video Uploaded | Telegram |



## 功能说明

构建AI自动化。

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

- 节点总数：46
- 触发方式：Telegram 消息触发

## 触发方式
- Telegram Trigger 触发

## 统计
- 节点总数：46
- 触发节点：1
- 处理节点：27
- 输出节点：18
- 分类：ai-agent
