## 简介
**Sentiment Analytics Visualizer**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5204

---

# Sentiment Analytics Visualizer


## 节点清单

| 节点 | 类型 |
|------|------|
| Loop Over Items | 分批处理 |
| Sentiment Analysis | sentimentAnalysis |
| OpenAI Chat Model | OpenAI Chat Model |
| When clicking 'Test workflow' | 手动触发 |
| Select Google Sheet | Google Sheets |
| Update Google Sheet | Google Sheets |
| Read Data from Google Sheet | Google Sheets |
| Extract Number of Answers per Sentiment | Code |
| Generate QuickChart | quickChart |
| Send Gmail with Sentiment Chart | Email 发送 |

## 触发方式
- When clicking 'Test workflow' 触发

## 统计
- 节点总数：10
- 触发节点：1
- 处理节点：8
- 输出节点：1
- 分类：workflow-automation
