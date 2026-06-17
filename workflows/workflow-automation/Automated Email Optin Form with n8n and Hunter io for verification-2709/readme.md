# Automated Email Optin Form with n8n and Hunter io for verification

https://n8nworkflows.xyz/workflows/2709

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
