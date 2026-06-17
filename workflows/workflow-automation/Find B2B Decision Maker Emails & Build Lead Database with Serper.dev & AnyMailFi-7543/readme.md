## 简介
**Find B2B Decision Maker Emails & Build Lead Database with Serper.dev & AnyMailFinder**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A-adapted（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/7543

---

# Find B2B Decision Maker Emails & Build Lead Database with Serper.dev & AnyMailFinder


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Execute workflow’ | 手动触发 |
| Get many rows | NocoDB |
| serper search domains | HTTP Request |
| extract url & domain | OpenAI |
| Get Sales Decision Maker Email | HTTP Request |
| Get Marketing Email | HTTP Request |
| Get CEO Email | HTTP Request |
| Update Companies Domains | NocoDB |
| Update Company Status | NocoDB |
| Filter | 过滤器 |
| Remove Duplicates | 去重 |
| Merge1 | 数据合并 |
| Extract Data3 | 数据设置 |
| Extract Data4 | 数据设置 |
| Extract Data5 | 数据设置 |
| Determine Email Status by Company | Code |
| Get All Company Status | NocoDB |
| If Only Risky Emails1 | 过滤器 |
| If Email Found1 | IF 判断 |
| Get All Company Emails | HTTP Request |
| Update Company Emails | NocoDB |
| Loop Over Items | 分批处理 |
| Filter1 | 过滤器 |
| Create Contacts | NocoDB |
| Wait | 等待 |
| Schedule Trigger2 | 定时触发器 |
| Merge | 数据合并 |

## 触发方式
- When clicking ‘Execute workflow’ 触发
- Schedule Trigger2 触发

## 统计
- 节点总数：27
- 触发节点：2
- 处理节点：20
- 输出节点：5
- 分类：workflow-automation
