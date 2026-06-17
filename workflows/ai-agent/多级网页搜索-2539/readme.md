## 简介
**多级网页搜索**

多阶段AI搜索和研究套件

> 分类：AI Agent | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：28 | 难度：⭐⭐⭐ 高级
> 原始来源：https://n8nworkflows.xyz/workflows/2539

---

# 多级网页搜索


## 节点清单

| 节点 | 类型 |
|------|------|
| Google Gemini Chat Model14 | Google Gemini |
| Google Gemini Chat Model | Google Gemini |
| Google Gemini Chat Model15 | Google Gemini |
| Auto-fixing Output Parser6 | 自动修复输出解析器 |
| Structured Output Parser3 | 结构化输出解析器 |
| Query 2 | HTTP Request |
| Query  1 | HTTP Request |
| Respond to Webhook | 响应 Webhook |
| Date & Time | 日期时间 |
| Auto-fixing Output Parser | 自动修复输出解析器 |
| Structured Output Parser1 | 结构化输出解析器 |
| Auto-fixing Output Parser7 | 自动修复输出解析器 |
| Structured Output Parser4 | 结构化输出解析器 |
| Query Maker - 1 | LLM Chain |
| Google Gemini Chat Model16 | Google Gemini |
| Article Extractor1 | HTTP Request |
| Analyst Emulator | LLM Chain |
| Webhook | Webhook |
| Query 1 Ranker & Query 2 Maker | LLM Chain |
| Date & Time1 | 日期时间 |
| Query-1 Combined | Code |
| Query-2 Combined | Code |
| Query 2 - Ranker | LLM Chain |
| Code | Code |
| Loop Over Items | 分批处理 |
| Delay-to-Avoid-Request-Per-Minute-Cap | 等待 |
| Research Reporter | LLM Chain |
| Code1 | Code |
| Webhook Call | HTTP Request |

## 触发方式
- Webhook 触发

## 统计
- 节点总数：29
- 触发节点：1
- 处理节点：23
- 输出节点：5
- 分类：ai-agent
