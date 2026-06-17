## 简介
**Automated Stock Technical Analysis with xAI Grok & Multi-channel Notifications**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A-adapted（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/11621

---

# Automated Stock Technical Analysis with xAI Grok & Multi-channel Notifications


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
