# Monitor NASA asteroid threats with AI fact-check and multi-channel alerts

https://n8nworkflows.xyz/workflows/11289

## 节点清单

| 节点 | 类型 |
|------|------|
| Daily Schedule | 定时触发器 |
| Webhook Trigger | Webhook |
| Merge Triggers | 数据合并 |
| Get NASA Asteroid Data | nasa |
| Analyze Asteroid Threats | Code |
| Check for Hazardous Objects | IF 判断 |
| Configure Regional Search | Code |
| Loop Over Regions | 分批处理 |
| Search Regional News | apify |
| Aggregate All News | 数据聚合 |
| AI Fact-Check Analysis | OpenAI |
| Parse AI Response | Code |
| Generate Visualization Charts | Code |
| Format Multi-Channel Messages | Code |
| Send Slack Alert | Slack |
| Send Discord Alert | Discord |
| Send Email Alert | Email 发送 |
| Webhook Response | 响应 Webhook |
| Log to Google Sheets | Google Sheets |
| Create All-Clear Status | Code |

## 触发方式
- Daily Schedule 触发
- Webhook Trigger 触发

## 统计
- 节点总数：20
- 触发节点：2
- 处理节点：14
- 输出节点：4
- 分类：workflow-automation
