## 简介
**Auto-Generate and Post Social Media Content to Bluesky using Groq LLM**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3455

---

# Auto-Generate and Post Social Media Content to Bluesky using Groq LLM


## 节点清单

| 节点 | 类型 |
|------|------|
| Create Bluesky Session | HTTP Request |
| Post to Bluesky | HTTP Request |
| Define Credentials | 数据设置 |
| Schedule Trigger | 定时触发器 |
| Groq Chat Model | Groq Chat Model |
| HTTP error | HTTP Request |
| Wait | 等待 |
| Stop and Error | 停止并报错 |
| LLM Chain | LLM Chain |
| Execution Count Code | Code |
| Execution Count Check | IF 判断 |
| Check if JSON is Valid | IF 判断 |
| Code code to cap posts at 300 characters | Code |
| Execution Count Code 2 | Code |
| Execution Count Check 2 | IF 判断 |

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：15
- 触发节点：1
- 处理节点：11
- 输出节点：3
- 分类：workflow-automation
