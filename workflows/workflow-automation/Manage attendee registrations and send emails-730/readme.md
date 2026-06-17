## 简介
**Manage attendee registrations and send emails**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/730

---

# Manage attendee registrations and send emails


## 节点清单

| 节点 | 类型 |
|------|------|
| Attendee Registrations | typeformTrigger |
| Add to Sheets | Google Sheets |
| Create Account | Mattermost |
| Add to team | Mattermost |
| Array to Rows | Function |
| Get Session Details | Google Sheets |
| Merge Data | 数据合并 |
| Add to channels | Mattermost |
| Add to Event | Google Calendar |
| Welcome Email | Email 发送 |



## 功能说明

邮件自动化处理，AI 分类整理或。

定时触发，通过 邮箱 + 在线表格 + HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- 邮箱 SMTP/IMAP 账号密码

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：10
- 触发方式：表单提交触发

## 触发方式
- Attendee Registrations 触发

## 统计
- 节点总数：10
- 触发节点：1
- 处理节点：5
- 输出节点：4
- 分类：workflow-automation
