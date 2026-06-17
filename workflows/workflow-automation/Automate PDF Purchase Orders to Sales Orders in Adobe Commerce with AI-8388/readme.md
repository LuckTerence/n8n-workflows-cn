## 简介
**Automate PDF Purchase Orders to Sales Orders in Adobe Commerce with AI**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/8388

---

# Automate PDF Purchase Orders to Sales Orders in Adobe Commerce with AI


## 节点清单

| 节点 | 类型 |
|------|------|
| Extract from File | 从文件提取 |
| Create cart | HTTP Request |
| On form submission | 表单触发器 |
| set Customer | 数据设置 |
| set Quote Id | 数据设置 |
| set Billing Address | HTTP Request |
| estimate Shipping Methods | HTTP Request |
| set Reference Number | HTTP Request |
| set OpenAI | 数据设置 |
| set Order Comment | HTTP Request |
| get Payment Methods | HTTP Request |
| Aggregate | 数据聚合 |
| check Companycredit | Code |
| When chat message received | Chat 触发器 |
| Extract from File1 | 从文件提取 |
| set Address | Code |
| get Configurable | HTTP Request |
| If companyCredit | IF 判断 |
| Merge | 数据合并 |
| set Express Shipping Method | HTTP Request |
| Limit | 数据限制 |
| set Standard Shipping Method | HTTP Request |
| set Feedback | 数据设置 |
| set Clean Articlenumber | 数据设置 |
| get Cart Items | HTTP Request |
| remove From Shopping Cart | HTTP Request |
| get Cart Items1 | HTTP Request |
| remove From Shopping Cart1 | HTTP Request |
| If Default Address | IF 判断 |
| set Feedback Default Address | 数据设置 |
| Switch | Switch 路由 |
| Extract from File2 | 从文件提取 |
| Stop and Error1 | 停止并报错 |
| No Operation, do nothing | 空操作 |
| Json error message | 数据设置 |
| Combine error fields | 数据设置 |
| No Operation, do nothing1 | 空操作 |
| Set successfull message | 数据设置 |
| Set empty email message | 数据设置 |
| Set empty products message | 数据设置 |
| Products not empty | IF 判断 |
| Emails not empty | IF 判断 |
| set Information | 数据设置 |
| set Information 2 | 数据设置 |
| Pay on account error message | 数据设置 |
| Set empty PO number message | 数据设置 |
| If PO number not empty | IF 判断 |
| Vorgangsnummer | 数据设置 |
| No Operation, do nothing3 | 空操作 |
| Split Out Products | 数据拆分 |
| Code | Code |
| get Products | 数据设置 |
| Execute Workflow | 执行工作流 |
| Wait | 等待 |
| Merge1 | 数据合并 |
| place Order | HTTP Request |
| filter Emailadresses | Code |
| remove SCH | Code |
| No Operation, do nothing4 | 空操作 |
| set Feedback configurable | 数据设置 |
| get Order by PO number | HTTP Request |
| Set empty PO number message1 | 数据设置 |
| IF PO number not exists | IF 判断 |
| Microsoft Outlook Trigger | microsoftOutlookTrigger |
| set Text | 数据设置 |
| AI Agent | AI Agent |
| Move a message | Outlook |
| No Operation, do nothing2 | 空操作 |
| get Customer | HTTP Request |
| If Customer | IF 判断 |
| Products | 空操作 |
| Azure OpenAI Chat Model1 | Azure OpenAI Chat Model |
| Loop until existing customer found | 分批处理 |
| If configurable product found | IF 判断 |
| Prepare sku & quote | 数据设置 |
| If product in cart | IF 判断 |
| Loop over products | 分批处理 |
| Combine processed skus | Code |
| Combine failed skus | Code |
| set Feedback failed | 数据设置 |
| set Feedback processed | 数据设置 |
| Combine feedback | Code |
| Keep 1 | 数据限制 |
| If express | IF 判断 |
| Split Emails | 数据拆分 |
| set Emails | 数据设置 |
| Email combine | 空操作 |
| If developer | IF 判断 |

## 触发方式
- On form submission 触发
- When chat message received 触发
- Microsoft Outlook Trigger 触发

## 统计
- 节点总数：88
- 触发节点：3
- 处理节点：68
- 输出节点：17
- 分类：workflow-automation
