## 简介
**Automated Stock Technical Analysis with xAI Grok & Multi-channel Notifications**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/11621

---

# Automated Stock Technical Analysis with xAI Grok & Multi-channel Notifications


## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Trigger | 定时触发器 |
| Interpret Data | Code |
| Rapiwa | rapiwa |
| Send a message | Email 发送 |
| Fetch Stock Market Data | HTTP Request |
| Send warning message | Telegram |
| Send Market Summary message | Telegram |
| Memory | 记忆缓冲区 |
| Analysis Agent | AI Agent |
| Send Market Summary On Channel | Telegram |
| Get Market Condition | HTTP Request |
| Check Market is open/close | IF 判断 |
| Currency/Symble List | 数据设置 |
| RSS Read | rssFeedReadTool |
| xAI | lmChatXAiGrok |
| Append row in sheet | Google Sheets |
| Clicking | 手动触发 |



## 功能说明

金融数据分析系统，市场行情采集与 AI 分析告警，定时执行。

定时触发、手动触发，通过 Telegram 通知 实现自动化。

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

- 节点总数：17
- 触发方式：定时触发, 手动触发

## 触发方式
- Schedule Trigger 触发
- RSS Read 触发
- Clicking 触发

## 统计
- 节点总数：17
- 触发节点：3
- 处理节点：8
- 输出节点：6
- 分类：workflow-automation
