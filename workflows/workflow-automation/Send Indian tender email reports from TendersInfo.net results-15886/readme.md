## 简介
**Send Indian tender email reports from TendersInfo.net results**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/15886

---

# Send Indian tender email reports from TendersInfo.net results


## 节点清单

| 节点 | 类型 |
|------|------|
| Webhook Trigger1 | Webhook |
| Parse Tender Response1 | Code |
| Select Email Fields1 | 数据设置 |
| Fetch Tender Data from API1 | HTTP Request |
| Filter GEM Tenders Only1 | 过滤器 |
| Respond to Webhook1 | 响应 Webhook |
| Build HTML Table | Code |

## 触发方式
- Webhook Trigger1 触发

## 统计
- 节点总数：7
- 触发节点：1
- 处理节点：4
- 输出节点：2
- 分类：workflow-automation
