## 简介
**Build Your First Automated Email Support Agent (AI Fallback & Logging)**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Slack/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/6287

---

# Build Your First Automated Email Support Agent (AI Fallback & Logging)


## 节点清单

| 节点 | 类型 |
|------|------|
| AI Agent | AI Agent |
| Gmail Trigger | Gmail 触发器 |
| Simple Memory | 记忆缓冲区 |
| Append or update row in sheet in Google Sheets | Google Sheets 工具 |
| OpenAI Model | OpenAI Chat Model |
| Gemini Chat Model | OpenAI Chat Model |
| Reply to a message(Thread) | Email 发送 |



## 功能说明

邮件自动化处理，AI 分类整理或。

定时触发、手动触发，通过 邮箱 + 在线表格 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com
- 邮箱 SMTP/IMAP 账号密码

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：7
- 触发方式：手动或子流程调用

## 触发方式
- Gmail Trigger 触发

## 统计
- 节点总数：7
- 触发节点：1
- 处理节点：5
- 输出节点：1
- 分类：workflow-automation
