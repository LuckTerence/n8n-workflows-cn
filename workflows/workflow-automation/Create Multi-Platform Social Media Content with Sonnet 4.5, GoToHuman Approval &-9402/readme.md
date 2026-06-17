# Create Multi-Platform Social Media Content with Sonnet 4.5, GoToHuman Approval & Sheets

https://n8nworkflows.xyz/workflows/9402

## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Execute workflow’ | 手动触发 |
| Send review request and wait for response | gotoHuman |
| Switch | Switch 路由 |
| Loop Over Items | 分批处理 |
| Update row in sheet | Google Sheets |
| Social Media Content Creator | AI Agent |
| Schedule Trigger | 定时触发器 |
| Set Text | 数据设置 |
| Set new prompt | 数据设置 |
| Get ideas | Google Sheets |
| Anthropic Chat Model | OpenAI Chat Model |

## 触发方式
- When clicking ‘Execute workflow’ 触发
- Schedule Trigger 触发

## 统计
- 节点总数：11
- 触发节点：2
- 处理节点：9
- 输出节点：0
- 分类：workflow-automation
