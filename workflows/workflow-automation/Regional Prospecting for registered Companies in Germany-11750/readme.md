## 简介
**Regional Prospecting for registered Companies in Germany**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/11750

---

# Regional Prospecting for registered Companies in Germany


## 节点清单

| 节点 | 类型 |
|------|------|
| Manual Trigger | 手动触发 |
| Validate Input | Code |
| Search Success? | IF 判断 |
| Normalize & Score Results | Code |
| Sort by Relevance | Code |
| High Quality Leads? | IF 判断 |
| Prepare High Quality Payload | 数据设置 |
| Prepare Medium Quality Payload | 数据设置 |
| Merge & Log Results | Code |
| Generate Summary Report | 数据设置 |
| Implisense Search | HTTP Request |
| Authorization | 数据设置 |
| Prepare Search Input | 数据设置 |

## 触发方式
- Manual Trigger 触发

## 统计
- 节点总数：13
- 触发节点：1
- 处理节点：11
- 输出节点：1
- 分类：workflow-automation
