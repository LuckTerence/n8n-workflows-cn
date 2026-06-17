## 简介
**Automatic Subscriber Creation in Beehiiv from Systeme.io Funnel Optins**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：B（需替换Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5992

---

# Automatic Subscriber Creation in Beehiiv from Systeme.io Funnel Optins


## 节点清单

| 节点 | 类型 |
|------|------|
| Clean Data | 数据设置 |
| Create New Beehiiv Subscriber | HTTP Request |
| Subscriber Created? | IF 判断 |
| Send Email Alert (Beehiiv API error) | Email 发送 |
| Configure Workflow | 数据设置 |
| On New Systeme.io Optin | Webhook |

## 触发方式
- On New Systeme.io Optin 触发

## 统计
- 节点总数：6
- 触发节点：1
- 处理节点：3
- 输出节点：2
- 分类：workflow-automation
