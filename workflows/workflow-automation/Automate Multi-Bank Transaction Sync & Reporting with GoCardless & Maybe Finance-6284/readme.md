## 简介
**Automate Multi-Bank Transaction Sync & Reporting with GoCardless & Maybe Finance**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：16 | 难度：⭐⭐⭐ 高级
> 原始来源：https://n8nworkflows.xyz/workflows/6284

---

# Automate Multi-Bank Transaction Sync & Reporting with GoCardless & Maybe Finance


## 节点清单

| 节点 | 类型 |
|------|------|
| Get access token | HTTP Request |
| Get Revolut Pro transactions | HTTP Request |
| Get Revolut Personal transactions | HTTP Request |
| Get accounts id from Maybe | HTTP Request |
| Step 2 - Get institution id | HTTP Request |
| Step 5 - Get account id | HTTP Request |
| Create transactions to Maybe | HTTP Request |
| Merge all transactions in one array | 数据合并 |
| Resend | resend |
| Extract booked - Revolut Personal | 列表操作 |
| Extract booked - Revolut Pro | 列表操作 |
| Set transactions for Revolut Pro | 数据设置 |
| Set transactions for Revolut Personal | 数据设置 |
| Schedule Trigger | 定时触发器 |
| Step 4 - Building link with Revolut | HTTP Request |
| Step 3a - User agreement with first Revolut Account | HTTP Request |
| Step 3a - User agreement with second Revolut Account | HTTP Request |

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：17
- 触发节点：1
- 处理节点：6
- 输出节点：10
- 分类：workflow-automation
