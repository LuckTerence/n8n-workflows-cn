## 简介
**Smart Email Classifier & Auto-Responder with AI**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3242

---

# Smart Email Classifier & Auto-Responder with AI


## 节点清单

| 节点 | 类型 |
|------|------|
| Sentiment Analysis | sentimentAnalysis |
| Azure OpenAI Chat Model | Azure OpenAI Chat Model |
| Spam | Email 发送 |
| Gmail | Email 发送 |
| Important | Email 发送 |
| Promotion | Email 发送 |
| Notification | Email 发送 |
| Personal | Email 发送 |
| Call request | Email 发送 |
| Needs Reply | Email 发送 |
| important? | sentimentAnalysis |
| Draft Reply | AI Agent |
| $INPUTS$ | 数据设置 |
| Draft | Gmail 工具 |
| Get emails | Gmail 工具 |
| needs reply? | sentimentAnalysis |
| No Operation, do nothing | 空操作 |
| Telegram | Telegram |
| Google Calendar | Google Calendar 工具 |
| Gmail Trigger | Gmail 触发器 |
| json schema | 结构化输出解析器 |
| Write draft | Email 发送 |



## 功能说明

邮件自动化处理，AI 分类整理或。

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

- 节点总数：22
- 触发方式：手动或子流程调用

## 触发方式
- Gmail Trigger 触发

## 统计
- 节点总数：22
- 触发节点：1
- 处理节点：11
- 输出节点：10
- 分类：workflow-automation
