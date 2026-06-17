## 简介
**CallForge - 04 - AI Workflow for Gong.io Sales Calls**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A-adapted（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3034

---

# CallForge - 04 - AI Workflow for Gong.io Sales Calls


## 节点清单

| 节点 | 类型 |
|------|------|
| Loop to next call | 空操作 |
| Execute Workflow Trigger | 执行工作流触发器 |
| Create Notion DB Page | Notion |
| Post Slack Receipt | Slack |
| AI Team Processor | 执行工作流 |
| Update Slack Progress | Slack |
| Merge call data and parent notion id | 数据合并 |
| Reduce down to 1 object | 数据聚合 |
| Get all older Calls | Notion |
| Isolate Only Call IDs | 数据设置 |
| Only Process New Calls | compareDatasets |
| Reduce down to One object | 数据聚合 |
| Bundle Slack Message Data | 数据聚合 |
| Merge Slack and Call Data | 数据合并 |
| Loop Over Calls | 分批处理 |
| Bundle Notion Parent Object Data | 数据聚合 |
| Bundle Processed Calls | 数据聚合 |
| Post Completed Calls Message | Slack |

## 触发方式
- Execute Workflow Trigger 触发

## 统计
- 节点总数：18
- 触发节点：1
- 处理节点：14
- 输出节点：3
- 分类：workflow-automation
