## 简介
**Automate purchase bill processing with AI OCR & QuickBooks integration**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/12013

---

# Automate purchase bill processing with AI OCR & QuickBooks integration


## 节点清单

| 节点 | 类型 |
|------|------|
| Split Items to Create | 数据拆分 |
| Create Items | HTTP Request |
| Merge Item Creation Paths | 数据合并 |
| Collect All Item Mappings | Code |
| Find Vendor | QuickBooks |
| Vendor Exists? | IF 判断 |
| Create Vendor | QuickBooks |
| Create Bill  | HTTP Request |
| Need to Create Items? | IF 判断 |
| Get All QB Items | QuickBooks |
| Prepare Items to Check | Code |
| Extract Invoice Data | 信息提取器 |
| Clean Text | Code |
| Loop Over Invoices | 分批处理 |
| Convert to Separate Items | Code |
| Extract from PDF | 从文件提取 |
| Check Which Items to Create | Code |
| Build Bill Payload | Code |
| OpenRouter Chat Model | OpenRouter Chat Model |
| On bill submission | 表单触发器 |

## 触发方式
- On bill submission 触发

## 统计
- 节点总数：20
- 触发节点：1
- 处理节点：17
- 输出节点：2
- 分类：workflow-automation
