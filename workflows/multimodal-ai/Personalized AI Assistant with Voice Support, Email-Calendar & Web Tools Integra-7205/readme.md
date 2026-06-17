## 简介
**Personalized AI Assistant with Voice Support, Email-Calendar & Web Tools Integration**

（待补充中文描述）

> 分类：多模态 AI | 适配等级：A（需替换Google Drive/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/7205

---

# Personalized AI Assistant with Voice Support, Email-Calendar & Web Tools Integration


## 节点清单

| 节点 | 类型 |
|------|------|
| Switch | Switch 路由 |
| Get a file | Telegram |
| Transcribe a recording | OpenAI |
| Edit Fields | 数据设置 |
| OpenAI Chat Model | OpenAI Chat Model |
| SerpAPI | SerpApi 工具 |
| Contacts | Airtable 工具 |
| Calculator | 计算器工具 |
| Basic LLM Chain | LLM Chain |
| Anthropic Chat Model | OpenAI Chat Model |
| Get Calendar | Google Calendar 工具 |
| Hacker News | hackerNewsTool |
| When chat message received | Chat 触发器 |
| Simple Memory | 记忆缓冲区 |
| Get many messages in Gmail | Gmail 工具 |
| Search files and folders in Google Drive | googleDriveTool |
| Wikipedia | Wikipedia 工具 |
| AI Agent - Nova | AI Agent |



## 功能说明

邮件自动化处理，AI 分类整理或。

定时触发、Chat 消息触发，通过 Telegram 通知 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com
- Telegram Bot Token → @BotFather 创建
- 邮箱 SMTP/IMAP 账号密码

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：18
- 触发方式：Chat 消息触发

## 触发方式
- When chat message received 触发

## 统计
- 节点总数：18
- 触发节点：1
- 处理节点：16
- 输出节点：1
- 分类：multimodal-ai
