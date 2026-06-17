## 简介
**Automated Upload & Send a Large File with TransferNow**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/8742

---

# Automated Upload & Send a Large File with TransferNow


## 节点清单

| 节点 | 类型 |
|------|------|
| On form submission | 表单触发器 |
| Calculate size | Code |
| Set Json | 数据设置 |
| Set Transfer | HTTP Request |
| Get Upload Url | HTTP Request |
| Upload done | HTTP Request |
| Get transfer data | HTTP Request |
| Get parameters | 数据设置 |
| Form | 表单 |
| Is complete? | IF 判断 |
| Send Transfer | HTTP Request |
| Send UploadUrl | HTTP Request |
| Merge | 数据合并 |

## 触发方式
- On form submission 触发

## 统计
- 节点总数：13
- 触发节点：1
- 处理节点：6
- 输出节点：6
- 分类：workflow-automation
