## 简介
**Route and validate B2B form leads with webhook firewall and SMTP emails**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：11 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/15630

---

# Route and validate B2B form leads with webhook firewall and SMTP emails


## 节点清单

| 节点 | 类型 |
|------|------|
| Form Webhook | Webhook |
| Format Tally Data | Code |
| Extract Form Data | 数据设置 |
| Validate Lead | IF 判断 |
| Switch by Service Tier | Switch 路由 |
| Email - Audit | Email 发送 |
| Email - Implementation | Email 发送 |
| Email - Managed Services | Email 发送 |
| Email - Generic/Fallback | Email 发送 |
| Notify Internal Team | Email 发送 |
| Success Response | 响应 Webhook |
| Error Response | 响应 Webhook |

## 触发方式
- Form Webhook 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：4
- 输出节点：7
- 分类：workflow-automation
