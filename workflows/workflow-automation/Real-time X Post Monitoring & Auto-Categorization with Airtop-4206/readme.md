## 简介
**Real-time X Post Monitoring & Auto-Categorization with Airtop**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4206

---

# Real-time X Post Monitoring & Auto-Categorization with Airtop


## 节点清单

| 节点 | 类型 |
|------|------|
| When Executed by Another Workflow | 执行工作流触发器 |
| Extract posts | Airtop |
| Session | Airtop |
| Window | Airtop |
| End session | Airtop |
| Filter out [NA] posts | 过滤器 |
| Parse JSON output | Code |
| Inputs | 数据设置 |

## 触发方式
- When Executed by Another Workflow 触发

## 统计
- 节点总数：8
- 触发节点：1
- 处理节点：7
- 输出节点：0
- 分类：workflow-automation
