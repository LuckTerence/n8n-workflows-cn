## 简介
**Food Menu Update Notifier**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：B（需替换Twilio/Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5877

---

# Food Menu Update Notifier


## 节点清单

| 节点 | 类型 |
|------|------|
| Send WhatsApp Notification | HTTP Request |
| Daily Menu Update Scheduler | 定时触发器 |
| Fetch Special Menu Data | Google Sheets |
| Detect Menu Changes | Code |
| Generate Menu Alert Message | Code |
| Fetch Customer Contact List | Google Sheets |
| Merge Menu with Customer Data | 数据设置 |
| Split by Notification Preference | 分批处理 |
| Filter WhatsApp Users | IF 判断 |
| Log WhatsApp Status | Google Sheets |
| Filter Email Users | IF 判断 |
| Send Menu Email | Email 发送 |
| Filter SMS Users | IF 判断 |
| Log Email Status1 | Google Sheets |
| Send Twilio SMS Alert | HTTP Request |
|  Log SMS Status | Google Sheets |
| Wait For All data | 等待 |

## 触发方式
- Daily Menu Update Scheduler 触发

## 统计
- 节点总数：17
- 触发节点：1
- 处理节点：13
- 输出节点：3
- 分类：workflow-automation
