## 简介
**Enterprise Contract Lifecycle Management with AI Risk Analysis**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Slack/Google Drive)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/8497

---

# Enterprise Contract Lifecycle Management with AI Risk Analysis


## 节点清单

| 节点 | 类型 |
|------|------|
| Monitor Contract Emails | Email 读取 |
| Monitor Google Drive | Google Drive 触发器 |
| Hourly CRM Check | 定时触发器 |
| Check Salesforce | salesforce |
| Merge Contract Sources | 数据合并 |
| Check Duplicate | PostgreSQL |
| New Contract? | IF 判断 |
| PDF Vector - Extract All Data | pdfVector |
| PDF Vector - Risk Analysis | pdfVector |
| Get Contract Template | PostgreSQL |
| Analyze & Score Contract | Code |
| Save to Contract Repository | PostgreSQL |
| Needs Legal Review? | IF 判断 |
| Notify Legal Team | Slack |
| Update Salesforce | salesforce |
| Daily Alert Check | 定时触发器 |
| Get Upcoming Alerts | PostgreSQL |
| Send Daily Summary | Slack |



## 功能说明

Enterprise Contract Lifecycle Management with AI R。

定时触发，通过 邮箱 + 数据库 + HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- 邮箱 SMTP/IMAP 账号密码
- 数据库连接信息

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：18
- 触发方式：定时触发

## 触发方式
- Monitor Google Drive 触发
- Hourly CRM Check 触发
- Daily Alert Check 触发

## 统计
- 节点总数：18
- 触发节点：3
- 处理节点：12
- 输出节点：3
- 分类：workflow-automation
