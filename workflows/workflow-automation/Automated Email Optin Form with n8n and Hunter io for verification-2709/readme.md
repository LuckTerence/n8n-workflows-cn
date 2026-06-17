## 简介
**Automated Email Optin Form with n8n and Hunter io for verification**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2709

---

# Automated Email Optin Form with n8n and Hunter io for verification


## 节点清单

| 节点 | 类型 |
|------|------|
| Email is not valid, do nothing | 空操作 |
| Check if the email is valid | IF 判断 |
| Verify email | hunter |
| Submit form | 表单触发器 |
| Add contact to list | sendGrid |

## 触发方式
- Submit form 触发

## 统计
- 节点总数：5
- 触发节点：1
- 处理节点：4
- 输出节点：0
- 分类：workflow-automation
