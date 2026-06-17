## 简介
**Import E.ON W1000 Energy Meter Data to Home Assistant with Spook Integration**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/9010

---

# Import E.ON W1000 Energy Meter Data to Home Assistant with Spook Integration


## 节点清单

| 节点 | 类型 |
|------|------|
| Extract from File | 从文件提取 |
| Rename "*_1" keys for merge | renameKeys |
| Get last 5 messages | Email 发送 |
| Aggregate_id | 数据聚合 |
| Get a message[0] | Email 发送 |
| Rename "*_1" keys for merge1 | renameKeys |
| Rename "*_1" keys for merge2 | renameKeys |
| Extract default data from source (+A) | 数据拆分 |
| Extract '*_1' data from source (-A) | 数据拆分 |
| Extract '*_2' data from source (1_8_0) | 数据拆分 |
| Extract '*_3' data from source (2_8_0) | 数据拆分 |
| Merge (+A; -A) | 数据合并 |
| Rename "*_1" keys for merge3 | renameKeys |
| Merge (+A; -A)1 | 数据合并 |
| Merge (+A; -A)2 | 数据合并 |
| Calculate hourly sum and | Code |
| Spook: update +A hitorical data1 | homeAssistant |
| Spook: update -A hitorical data1 | homeAssistant |
| Generate 1_8_0 list for stats | 数据设置 |
| Generate 2_8_0 list for stats | 数据设置 |
| Generate 1_8_0 stats | 数据聚合 |
| Generate 2_8_0 stats | 数据聚合 |
| Update input_number.exportt entity state1 | homeAssistant |
| Update input_number.import entity state1 | homeAssistant |
| Gmail Trigger | Gmail 触发器 |
| Schedule Trigger | 定时触发器 |
| If attachment_0 is xlsx | IF 判断 |
| No Operation, do nothing1 | 空操作 |
| Email Trigger (IMAP) | Email 读取 |
| Check Email Subject | IF 判断 |
| Convert datetime to Spook format | 日期时间 |
| Convert Excel time | 日期时间 |

## 触发方式
- Gmail Trigger 触发
- Schedule Trigger 触发

## 统计
- 节点总数：32
- 触发节点：2
- 处理节点：27
- 输出节点：3
- 分类：workflow-automation
