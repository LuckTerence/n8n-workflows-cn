## 简介
**BambooHR AI-Powered Company Policies and Benefits Chatbot**

（待补充中文描述）

> 分类：AI Agent | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：37 | 难度：⭐⭐⭐ 高级
> 原始来源：https://n8nworkflows.xyz/workflows/2850

---

# BambooHR AI-Powered Company Policies and Benefits Chatbot


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Test workflow’ | 手动触发 |
| Default Data Loader | 文档加载器 |
| Embeddings OpenAI | OpenAI Embeddings |
| Recursive Character Text Splitter | 文本分割器 |
| Window Buffer Memory | 记忆缓冲区 |
| OpenAI Chat Model | OpenAI Chat Model |
| Vector Store Tool | 向量存储工具 |
| OpenAI Chat Model1 | OpenAI Chat Model |
| Embeddings OpenAI1 | OpenAI Embeddings |
| Employee Lookup Tool | 工作流工具 |
| OpenAI Chat Model2 | OpenAI Chat Model |
| OpenAI Chat Model3 | OpenAI Chat Model |
| OpenAI Chat Model4 | OpenAI Chat Model |
| Auto-fixing Output Parser | 自动修复输出解析器 |
| OpenAI Chat Model5 | OpenAI Chat Model |
| Structured Output Parser | 结构化输出解析器 |
| GET all files | bambooHr |
| Filter out files from undesired categories | 过滤器 |
| Split out individual files | 数据拆分 |
| Filter out non-pdf files | 过滤器 |
| Download file from BambooHR | bambooHr |
| Supabase Vector Store | Supabase 向量存储 |
| Employee initiates a conversation | Chat 触发器 |
| Supabase Vector Store Retrieval | Supabase 向量存储 |
| AI-Powered HR Benefits and Company Policies Chatbot | 执行工作流触发器 |
| Text Classifier | 文本分类器 |
| GET all employees | bambooHr |
| Filter out other employees | 过滤器 |
| Stringify employee record for response | 数据设置 |
| GET all employees (second path) | bambooHr |
| Extract departments | 数据聚合 |
| Ensure uniqueness in department list | 数据设置 |
| Extract department | 信息提取器 |
| Retrieve all employees | bambooHr |
| Filter out other departments | 过滤器 |
| Extract relevant employee fields | 数据聚合 |
| Identify most senior employee | LLM Chain |
| Format name for response | 数据设置 |
| HR AI Agent | AI Agent |

## 触发方式
- When clicking ‘Test workflow’ 触发
- Employee initiates a conversation 触发
- AI-Powered HR Benefits and Company Policies Chatbot 触发

## 统计
- 节点总数：39
- 触发节点：3
- 处理节点：36
- 输出节点：0
- 分类：ai-agent
