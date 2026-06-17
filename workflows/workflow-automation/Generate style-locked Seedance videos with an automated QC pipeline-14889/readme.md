## 简介
**Generate style-locked Seedance videos with an automated QC pipeline**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Slack/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/14889

---

# Generate style-locked Seedance videos with an automated QC pipeline


## 节点清单

| 节点 | 类型 |
|------|------|
| Poll: Check Variant Generation Status1 | HTTP Request |
| Wait 20s Before Retry1 | 等待 |
| Slack: Post Style QC Report1 | Slack |
| Gmail: Send QC Report to Editorial1 | Email 发送 |
| Telegram: Notify on QC Rejection1 | Telegram |
| Jira: Create Style Review Task1 | jira |
| Webhook: Style Transfer Request2 | Webhook |
| Validate & Extract Show Style Profile2 | Code |
| Build Style-Locked Variants2 | Code |
| Build Style-Anchored Request2 | Code |
| Seedance: Generate Style-Locked Variant2 | HTTP Request |
| Merge Variant Job + Style Data2 | Code |
| Variant Ready?2 | IF 判断 |
| Run Style QC Check2 | Code |
| QC Gate: Style Approved?2 | IF 判断 |
| Aggregate QC Results2 | Code |
| On Workflow Error | 错误触发器 |
| Slack: Error Alert | Slack |



## 功能说明

AI 视频生成工作流，自动创作视频内容，Webhook 触发。

Webhook触发，通过 Telegram 通知 实现自动化。

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

- 节点总数：18
- 触发方式：Webhook 触发

## 触发方式
- Webhook: Style Transfer Request2 触发
- On Workflow Error 触发

## 统计
- 节点总数：18
- 触发节点：2
- 处理节点：10
- 输出节点：6
- 分类：workflow-automation
