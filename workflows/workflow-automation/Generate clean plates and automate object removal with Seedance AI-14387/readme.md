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

## 触发方式
- Webhook: Clean Plate Request 触发
- On Workflow Error 触发

## 统计
- 节点总数：21
- 触发节点：2
- 处理节点：12
- 输出节点：7
- 分类：workflow-automation
