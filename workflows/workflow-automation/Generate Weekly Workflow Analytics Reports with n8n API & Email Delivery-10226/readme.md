## 简介
**Generate Weekly Workflow Analytics Reports with n8n API & Email Delivery**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/10226

---

# Generate Weekly Workflow Analytics Reports with n8n API & Email Delivery


## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Trigger | 定时触发器 |
| Get all previous executions | n8n |
| Get all Workflows | n8n |
| Merge | 数据合并 |
| Edit Field ID to workflowId | 数据设置 |
| Filter executions last week | 过滤器 |
| Prepare html report | Code |
| Send a message gmail | Email 发送 |
| Send a message outlook | Outlook |

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：6
- 输出节点：2
- 分类：workflow-automation
