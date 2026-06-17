## 简介
**Credit Card Payment Reminder & Tracking-For Taiwan Banks**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Gmail)（基本改完，配置 API Key 应该就能跑）
> 节点数：29 | 难度：⭐⭐⭐ 高级
> 原始来源：https://n8nworkflows.xyz/workflows/2867

---

# Credit Card Payment Reminder & Tracking-For Taiwan Banks


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking 'Test workflow' | 手动触发 |
| Google Sheets | Google Sheets |
| Webhook | Webhook |
| Gmail-SINOPAC | Gmail 触发器 |
| SINOPAC_PDF | 从文件提取 |
| SINOPAC_set field | 数据设置 |
| Organize Data | 数据设置 |
| Create Google Calendar Event | Google Calendar |
| Update Google Calendar - change status | Google Calendar |
| Cathay_set field | 数据设置 |
| Gmail-CTBC | Gmail 触发器 |
| CTBC _set field | 数据设置 |
| Gmail-Cathay | Gmail 触发器 |
| Gmail-Fubon | Gmail 触发器 |
| Fubon_PDF | 从文件提取 |
| Fubon_set field | 数据设置 |
| Gmail-E.SUN | Gmail 触发器 |
| E.SUN_PDF | 从文件提取 |
| E.SUN_set field | 数据设置 |
| Gmail-DBS | Gmail 触发器 |
| DBS_PDF | 从文件提取 |
| DBS_set field | 数据设置 |
| Gmail-Union | Gmail 触发器 |
| Union_PDF | 从文件提取 |
| Union_set fields | 数据设置 |
| Gmail-Taishin | Gmail 触发器 |
| Taishin_PDF | 从文件提取 |
| Taishin_set fields | 数据设置 |
| Get Google Calendar Event by id | Google Calendar |
| Update Google Calendar event staus | Google Calendar |
| Update Google Sheets pay status | Google Sheets |

## 触发方式
- When clicking 'Test workflow' 触发
- Webhook 触发
- Gmail-SINOPAC 触发
- Gmail-CTBC 触发
- Gmail-Cathay 触发
- Gmail-Fubon 触发
- Gmail-E.SUN 触发
- Gmail-DBS 触发
- Gmail-Union 触发
- Gmail-Taishin 触发

## 统计
- 节点总数：31
- 触发节点：10
- 处理节点：21
- 输出节点：0
- 分类：workflow-automation
