# Auto-Bidder for Freelancer.com with Telegram Approval and AI Proposals

https://n8nworkflows.xyz/workflows/6048

## 节点清单

| 节点 | 类型 |
|------|------|
| create a bid | HTTP Request |
| If | IF 判断 |
| AI Agent | AI Agent |
| OpenAI Chat Model | OpenAI Chat Model |
| ExtractDate | 数据设置 |
| SetInputs | 数据设置 |
| If1 | IF 判断 |
| Send Succuss | Telegram |
| Search | HTTP Request |
| GetProjects | 数据拆分 |
| Loop Over Items | 分批处理 |
| checkBidding | HTTP Request |
| Split Out | 数据拆分 |
| Edit Fields | 数据设置 |
| Aggregate | 数据聚合 |
| If2 | IF 判断 |
| GetApproval | Telegram |
| Canceled  | Telegram |
| When Executed by Another Workflow | 执行工作流触发器 |
| AlreadyBid | 数据设置 |
| When clicking ‘Execute workflow’ | 手动触发 |
| Execute Workflow | 执行工作流 |
| Schedule Trigger | 定时触发器 |
| Edit Fields1 | 数据设置 |
| Split Out1 | 数据拆分 |

## 触发方式
- When Executed by Another Workflow 触发
- When clicking ‘Execute workflow’ 触发
- Schedule Trigger 触发

## 统计
- 节点总数：25
- 触发节点：3
- 处理节点：16
- 输出节点：6
- 分类：workflow-automation
