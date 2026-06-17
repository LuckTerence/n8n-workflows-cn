## 简介
**Generate AI camera moves with Seedance and build a previs review board**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A-adapted（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/14891

---

# Generate AI camera moves with Seedance and build a previs review board


## 节点清单

| 节点 | 类型 |
|------|------|
| Extract & Map Form Fields | Code |
| AI Agent: Generate Camera Options | AI Agent |
| Azure OpenAI: GPT-4o Mini | Azure OpenAI Chat Model |
| Parse AI Response → Seedance Items | Code |
| Build Seedance API Request | Code |
| Seedance: Submit Camera Move Job | HTTP Request |
| Store Job ID + Move Metadata | Code |
| Poll: Check Move Render Status | HTTP Request |
| Move Render Complete? | IF 判断 |
| Wait 20s Before Retry | 等待 |
| Collect Move + Tag Key Frames | Code |
| Download Lighting Reference Video | HTTP Request |
| Google Drive: Archive Lighting Ref | Google Drive |
| Jira: Create Previs Review Task | jira |
| ClickUp: Create Previs Production Record | clickUp |
| Telegram: Deliver Previs to Supervisor | Telegram |
| Telegram: Alert on AI Agent Failure | Telegram |
| Form: Previs Brief Input1 | 表单触发器 |
| Compile Previs Board Package1 | Code |
| Slack: Publish Previs Board1 | Slack |
| On Workflow Error | 错误触发器 |
| Slack: Error Alert | Slack |

## 触发方式
- Form: Previs Brief Input1 触发
- On Workflow Error 触发

## 统计
- 节点总数：22
- 触发节点：2
- 处理节点：13
- 输出节点：7
- 分类：workflow-automation
