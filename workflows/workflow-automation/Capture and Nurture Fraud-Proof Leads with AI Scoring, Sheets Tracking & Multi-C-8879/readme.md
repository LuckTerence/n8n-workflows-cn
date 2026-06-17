## 简介
**Capture and Nurture Fraud-Proof Leads with AI Scoring, Sheets Tracking & Multi-Channel Alerts**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Slack/Gmail)（基本改完，配置 API Key 应该就能跑）
> 节点数：19 | 难度：⭐⭐⭐ 高级
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

## 触发方式
- Capture Leads 触发
- Weekly Report Trigger 触发

## 统计
- 节点总数：21
- 触发节点：2
- 处理节点：14
- 输出节点：5
- 分类：workflow-automation
