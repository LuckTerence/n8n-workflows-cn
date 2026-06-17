## 简介
**B2B lead qualification**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5404

---

# B2B lead qualification


## 节点清单

| 节点 | 类型 |
|------|------|
| New Lead Captured | Google Sheets 触发器 |
| Initiate Voice Call (VAPI) | HTTP Request |
| Save Qualified Lead to CRM Sheet | Google Sheets |
| Send Call Data Acknowledgement | 响应 Webhook |
| Receive Lead Details from VAPI | Webhook |

## 触发方式
- New Lead Captured 触发
- Receive Lead Details from VAPI 触发

## 统计
- 节点总数：5
- 触发节点：2
- 处理节点：1
- 输出节点：2
- 分类：workflow-automation
