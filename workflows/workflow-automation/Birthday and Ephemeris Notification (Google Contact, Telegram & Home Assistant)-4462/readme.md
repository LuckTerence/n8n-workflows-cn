## 简介
**Birthday and Ephemeris Notification (Google Contact, Telegram & Home Assistant)**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：21 | 难度：⭐⭐⭐ 高级
> 原始来源：https://n8nworkflows.xyz/workflows/4462

---

# Birthday and Ephemeris Notification (Google Contact, Telegram & Home Assistant)


## 节点清单

| 节点 | 类型 |
|------|------|
| Google Contacts | googleContacts |
| Get One first name list | 数据设置 |
| First names | 数据聚合 |
| Nominis - Saints du jour | HTTP Request |
| Combine Firstname & Saints | 数据合并 |
| No Saint Today ? | IF 判断 |
| Compose Message | 数据设置 |
| Single list Birthday | 数据设置 |
| Get Nominis URL | 数据设置 |
| Sent Telegram Message | Telegram |
| Birthday Today? | IF 判断 |
| Set Date Offset | 数据设置 |
| Everyday at 7am | 定时触发器 |
| List of Saints of the day | 数据设置 |
| Check if any firstname match a Saints of the day | Code |
| Aggregate Birthdays | 数据聚合 |
| Aggregate No Birthday | 数据聚合 |
| "Bonne fête" celebration message | 数据设置 |
| Birthday celebration message | 数据设置 |
| Merge Birthday + Fête Messages | 数据合并 |
| Check if any celebration to make | IF 判断 |
| Send to Google Home Speaker | homeAssistant |

## 触发方式
- Everyday at 7am 触发

## 统计
- 节点总数：22
- 触发节点：1
- 处理节点：19
- 输出节点：2
- 分类：workflow-automation
