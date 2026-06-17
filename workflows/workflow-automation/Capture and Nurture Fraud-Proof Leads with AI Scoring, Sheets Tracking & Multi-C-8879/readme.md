## 简介
**Capture and Nurture Fraud-Proof Leads with AI Scoring, Sheets Tracking & Multi-Channel Alerts**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Slack/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/8879

---

# Capture and Nurture Fraud-Proof Leads with AI Scoring, Sheets Tracking & Multi-Channel Alerts


## 节点清单

| 节点 | 类型 |
|------|------|
| Capture Leads | Webhook |
| IP Lookup | HTTP Request |
| Filter Valid Emails | IF 判断 |
| Lead Quality Score | Code |
| Append row in sheet | Google Sheets |
| Merge | 数据合并 |
| High Score Check | IF 判断 |
| No Operation, do nothing | 空操作 |
| Notify Sales Team | Slack |
| Auto-Send Welcome Email | Email 发送 |
| Reformat for Email | 数据设置 |
| Track Email Opens | 数据设置 |
| Check No Response | IF 判断 |
| Auto Follow-Up Email | Email 发送 |
| Calculate Engagement Score | Code |
| Weekly Report Trigger | 定时触发器 |
| Generate Weekly Report | Code |
| Validate Email | verifiEmail |
| Delay 24 Hours | 等待 |
| Send Report to Sales Head | Email 发送 |
| Set User Config | 数据设置 |



## 功能说明

客户关系管理工具，自动管理销售线索和客户数据，定时执行。

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

- 节点总数：21
- 触发方式：Webhook 触发, 定时触发

## 触发方式
- Capture Leads 触发
- Weekly Report Trigger 触发

## 统计
- 节点总数：21
- 触发节点：2
- 处理节点：14
- 输出节点：5
- 分类：workflow-automation
