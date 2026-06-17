## 简介
**Real Estate Lead Generation with BatchData Skip Tracing & CRM Integration**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3666

---

# Real Estate Lead Generation with BatchData Skip Tracing & CRM Integration


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking "Execute Workflow" | 手动触发 |
| Daily Schedule | 定时触发器 |
| Search Properties API | HTTP Request |
| Configure Search Parameters | 数据设置 |
| Filter Property Results | Code |
| Get Owner Contact Info | HTTP Request |
| Format Lead Data | Code |
| Create Excel Spreadsheet | 电子表格文件 |
| Push to CRM | hubspot |
| Email Notification | Email 发送 |
| Summarize Results | Code |

## 触发方式
- When clicking "Execute Workflow" 触发
- Daily Schedule 触发

## 统计
- 节点总数：11
- 触发节点：2
- 处理节点：6
- 输出节点：3
- 分类：workflow-automation
