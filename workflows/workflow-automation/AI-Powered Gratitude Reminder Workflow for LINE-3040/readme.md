## 简介
**AI-Powered Gratitude Reminder Workflow for LINE**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3040

---

# AI-Powered Gratitude Reminder Workflow for LINE


## 节点清单

| 节点 | 类型 |
|------|------|
| Trigger 2100 Bear Gratitude Jar Notice | 定时触发器 |
| WriteReminder | LLM Chain |
| Reformat Output from Chat Model | 数据设置 |
| Azure OpenAI Chat Model | Azure OpenAI Chat Model |
| Line Push Message | HTTP Request |

## 触发方式
- Trigger 2100 Bear Gratitude Jar Notice 触发

## 统计
- 节点总数：5
- 触发节点：1
- 处理节点：3
- 输出节点：1
- 分类：workflow-automation
