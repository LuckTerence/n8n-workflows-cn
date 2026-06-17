# Bulk Auto-Publish Videos to Social Networks with AI Copy and Client Approval

https://n8nworkflows.xyz/workflows/11638

## 节点清单

| 节点 | 类型 |
|------|------|
| Start Campaign | 表单触发器 |
| Campaign Settings | 数据设置 |
| Fetch Videos from Drive | Google Drive |
| Video Files Only | 过滤器 |
| Build Schedule Calendar | Code |
| Process Each Video | 分批处理 |
| Download from Drive | Google Drive |
| AI Video Analysis | OpenAI Chat Model |
| Generate Social Copy | AI Agent |
| Gemini Pro | OpenAI Chat Model |
| Structured Output Parser | 结构化输出解析器 |
| Format Content Data | Code |
| Save Draft to Sheet | Google Sheets |
| Publisher Config | 数据设置 |
| Load Content Queue | Google Sheets |
| Only Approved | 过滤器 |
| Process Queue | 分批处理 |
| Get Video File | Google Drive |
| Build Upload Payload | Code |
| TikTok Enabled? | IF 判断 |
| Instagram Enabled? | IF 判断 |
| YouTube Enabled? | IF 判断 |
| Schedule TikTok | uploadPost |
| Schedule Instagram | uploadPost |
| Schedule YouTube | uploadPost |
| Mark as Scheduled | Google Sheets |
| 15 mins check | 定时触发器 |

## 触发方式
- Start Campaign 触发
- 15 mins check 触发

## 统计
- 节点总数：27
- 触发节点：2
- 处理节点：25
- 输出节点：0
- 分类：workflow-automation
