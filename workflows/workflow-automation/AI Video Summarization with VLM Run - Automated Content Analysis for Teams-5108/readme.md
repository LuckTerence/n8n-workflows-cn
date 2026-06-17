# AI Video Summarization with VLM Run - Automated Content Analysis for Teams

https://n8nworkflows.xyz/workflows/5108

## 节点清单

| 节点 | 类型 |
|------|------|
| VLM Run Video Summarizer | vlmRun |
| Monitor Video Uploads | Google Drive 触发器 |
| Download Video File | Google Drive |
| Receive VLM Run Callback | Webhook |
| Send Summary to Team | Slack |

## 触发方式
- Monitor Video Uploads 触发
- Receive VLM Run Callback 触发

## 统计
- 节点总数：5
- 触发节点：2
- 处理节点：2
- 输出节点：1
- 分类：workflow-automation
