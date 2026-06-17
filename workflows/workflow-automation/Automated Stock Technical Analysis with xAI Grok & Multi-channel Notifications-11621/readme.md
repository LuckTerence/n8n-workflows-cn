# Automated Stock Technical Analysis with xAI Grok & Multi-channel Notifications

https://n8nworkflows.xyz/workflows/11621

## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Trigger | 定时触发器 |
| Interpret Data | Code |
| Rapiwa | rapiwa |
| Send a message | Email 发送 |
| Fetch Stock Market Data | HTTP Request |
| Send warning message | Telegram |
| Send Market Summary message | Telegram |
| Memory | 记忆缓冲区 |
| Analysis Agent | AI Agent |
| Send Market Summary On Channel | Telegram |
| Get Market Condition | HTTP Request |
| Check Market is open/close | IF 判断 |
| Currency/Symble List | 数据设置 |
| RSS Read | rssFeedReadTool |
| xAI | lmChatXAiGrok |
| Append row in sheet | Google Sheets |
| Clicking | 手动触发 |

## 触发方式
- Schedule Trigger 触发
- RSS Read 触发
- Clicking 触发

## 统计
- 节点总数：17
- 触发节点：3
- 处理节点：8
- 输出节点：6
- 分类：workflow-automation
