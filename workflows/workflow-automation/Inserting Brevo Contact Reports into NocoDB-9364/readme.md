## 简介
**Inserting Brevo Contact Reports into NocoDB**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：21 | 难度：⭐⭐⭐ 高级
> 原始来源：https://n8nworkflows.xyz/workflows/9364

---

# Inserting Brevo Contact Reports into NocoDB


## 节点清单

| 节点 | 类型 |
|------|------|
| Get Brevo Contact Report | HTTP Request |
| Split Out - messagesSent | 数据拆分 |
| Split Out - delivered | 数据拆分 |
| Split Out - opened | 数据拆分 |
| Code | Code |
| Edit Fields | 数据设置 |
| Code1 | Code |
| Edit Fields2 | 数据设置 |
| Code2 | Code |
| Edit Fields3 | 数据设置 |
| Code3 | Code |
| Edit Fields4 | 数据设置 |
| Schedule Trigger | 定时触发器 |
| Split Out - clicked | 数据拆分 |
| Check if Email is Inserted Before | 过滤器 |
| Merge | 数据合并 |
| Delete Nulls | Code |
| Update NocoDB | NocoDB |
| If Email Blacklisted | IF 判断 |
| Loop | 分批处理 |
| Update NocoDB - blacklisted | NocoDB |
| Insert Emails from NocoDB | NocoDB |

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：22
- 触发节点：1
- 处理节点：20
- 输出节点：1
- 分类：workflow-automation
