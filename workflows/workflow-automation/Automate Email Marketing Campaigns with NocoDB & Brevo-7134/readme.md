## 简介
**Automate Email Marketing Campaigns with NocoDB & Brevo**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/7134

---

# Automate Email Marketing Campaigns with NocoDB & Brevo


## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Trigger | 定时触发器 |
| Setup Flow | 数据设置 |
| Map Data | 数据设置 |
| Filter Template | 过滤器 |
| IF Template Parameters OK | IF 判断 |
| IF user_id is not empty | IF 判断 |
| Change Status to Sending | NocoDB |
| Get all flow templates from NocoDB | NocoDB |
| Wait | 等待 |
| Remove Duplicates | 去重 |
| Add records By Status Processing | NocoDB |
| Insert Data By Status Processing | NocoDB |
| IF Type Email | IF 判断 |
| Brevo Send Email | sendInBlue |
| Update Data | NocoDB |
| Status-no-email | NocoDB |
| Schedule Trigger1 | 定时触发器 |
| Insert Data By Status Sending | NocoDB |
| Status-disposal-email | NocoDB |
| Get user_id from dcp | NocoDB |
| If email is not empty | IF 判断 |
| Disposal Check | IF 判断 |

## 触发方式
- Schedule Trigger 触发
- Schedule Trigger1 触发

## 统计
- 节点总数：22
- 触发节点：2
- 处理节点：20
- 输出节点：0
- 分类：workflow-automation
