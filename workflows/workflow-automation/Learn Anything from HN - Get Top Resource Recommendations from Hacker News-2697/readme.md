## 简介
**Learn Anything from HN - Get Top Resource Recommendations from Hacker News**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A-adapted（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2697

---

# Learn Anything from HN - Get Top Resource Recommendations from Hacker News


## 节点清单

| 节点 | 类型 |
|------|------|
| Google Gemini Chat Model | OpenAI Chat Model |
| Basic LLM Chain | LLM Chain |
| SearchAskHN | hackerNews |
| FindHNComments | HTTP Request |
| CombineIntoSingleText | 数据聚合 |
| SplitOutChildrenIDs | 数据拆分 |
| GetTopicFromToLearn | 表单触发器 |
| SendEmailWithTopResources | Email 发送 |
| Convert2HTML | Markdown |
| Finished | 空操作 |

## 触发方式
- GetTopicFromToLearn 触发

## 统计
- 节点总数：10
- 触发节点：1
- 处理节点：7
- 输出节点：2
- 分类：workflow-automation
