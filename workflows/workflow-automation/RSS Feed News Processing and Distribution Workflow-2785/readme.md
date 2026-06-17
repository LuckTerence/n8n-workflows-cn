## 简介
**RSS Feed News Processing and Distribution Workflow**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A-adapted（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2785

---

# RSS Feed News Processing and Distribution Workflow


## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Trigger | 定时触发器 |
| RSS Read Testing Catalog | RSS Feed |
| Transform date | 数据设置 |
| Filter by date (more than 7 days) | 过滤器 |
| Sort by date | 数据排序 |
| Limit news to x | 数据限制 |
| Transform new to MD | Code |
| Publish comment | trello |
| Send revision email | Email 发送 |
| Merge | 数据合并 |
| RSS Read marktechpost | RSS Feed |
| RSS Read | RSS Feed |

## 触发方式
- Schedule Trigger 触发
- RSS Read Testing Catalog 触发
- RSS Read marktechpost 触发
- RSS Read 触发

## 统计
- 节点总数：12
- 触发节点：4
- 处理节点：7
- 输出节点：1
- 分类：workflow-automation
