## 简介
**Multi-Channel Customer Support Automation Suite**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：13 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/5135

---

# Multi-Channel Customer Support Automation Suite


## 节点清单

| 节点 | 类型 |
|------|------|
| Email Trigger | Email 读取 |
| Web Form Webhook | Webhook |
| Normalize Messages | Function |
| Categorize & Prioritize | Function |
| Check Auto-Response | IF 判断 |
| Generate Auto-Response | Function |
| Send Auto-Response | Email 发送 |
| Notify Slack | Slack |
| Store in CRM | Function |
| Log Success | Function |
| Error Handler | Function |
| Merge | 数据合并 |
| Notify Error to Slack | HTTP Request |
| Webhook Response | 响应 Webhook |

## 触发方式
- Web Form Webhook 触发

## 统计
- 节点总数：14
- 触发节点：1
- 处理节点：8
- 输出节点：5
- 分类：workflow-automation
