## 简介
**Generate GLPI Support Performance Reports with SLA Tracking & Email Delivery**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/9210

---

# Generate GLPI Support Performance Reports with SLA Tracking & Email Delivery


## 节点清单

| 节点 | 类型 |
|------|------|
| Variables | 数据设置 |
| Edit Fields | 数据设置 |
| Split Out | 数据拆分 |
| Send a message | Email 发送 |
| Get tickets | HTTP Request |
| Schedule Trigger | 定时触发器 |
| Get session token | HTTP Request |
| End session | HTTP Request |
| No Operation, do nothing | 空操作 |
| Date range | Code |
| Metrics | Code |
| Generate report | HTML |

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：7
- 输出节点：4
- 分类：workflow-automation
