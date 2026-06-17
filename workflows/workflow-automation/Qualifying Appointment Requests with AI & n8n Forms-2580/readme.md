## 简介
**Qualifying Appointment Requests with AI & n8n Forms**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2580

---

# Qualifying Appointment Requests with AI & n8n Forms


## 节点清单

| 节点 | 类型 |
|------|------|
| n8n Form Trigger | 表单触发器 |
| Form End | 表单 |
| Enter Date & Time | 表单 |
| Get Form Values | 数据设置 |
| Terms & Conditions | 表单 |
| OpenAI Chat Model | OpenAI Chat Model |
| Has Accepted? | IF 判断 |
| Send Receipt | Email 发送 |
| Wait for Approval | Email 发送 |
| Has Approval? | IF 判断 |
| OpenAI Chat Model1 | OpenAI Chat Model |
| Create Appointment | Google Calendar |
| Send Rejection | Email 发送 |
| Decline | 表单 |
| Decline1 | 表单 |
| Trigger Approval Process | 执行工作流 |
| Execute Workflow Trigger | 执行工作流触发器 |
| Summarise Enquiry | LLM Chain |
| Enquiry Classifier | 文本分类器 |



## 功能说明

表单问卷工具，自动收集和处理用户反馈（Qualifying)表单提交触发，通过 邮箱 实现自动化。

，通过 邮箱 实现自动化。

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
- 触发方式：表单提交触发

## 触发方式
- n8n Form Trigger 触发
- Execute Workflow Trigger 触发

## 统计
- 节点总数：19
- 触发节点：2
- 处理节点：14
- 输出节点：3
- 分类：workflow-automation
