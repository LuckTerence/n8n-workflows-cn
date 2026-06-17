## 简介
**Lusha to Easy Redmine CRM: Automated Lead Enrichment**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：6 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/10726

---

# Lusha to Easy Redmine CRM: Automated Lead Enrichment


## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Trigger | 定时触发器 |
| Split Out | 数据拆分 |
| Get Leads from Easy Redmine | easyRedmine |
| Get Data from Lusha | HTTP Request |
| Filter Leads Found in Lusha | 过滤器 |
| Contact Data Transformation for CRM | Code |
| Update Leads in Easy Redmine CRM | HTTP Request |

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：7
- 触发节点：1
- 处理节点：4
- 输出节点：2
- 分类：workflow-automation
