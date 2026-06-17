# Daily Company Online Presence Monitor with AI Sentiment Analysis & Multi-platform Tracking

https://n8nworkflows.xyz/workflows/6668

## 节点清单

| 节点 | 类型 |
|------|------|
| Daily Morning Trigger (9 AM) | 定时触发器 |
| Set Company Details | 数据设置 |
| Fetch Google News RSS | rssFeed |
| Prepare News for Merge | Function |
| Search Reddit Posts | reddit |
| Prepare Reddit for Merge | Function |
| Search YouTube Videos | youTube |
| Prepare YouTube for Merge | Function |
| Merge All Mentions | 列表操作 |
| SQLite: Ensure Table Exists | sqlite |
| Filter New Mentions (Deduplication) | Function |
| SQLite: Check If Processed | sqlite |
| AI: Analyze Sentiment & Summarize | OpenAI |
| Process AI Results & Categorize | Function |
| SQLite: Record Processed Mentions | sqlite |
| Format Report Email | Function |
| Send Report Email | Email 发送 |

## 触发方式
- Daily Morning Trigger (9 AM) 触发

## 统计
- 节点总数：17
- 触发节点：1
- 处理节点：15
- 输出节点：1
- 分类：workflow-automation
