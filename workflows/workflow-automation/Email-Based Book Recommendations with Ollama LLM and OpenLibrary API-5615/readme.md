## 简介
**Email-Based Book Recommendations with Ollama LLM and OpenLibrary API**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5615

---

# Email-Based Book Recommendations with Ollama LLM and OpenLibrary API


## 节点清单

| 节点 | 类型 |
|------|------|
| Ollama Model | Ollama Chat Model |
| Email Trigger – Book Request | Email 读取 |
| Analyze Email with Ollama | AI Agent |
| Create Book Search Query | 数据设置 |
| Call Book Search API | HTTP Request |
| Check API Response | IF 判断 |
| Handle No Book Found | Email 发送 |
| Check Book Name | Code |
| Extract Book Summary | HTTP Request |
| Wait for Summary Response | 等待 |
| Retrieve Book Details | HTTP Request |
| Format Book Data | 数据设置 |
| Enhance Data with Code | Code |
| Generate Email Content | 数据设置 |
| Send Recommendation Email | Email 发送 |

## 触发方式
- 手动触发

## 统计
- 节点总数：15
- 触发节点：0
- 处理节点：9
- 输出节点：6
- 分类：workflow-automation
