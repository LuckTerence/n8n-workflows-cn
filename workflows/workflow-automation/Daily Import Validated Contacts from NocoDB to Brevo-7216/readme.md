# Daily Import Validated Contacts from NocoDB to Brevo

https://n8nworkflows.xyz/workflows/7216

## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Trigger | 定时触发器 |
| Check if parameters are not empty | IF 判断 |
| Check if email is Disposal | IF 判断 |
| Loop Over Items | 分批处理 |
| Brevo: Create Contact | sendInBlue |
| NocoDB: Get new users list | NocoDB |
| NocoDB: change status to 1-empty-fields | NocoDB |
| NocoDB: change status to 2-disposal-email | NocoDB |
| NocoDB: change status to 3-contact-created | NocoDB |

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：8
- 输出节点：0
- 分类：workflow-automation
