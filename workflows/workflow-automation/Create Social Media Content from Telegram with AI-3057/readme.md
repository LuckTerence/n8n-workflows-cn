## 简介
**Create Social Media Content from Telegram with AI**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3057

---

# Create Social Media Content from Telegram with AI


## 节点清单

| 节点 | 类型 |
|------|------|
| Receive Telegram Messages | Telegram 触发器 |
| Voice or Text? | Switch 路由 |
| Fetch Voice Message | Telegram |
| Transcribe Voice to Text | OpenAI |
| Prepare for LLM | 数据设置 |
| AI Agent | AI Agent |
| OpenAI Chat Model | OpenAI Chat Model |
| SerpAPI | SerpApi 工具 |
| Structured Output Parser | 结构化输出解析器 |
| Extract from File | 从文件提取 |
| Prepare Final Output | 数据设置 |
| Generate Image | HTTP Request |

## 触发方式
- Receive Telegram Messages 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：9
- 输出节点：2
- 分类：workflow-automation
