# Smart irrigation scheduler with weather forecast and soil analysis

https://n8nworkflows.xyz/workflows/11939

## 节点清单

| 节点 | 类型 |
|------|------|
| Daily Morning Check | 定时触发器 |
| Manual Override Trigger | Webhook |
| Merge Triggers | 数据合并 |
| Define Irrigation Zones | 数据设置 |
| Split Zones | 数据拆分 |
| Get Current Weather | openWeatherMap |
| Get 5-Day Forecast | openWeatherMap |
| Merge Weather Data | 数据合并 |
| Analyze Irrigation Need | Code |
| Filter Zones Needing Water | 过滤器 |
| Aggregate All Results | 数据聚合 |
| Generate Irrigation Schedule | Code |
| Has Irrigation Tasks? | IF 判断 |
| Log to Google Sheets | Google Sheets |
| Send IoT Commands | HTTP Request |
| Send Slack Report | Slack |
| Log No Action | 数据设置 |
| Respond to Webhook | 响应 Webhook |

## 触发方式
- Daily Morning Check 触发
- Manual Override Trigger 触发

## 统计
- 节点总数：18
- 触发节点：2
- 处理节点：13
- 输出节点：3
- 分类：workflow-automation
