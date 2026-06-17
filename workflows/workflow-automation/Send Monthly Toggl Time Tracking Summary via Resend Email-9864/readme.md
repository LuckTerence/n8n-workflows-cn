## 简介
**Send Monthly Toggl Time Tracking Summary via Resend Email**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/9864

---

# Send Monthly Toggl Time Tracking Summary via Resend Email


## 节点清单

| 节点 | 类型 |
|------|------|
| Get Toggle Projects | HTTP Request |
| Schedule Trigger | 定时触发器 |
| Get Toggle Summary | HTTP Request |
| Prepare html raport | Code |
| Send email via Resend | HTTP Request |
| Merge data | 数据合并 |
| Prepare projects list | Code |

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：7
- 触发节点：1
- 处理节点：3
- 输出节点：3
- 分类：workflow-automation
