# Generate merchandise proposals and market research from NASA APOD

https://n8nworkflows.xyz/workflows/11291

## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Trigger1 | 定时触发器 |
| Workflow Configuration1 | 数据设置 |
| Get NASA APOD1 | nasa |
| Generate Keywords & Check Logo1 | OpenAI |
| Create Mockup with Cloudinary1 | HTTP Request |
| Search Etsy Market1 | apify |
| Calculate Profit1 | Code |
| Merge Data1 | 数据合并 |
| AI Marketing Advisor1 | OpenAI |
| Send Slack Proposal1 | Slack |
| Wait for User Decision1 | 等待 |
| Check User Decision1 | Switch 路由 |
| Download NASA Image1 | HTTP Request |
| Save to Google Drive1 | Google Drive |
| Save to Notion DB1 | Notion |

## 触发方式
- Schedule Trigger1 触发

## 统计
- 节点总数：15
- 触发节点：1
- 处理节点：11
- 输出节点：3
- 分类：workflow-automation
