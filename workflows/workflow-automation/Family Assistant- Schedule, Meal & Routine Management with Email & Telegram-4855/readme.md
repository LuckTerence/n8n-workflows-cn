## 简介
**Family Assistant: Schedule, Meal & Routine Management with Email & Telegram**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4855

---

# Family Assistant: Schedule, Meal & Routine Management with Email & Telegram


## 节点清单

| 节点 | 类型 |
|------|------|
| Start | start |
| Daily Morning Trigger (Weekdays) | 定时触发器 |
| If Events Today? | IF 判断 |
| Email Schedule Reminder | Email 发送 |
| Email Morning Checklist | Email 发送 |
| Email Meal Idea | Email 发送 |
| Daily Evening Trigger | 定时触发器 |
| Email Bedtime Reminder | Email 发送 |
| Weekly Planning Trigger (Sunday PM) | 定时触发器 |
| Email Weekly Plan Prompt | Email 发送 |
| Screen Time Break Trigger (Optional) | 定时触发器 |
| Email Screen Break Reminder | Email 发送 |
| Email Positive Thought/Fact | Email 发送 |
| Telegram Trigger | Telegram 触发器 |
| Trigger: School/Daycare Comms Check | 定时触发器 |
| Email: School Comms Reminder | Email 发送 |
| Trigger: Weekly Wins/Gratitude | 定时触发器 |
| Email: Wins/Gratitude Reminder | Email 发送 |
| Trigger: Daily Evening Check-in | 定时触发器 |
| Email: Evening Check-in | Email 发送 |
| Format Check-in Message | Code |
| Get Positive Thought/Fact1 | Code |
| Screen Time Break Trigger (Optional)1 | 定时触发器 |
| Daily Meal Idea | 定时触发器 |
| Daily Meal Idea1 | 定时触发器 |
| Code | Code |
| Check Today's Schedule | Code |
| Generate Meal Idea | Code |
| Define Daily Schedules | 数据设置 |
| Define Check-in Items | 数据设置 |
| Edit Fields | 数据设置 |
| Telegram | Telegram |
| Gmail | Email 发送 |



## 功能说明

邮件自动化处理，AI 分类整理或。

定时触发、Telegram 消息触发，通过 Telegram 通知 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- Telegram Bot Token → @BotFather 创建
- 邮箱 SMTP/IMAP 账号密码

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：33
- 触发方式：Telegram 消息触发

## 触发方式
- Daily Morning Trigger (Weekdays) 触发
- Daily Evening Trigger 触发
- Weekly Planning Trigger (Sunday PM) 触发
- Screen Time Break Trigger (Optional) 触发
- Telegram Trigger 触发
- Trigger: School/Daycare Comms Check 触发
- Trigger: Weekly Wins/Gratitude 触发
- Trigger: Daily Evening Check-in 触发
- Screen Time Break Trigger (Optional)1 触发
- Daily Meal Idea 触发
- Daily Meal Idea1 触发

## 统计
- 节点总数：33
- 触发节点：11
- 处理节点：10
- 输出节点：12
- 分类：workflow-automation
