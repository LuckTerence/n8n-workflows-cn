## 简介
**Generate Financial Reports with AI Insights, Budget Analysis & Smart Alerts**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Slack/Google Drive/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/10677

---

# Generate Financial Reports with AI Insights, Budget Analysis & Smart Alerts


## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Monthly | 定时触发器 |
| Calculate Period | Code |
| Fetch Current P&L | HTTP Request |
| Fetch Previous P&L | HTTP Request |
| Merge Data | 数据合并 |
| Analyze Financial Data | Code |
| Prepare AI Context | 数据设置 |
| AI Financial Insights | AI Agent |
| OpenAI Chat Model | OpenAI Chat Model |
| Prepare Report Data | Code |
| Requires CFO Review? | IF 判断 |
| Request CFO Review | Email 发送 |
| Generate Report HTML | Code |
| HTML to PDF | htmlcsstopdf |
| Save to Google Drive | Google Drive |
| Send to Stakeholders | Email 发送 |
| Health Critical? | IF 判断 |
| Alert - Critical | HTTP Request |
| Notify - Standard | HTTP Request |



## 功能说明

监控告警系统，异常检测并发送通知，定时执行。

定时触发，通过 邮箱 + HTTP API 实现自动化。

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

- 节点总数：19
- 触发方式：定时触发

## 触发方式
- Schedule Monthly 触发

## 统计
- 节点总数：19
- 触发节点：1
- 处理节点：12
- 输出节点：6
- 分类：workflow-automation
