## 简介
**List social media activity of a company before a call**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2124

---

# List social media activity of a company before a call


## 节点清单

| 节点 | 类型 |
|------|------|
| Get recetn tweets | HTTP Request |
| Setup | 数据设置 |
| Every morning @ 7 | 定时触发器 |
| Get meetings for today | Google Calendar |
| Get attendees email domains | 数据设置 |
| Split Out | 数据拆分 |
| Get recent LinkedIn posts | HTTP Request |
| Enrich attendee company | clearbit |
| Gmail | Email 发送 |
| Format LinkedIn Posts | Code |
| Format Tweets | Code |
| Combine all activity for a company | 数据合并 |
| Extract data for email | 数据设置 |
| Prepare email template | HTML |
| Switch | Switch 路由 |
| Keep only ones with the domain | 过滤器 |

## 触发方式
- Every morning @ 7 触发

## 统计
- 节点总数：16
- 触发节点：1
- 处理节点：12
- 输出节点：3
- 分类：workflow-automation
