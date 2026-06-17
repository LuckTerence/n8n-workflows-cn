# Automate Sports Betting Data with the Odds API

https://n8nworkflows.xyz/workflows/2843

## 节点清单

| 节点 | 类型 |
|------|------|
| Morning Trigger To Pull Data At 7:00am | 定时触发器 |
| Evening Trigger To Pull Data At 11:00pm | 定时触发器 |
| Retrieve Data Of Upcoming Sport Events For The Day | HTTP Request |
| Create Records Of Upcoming Events For The Day | Airtable |
| Retrieve Sport Results Data At The End Of The Day | HTTP Request |
| Combine Sport Results With Upcoming Events Records By Matching ID | 数据合并 |
| Update Table Records With Scores And Results For Sport Events | Airtable |

## 触发方式
- Morning Trigger To Pull Data At 7:00am 触发
- Evening Trigger To Pull Data At 11:00pm 触发

## 统计
- 节点总数：7
- 触发节点：2
- 处理节点：3
- 输出节点：2
- 分类：workflow-automation
