## 简介
**AI-Powered Invoice Reminder & Payment Tracker for Finance & Accounting**

（待补充中文描述）

> 分类：金融分析 | 适配等级：A（需替换Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/10111

---

# AI-Powered Invoice Reminder & Payment Tracker for Finance & Accounting


## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Daily Check | 定时触发器 |
| Fetch Pending Invoices | PostgreSQL |
| Filter Overdue Invoices | IF 判断 |
| Calculate Reminder Logic | Code |
| Prepare AI Prompt | 数据设置 |
| Format Email | Code |
| Send Email Reminder | Email 发送 |
| Update Reminder Status | PostgreSQL |
| Create Activity Log | 数据设置 |
| Save to Activity Log | PostgreSQL |
| Generate Daily Summary | Code |
| Send Summary to Finance Team | Email 发送 |
| Webhook: Payment Received | Webhook |
| Update Payment Status | PostgreSQL |
| Webhook Response | 响应 Webhook |
| Send Payment Confirmation | Email 发送 |
| Generate Email | OpenAI Chat Model |
| AI Agent For Generate Email Content | AI Agent |



## 功能说明

AI 语音处理工作流，语音合成或转录，定时执行。

定时触发、Webhook触发，通过 邮箱 + 数据库 + HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com
- 邮箱 SMTP/IMAP 账号密码
- 数据库连接信息
- 通义万相 API Key → https://dashscope.aliyun.com

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：18
- 触发方式：定时触发, Webhook 触发

## 触发方式
- Schedule Daily Check 触发
- Webhook: Payment Received 触发

## 统计
- 节点总数：18
- 触发节点：2
- 处理节点：12
- 输出节点：4
- 分类：finance-analysis
