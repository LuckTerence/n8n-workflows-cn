## 简介
**Generate multi-pass Seedance AI roto mattes with QC and Nuke handoff**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Slack/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/14390

---

# Generate multi-pass Seedance AI roto mattes with QC and Nuke handoff


## 节点清单

| 节点 | 类型 |
|------|------|
| Validate & Extract Roto Brief | Code |
| Fan-Out: 4 Roto Passes | Code |
| Build Roto Request Body | Code |
| Seedance: Generate Roto Pass | HTTP Request |
| Merge Roto Job ID + Metadata | Code |
| Poll: Check Roto Job Status | HTTP Request |
| Wait 20s | 等待 |
| Roto Render Complete? | IF 判断 |
| Build Roto Metadata + QC Score | Code |
| QC Gate: Passes Threshold? | IF 判断 |
| Generate Nuke Roto Template | Code |
| Download Roto Pass Video | HTTP Request |
| Aggregate All Roto Passes | Code |
| Slack: QC Failed — Manual Roto Required | Slack |
| On Workflow Error | 错误触发器 |
| Slack: Error Alert | Slack |
| Google Sheets Trigger | Google Sheets 触发器 |
| Jira: Create Review Task | jira |
| Send a message | Email 发送 |
| Send Telegram1 | Telegram |



## 功能说明

Generate multi-pass Seedance AI roto mattes with Q。

手动触发，通过 Telegram 通知 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- Telegram Bot Token → @BotFather 创建
- 邮箱 SMTP/IMAP 账号密码
- 通义万相 API Key → https://dashscope.aliyun.com

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：20
- 触发方式：手动或子流程调用

## 触发方式
- On Workflow Error 触发
- Google Sheets Trigger 触发

## 统计
- 节点总数：20
- 触发节点：2
- 处理节点：11
- 输出节点：7
- 分类：workflow-automation
