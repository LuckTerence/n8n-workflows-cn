## 简介
**Auto n8n Updater (Docker)**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5198

---

# Auto n8n Updater (Docker)


## 节点清单

| 节点 | 类型 |
|------|------|
| Docker Path | 数据设置 |
| Update Docker | SSH |
| Get n8n Current Version | SSH |
| Get Instance's Settings | HTTP Request |
| Is Docker | IF 判断 |
| Get Version's Last Update | HTTP Request |
| Target Version | 数据设置 |
| Get Current Version | HTTP Request |
| Needs Update ? | IF 判断 |
| Google Gemini Chat Model | OpenAI Chat Model |
| Approved ? | IF 判断 |
| Every Hour | 定时触发器 |
| Published In Last Hours ? | IF 判断 |
| Release Overview | LLM Chain |
| Approve Update | Telegram |
| Get n8n Github Release | HTTP Request |

## 触发方式
- Every Hour 触发

## 统计
- 节点总数：16
- 触发节点：1
- 处理节点：10
- 输出节点：5
- 分类：devops
