## 简介
**Generate clean plates and automate object removal with Seedance AI**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Notion/Slack/Google Drive)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/14387

---

# Generate clean plates and automate object removal with Seedance AI


## 节点清单

| 节点 | 类型 |
|------|------|
| Webhook: Clean Plate Request | Webhook |
| Validate & Extract Input | Code |
| Fan-Out: 4 Clean Plate Passes | Code |
| Build Clean Plate Request | Code |
| Seedance: Generate Clean Pass | HTTP Request |
| Merge Job ID + Metadata | Code |
| Poll: Check Job Status | HTTP Request |
| Wait 20s | 等待 |
| Render Complete? | IF 判断 |
| Build Clean Plate Metadata + QC | Code |
| QC Check: Passes Threshold? | IF 判断 |
| Generate Nuke Comp Script | Code |
| Download Clean Plate Video | HTTP Request |
| Google Drive: Upload Clean Plate | Google Drive |
| Aggregate All Passes | Code |
| Slack: Notify Paint/Comp Team | Slack |
| Slack: QC Failed — Artist Review | Slack |
| Create a database page | Notion |
| Send Telegram1 | Telegram |
| On Workflow Error | 错误触发器 |
| Slack: Error Alert | Slack |



## 功能说明

Generate clean plates and automate object removal。

Webhook触发，通过 Telegram 通知 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- Telegram Bot Token → @BotFather 创建
- 通义万相 API Key → https://dashscope.aliyun.com

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：21
- 触发方式：Webhook 触发

## 触发方式
- Webhook: Clean Plate Request 触发
- On Workflow Error 触发

## 统计
- 节点总数：21
- 触发节点：2
- 处理节点：12
- 输出节点：7
- 分类：workflow-automation
