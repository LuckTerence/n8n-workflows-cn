## 简介
**Generate multi-pass Seedance AI roto mattes with QC and Nuke handoff**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：B（需替换Google Sheets/Slack/Gmail)（基本改完，配置 API Key 应该就能跑）
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

## 触发方式
- On Workflow Error 触发
- Google Sheets Trigger 触发

## 统计
- 节点总数：20
- 触发节点：2
- 处理节点：11
- 输出节点：7
- 分类：workflow-automation
