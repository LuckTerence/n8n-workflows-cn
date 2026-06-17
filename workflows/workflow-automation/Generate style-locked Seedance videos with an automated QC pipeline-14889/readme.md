## 简介
**Generate style-locked Seedance videos with an automated QC pipeline**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A-adapted（基本改完，配置 API Key 应该就能跑）
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

## 触发方式
- Webhook: Style Transfer Request2 触发
- On Workflow Error 触发

## 统计
- 节点总数：18
- 触发节点：2
- 处理节点：10
- 输出节点：6
- 分类：workflow-automation
