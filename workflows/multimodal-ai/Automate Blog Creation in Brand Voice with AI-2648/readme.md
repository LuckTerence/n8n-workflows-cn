# Automate Blog Creation in Brand Voice with AI

https://n8nworkflows.xyz/workflows/2648

## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Test workflow’ | 手动触发 |
| OpenAI Chat Model | OpenAI Chat Model |
| OpenAI Chat Model1 | OpenAI Chat Model |
| OpenAI Chat Model2 | OpenAI Chat Model |
| Extract Voice Characteristics | 信息提取器 |
| Get Blog | HTTP Request |
| Get Article | HTTP Request |
| Extract Article URLs | HTML |
| Split Out URLs | 数据拆分 |
| Latest Articles | 数据限制 |
| Extract Article Content | HTML |
| Combine Articles | 数据聚合 |
| Article Style & Brand Voice | 数据合并 |
| Save as Draft | wordpress |
| Capture Existing Article Structure | LLM Chain |
| Markdown | Markdown |
| Content Generation Agent | 信息提取器 |
| New Article Instruction | 数据设置 |

## 触发方式
- When clicking ‘Test workflow’ 触发

## 统计
- 节点总数：18
- 触发节点：1
- 处理节点：15
- 输出节点：2
- 分类：multimodal-ai
