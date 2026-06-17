## 简介
**Stock Fundamental Analysis & AI-Powered Reports with Mistral and AlphaVantage**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：B（需替换Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5710

---

# Stock Fundamental Analysis & AI-Powered Reports with Mistral and AlphaVantage


## 节点清单

| 节点 | 类型 |
|------|------|
| Set Variables | 数据设置 |
| Get News Data | HTTP Request |
| Get News Data1 | HTTP Request |
| Get News Data2 | HTTP Request |
| Get News Data3 | HTTP Request |
| Get News Data4 | HTTP Request |
| Merge | 数据合并 |
| Get News Data5 | HTTP Request |
| Auto-fixing Output Parser | 自动修复输出解析器 |
| Mistral Cloud Chat Model | Mistral Chat Model |
| Structured Output Parser1 | 结构化输出解析器 |
| Mistral Cloud Chat Model1 | Mistral Chat Model |
| Code1 | Code |
| Split Out | 数据拆分 |
| Split Out2 | 数据拆分 |
| Merge1 | 数据合并 |
| Limit | 数据限制 |
| Code2 | Code |
| Merge2 | 数据合并 |
| Aggregate | 数据聚合 |
| Gmail | Email 发送 |
| Basic LLM Chain | LLM Chain |
| HTML | HTML |
| Basic LLM Chain1 | LLM Chain |
| Mistral Cloud Chat Model2 | Mistral Chat Model |
| HTML2 | HTML |
| Structured Output Parser | 结构化输出解析器 |
| On form submission | 表单触发器 |

## 触发方式
- On form submission 触发

## 统计
- 节点总数：28
- 触发节点：1
- 处理节点：20
- 输出节点：7
- 分类：workflow-automation
