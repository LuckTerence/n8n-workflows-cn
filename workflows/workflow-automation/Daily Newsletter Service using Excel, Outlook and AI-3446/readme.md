## 简介
**Daily Newsletter Service using Excel, Outlook and AI**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A-adapted（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3446

---

# Daily Newsletter Service using Excel, Outlook and AI


## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Trigger | 定时触发器 |
| Get Subscribers | microsoftExcel |
| Get Unique Categories | 数据设置 |
| OpenAI Chat Model | OpenAI Chat Model |
| Aggregate | 数据聚合 |
| Collect Fields | 数据设置 |
| Categories to Items | 数据拆分 |
| For Each Category | 分批处理 |
| Workflows to Items | 数据拆分 |
| Workflow Summarizer | LLM Chain |
| Merge | 数据合并 |
| Fetch Latest 10 per Category | HTTP Request |
| No Operation, do nothing | 空操作 |
| Get Relevant Workflows | 数据设置 |
| Flatten Workflows | 数据设置 |
| Remove Already Seen | 去重 |
| Workflow to Items | 数据拆分 |
| Combine Workflows | 数据聚合 |
| Has New Workflows? | IF 判断 |
| With User Reference | 数据设置 |
| Generate HTML Template | HTML |
| Parse Rows | 数据设置 |
| Send Daily Digest | Outlook |
| Append Category | 数据设置 |
| For Each Subscriber | 分批处理 |

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：25
- 触发节点：1
- 处理节点：22
- 输出节点：2
- 分类：workflow-automation
