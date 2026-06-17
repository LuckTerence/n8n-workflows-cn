## 简介
**Send Personalized HTML Welcome Emails to New Xero Contacts via SMTP**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/7165

---

# Send Personalized HTML Welcome Emails to New Xero Contacts via SMTP


## 节点清单

| 节点 | 类型 |
|------|------|
| Send Personalized Welcome Email | Email 发送 |
| New Contact in Xero | Webhook |
| Is it a NEW Contact? | IF 判断 |
| Fetch Full Contact Details from Xero | xero |
| Build Personalized HTML Email | Code |



## 功能说明

邮件自动化处理，AI 分类整理或。

定时触发、Webhook触发，通过 邮箱 + HTTP API 实现自动化。

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

- 节点总数：5
- 触发方式：Webhook 触发

## 触发方式
- New Contact in Xero 触发

## 统计
- 节点总数：5
- 触发节点：1
- 处理节点：3
- 输出节点：1
- 分类：workflow-automation
