## 简介
**Generate Invoices, Save to Drive and Send Email to Customer with JS + G Sheets**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Google Drive)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4105

---

# Generate Invoices, Save to Drive and Send Email to Customer with JS + G Sheets


## 节点清单

| 节点 | 类型 |
|------|------|
| Webhook Simulator | Webhook |
| Generate Invoice ID | Code |
| Check if ID Already Exists | Google Sheets |
| If Does not Exist | IF 判断 |
| Set Fields | 数据设置 |
| Create Invoice HTML | Code |
| HTML to PDF | HTTP Request |
| Upload PDF to GDrive | Google Drive |
| Email Invoice to Customer | Email 发送 |
| Append Details to Invoices Sheet | Google Sheets |
| Download PDF from API | HTTP Request |



## 功能说明

邮件自动化处理，AI 分类整理或。

定时触发、Webhook触发，通过 邮箱 + HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- 邮箱 SMTP/IMAP 账号密码
- 通义万相 API Key → https://dashscope.aliyun.com

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：11
- 触发方式：Webhook 触发

## 触发方式
- Webhook Simulator 触发

## 统计
- 节点总数：11
- 触发节点：1
- 处理节点：7
- 输出节点：3
- 分类：workflow-automation
