## 简介
**Route ATS applicants to Aloware for role-based SMS AI pre-screening and follow-up**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A-adapted（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/14934

---

# Route ATS applicants to Aloware for role-based SMS AI pre-screening and follow-up


## 节点清单

| 节点 | 类型 |
|------|------|
| ATS: New Application Received | Webhook |
| Normalize Candidate Data | 数据设置 |
| Has Valid Phone? | IF 判断 |
| No Phone — Skip | 空操作 |
| Aloware: Create or Update Contact | HTTP Request |
| Is Sales Role? | IF 判断 |
| SMS: Sales Role Welcome | HTTP Request |
| Aloware: Sales Pre-screening Sequence | HTTP Request |
| Is Engineering Role? | IF 判断 |
| SMS: Engineering Role Welcome | HTTP Request |
| Aloware: Tech Pre-screening Sequence | HTTP Request |
| SMS: General Role Welcome | HTTP Request |
| Aloware: General Pre-screening Sequence | HTTP Request |
| Wait 24h (Sales) | 等待 |
| Wait 24h (Tech) | 等待 |
| Wait 24h (General) | 等待 |
| Check Response (Sales) | HTTP Request |
| Check Response (Tech) | HTTP Request |
| Check Response (General) | HTTP Request |
| Did Respond? (Sales) | IF 判断 |
| Did Respond? (Tech) | IF 判断 |
| Did Respond? (General) | IF 判断 |
| Candidate Engaged — Done | 空操作 |
| Aloware: Send Follow-up SMS | HTTP Request |
| Slack: Notify Hiring Manager | Slack |

## 触发方式
- ATS: New Application Received 触发

## 统计
- 节点总数：25
- 触发节点：1
- 处理节点：12
- 输出节点：12
- 分类：workflow-automation
