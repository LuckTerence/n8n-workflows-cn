## 简介
**Daily Import Validated Contacts from NocoDB to Brevo**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：8 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/7216

---

# Daily Import Validated Contacts from NocoDB to Brevo


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
