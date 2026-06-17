## 简介
**Convert Outlook emails to Planner tasks and monitor Secure Score with Teams alerts in M365**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/15797

---

# Convert Outlook emails to Planner tasks and monitor Secure Score with Teams alerts in M365


## 节点清单

| 节点 | 类型 |
|------|------|
| Every 30 Minutes | 定时触发器 |
| Get Unread Emails | Outlook |
| Any Emails? | IF 判断 |
| No New Emails | 空操作 |
| One Email at a Time | 分批处理 |
| Extract Task from Email | Code |
| Keyword Match Found? | IF 判断 |
| Create Planner Task | HTTP Request |
| Set Task Details (Notes) | HTTP Request |
| Post Teams Notification | Teams |
| Reply, Categorize & Mark Read | Outlook |
| Mark as Read After Reply | Outlook |
| Done (Email Processed) | 空操作 |
| Error Capture (Poison Pill Guard) | Code |
| Had Error? | IF 判断 |
| Mark as Read (No Action) | Outlook |
| API Rate Limit Throttle | 等待 |
| Workflow Error Trigger | 错误触发器 |
| Send Error Notification Email | HTTP Request |
| Every Monday at 8AM | 定时触发器 |
| Get Latest Secure Score | HTTP Request |
| Calculate Security Score Percentage | Code |
| Is Score Below 80%? | IF 判断 |
| Create Security Planner Task | HTTP Request |
| Set Security Task Details | HTTP Request |
| Post Security Teams Alert | Teams |
| Post Security Teams Summary | Teams |
| Get Existing Planner Tasks | HTTP Request |
| Alert Task Already Open? | IF 判断 |
| Resolve Existing Task ID | Code |
| Update Existing Alert Task | HTTP Request |



## 功能说明

邮件自动化处理，AI 分类整理或。

定时触发，通过 邮箱 + HTTP API 实现自动化。

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

- 节点总数：31
- 触发方式：定时触发

## 触发方式
- Every 30 Minutes 触发
- Workflow Error Trigger 触发
- Every Monday at 8AM 触发

## 统计
- 节点总数：31
- 触发节点：3
- 处理节点：13
- 输出节点：15
- 分类：workflow-automation
