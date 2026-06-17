## 简介
**Daily Financial News Summary with Ollama LLM - Automated Email Report**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Gmail)（基本改完，配置 API Key 应该就能跑）
> 节点数：7 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/5405

---

# Daily Financial News Summary with Ollama LLM - Automated Email Report


## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Daily Trigger	 | 定时触发器 |
| Fetch Financial News Webpage	 | HTTP Request |
| Delay to Ensure Page Load	 | 等待 |
| Extract News Headlines & Text	 | HTML |
| Clean Extracted News Data	 | 数据设置 |
| AI Financial News Summarizer	 | AI Agent |
| Email Daily Financial Summary	 | Email 发送 |
| LLM Chat Model | Ollama Chat Model |

## 触发方式
- Schedule Daily Trigger	 触发

## 统计
- 节点总数：8
- 触发节点：1
- 处理节点：5
- 输出节点：2
- 分类：workflow-automation
