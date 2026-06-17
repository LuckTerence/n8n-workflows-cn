## 简介
**Secure GET Webhooks with Query Parameter Validation for Limited Authentication Cases**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：B（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/9570

---

# Secure GET Webhooks with Query Parameter Validation for Limited Authentication Cases


## 节点清单

| 节点 | 类型 |
|------|------|
| Validation Failed | 停止并报错 |
| Secret valid? | IF 判断 |
| Do whatever your workflow is supposed to do | 空操作 |
| "Unprotected" Webhook | Webhook |

## 触发方式
- "Unprotected" Webhook 触发

## 统计
- 节点总数：4
- 触发节点：1
- 处理节点：3
- 输出节点：0
- 分类：workflow-automation
