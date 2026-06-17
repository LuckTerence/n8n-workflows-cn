## 简介
**Enterprise Contract Lifecycle Management with AI Risk Analysis**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Slack/Google Drive)（基本改完，配置 API Key 应该就能跑）
> 节点数：16 | 难度：⭐⭐⭐ 高级
> 原始来源：https://n8nworkflows.xyz/workflows/8497

---

# Enterprise Contract Lifecycle Management with AI Risk Analysis


## 节点清单

| 节点 | 类型 |
|------|------|
| Monitor Contract Emails | Email 读取 |
| Monitor Google Drive | Google Drive 触发器 |
| Hourly CRM Check | 定时触发器 |
| Check Salesforce | salesforce |
| Merge Contract Sources | 数据合并 |
| Check Duplicate | PostgreSQL |
| New Contract? | IF 判断 |
| PDF Vector - Extract All Data | pdfVector |
| PDF Vector - Risk Analysis | pdfVector |
| Get Contract Template | PostgreSQL |
| Analyze & Score Contract | Code |
| Save to Contract Repository | PostgreSQL |
| Needs Legal Review? | IF 判断 |
| Notify Legal Team | Slack |
| Update Salesforce | salesforce |
| Daily Alert Check | 定时触发器 |
| Get Upcoming Alerts | PostgreSQL |
| Send Daily Summary | Slack |

## 触发方式
- Monitor Google Drive 触发
- Hourly CRM Check 触发
- Daily Alert Check 触发

## 统计
- 节点总数：18
- 触发节点：3
- 处理节点：12
- 输出节点：3
- 分类：workflow-automation
