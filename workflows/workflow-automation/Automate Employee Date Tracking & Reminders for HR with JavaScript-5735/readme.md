## 简介
**Automate Employee Date Tracking & Reminders for HR with JavaScript**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Slack/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5735

---

# Automate Employee Date Tracking & Reminders for HR with JavaScript


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking 'Test workflow' | 手动触发 |
| Sample Data Generator | Code |
| Date Analysis & Categorization | Code |
| Reminder Scheduler | Code |
| Advanced Date Filters | Code |
| Date Formatting & Export | Code |
| Gmail | Email 发送 |
| Slack | Slack |
| Google Calendar | Google Calendar |
| Edit Fields | 数据设置 |
| HR DATA | Google Sheets |



## 功能说明

AI 招聘助手，简历筛选或面试流程自动化。

手动触发，通过 邮箱 + Slack + HTTP API 实现自动化。

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

- 节点总数：11
- 触发方式：手动触发

## 触发方式
- When clicking 'Test workflow' 触发

## 统计
- 节点总数：11
- 触发节点：1
- 处理节点：8
- 输出节点：2
- 分类：workflow-automation
