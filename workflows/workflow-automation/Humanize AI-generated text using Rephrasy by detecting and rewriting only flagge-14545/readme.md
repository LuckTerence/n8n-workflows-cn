# Humanize AI-generated text using Rephrasy by detecting and rewriting only flagged sentences

https://n8nworkflows.xyz/workflows/14545

## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Execute workflow’ | 手动触发 |
| Split Out | 数据拆分 |
| Loop Over Items | 分批处理 |
| Set text | 数据设置 |
| AI Detector | HTTP Request |
| AI Humanizer | HTTP Request |
| Get sentences | Code |
| > 50? | IF 判断 |
| Text | 数据设置 |
| Continue... | 空操作 |
| Text 2 | 数据设置 |
| Aggregate Text | 数据聚合 |

## 触发方式
- When clicking ‘Execute workflow’ 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：9
- 输出节点：2
- 分类：workflow-automation
