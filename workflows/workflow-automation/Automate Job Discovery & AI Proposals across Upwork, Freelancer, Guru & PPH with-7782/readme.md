## 简介
**Automate Job Discovery & AI Proposals across Upwork, Freelancer, Guru & PPH with OpenRouter**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Gmail)（基本改完，配置 API Key 应该就能跑）
> 节点数：16 | 难度：⭐⭐⭐ 高级
> 原始来源：https://n8nworkflows.xyz/workflows/7782

---

# Automate Job Discovery & AI Proposals across Upwork, Freelancer, Guru & PPH with OpenRouter


## 节点清单

| 节点 | 类型 |
|------|------|
| RSS Feed Trigger | rssFeedReadTrigger |
| Loop Over Items | 分批处理 |
| Extract Title & Budget | Code |
| Decode URL & Source | Code |
| Set Variables | 数据设置 |
| OpenRouter Chat Model | OpenRouter Chat Model |
| Filter | 过滤器 |
| Send a message | Email 发送 |
| Update Datatbase | Google Sheets |
| AI Proposal Agent | AI Agent |
| Append row in sheet | Google Sheets |
| Wait | 等待 |
| Aggregate | 数据聚合 |
| HTML Aggregated email | HTML |
| Limit | 数据限制 |
| Build a single HTML string | Code |

## 触发方式
- RSS Feed Trigger 触发

## 统计
- 节点总数：16
- 触发节点：1
- 处理节点：14
- 输出节点：1
- 分类：workflow-automation
