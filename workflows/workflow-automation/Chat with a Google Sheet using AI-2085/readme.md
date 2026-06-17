## 简介
**Chat with a Google Sheet using AI**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：B（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2085

---

# Chat with a Google Sheet using AI


## 节点清单

| 节点 | 类型 |
|------|------|
| When chat message received | Chat 触发器 |
| OpenAI Chat Model1 | OpenAI Chat Model |
| Simple Memory | 记忆缓冲区 |
| When Executed by Another Workflow | 执行工作流触发器 |
| AI Agent | AI Agent |
| List columns tool | 工作流工具 |
| Get column values tool | 工作流工具 |
| Get customer tool | 工作流工具 |
| Set Google Sheet URL | 数据设置 |
| Get Google sheet contents | Google Sheets |
| Check operation | Switch 路由 |
| Get column names | 数据设置 |
| Prepare column data | 数据设置 |
| Filter | 过滤器 |
| Prepare output | Code |

## 触发方式
- When chat message received 触发
- When Executed by Another Workflow 触发

## 统计
- 节点总数：15
- 触发节点：2
- 处理节点：13
- 输出节点：0
- 分类：workflow-automation
