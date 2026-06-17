## 简介
**Hacker News Throwback Machine - See What Was Hot on This Day, Every Year!**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2688

---

# Hacker News Throwback Machine - See What Was Hot on This Day, Every Year!


## 节点清单

| 节点 | 类型 |
|------|------|
| Basic LLM Chain | LLM Chain |
| Google Gemini Chat Model | OpenAI Chat Model |
| Schedule Trigger | 定时触发器 |
| CreateYearsList | Code |
| CleanUpYearList | 数据设置 |
| SplitOutYearList | 数据拆分 |
| GetFrontPage | HTTP Request |
| ExtractDetails | HTML |
| GetHeadlines | 数据设置 |
| GetDate | 数据设置 |
| MergeHeadlinesDate | 数据合并 |
| SingleJson | 数据聚合 |
| Telegram | Telegram |

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：13
- 触发节点：1
- 处理节点：10
- 输出节点：2
- 分类：workflow-automation
