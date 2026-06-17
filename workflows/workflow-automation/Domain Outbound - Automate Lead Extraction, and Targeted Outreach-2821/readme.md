## 简介
**Domain Outbound : Automate Lead Extraction, and Targeted Outreach**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A-adapted（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2821

---

# Domain Outbound : Automate Lead Extraction, and Targeted Outreach


## 节点清单

| 节点 | 类型 |
|------|------|
| Google Sheets | Google Sheets |
| Remove Duplicates | 去重 |
| Remove Duplicates2 | 去重 |
| Split Out | 数据拆分 |
| Aggregate | 数据聚合 |
| Loop Over Items | 分批处理 |
| HTTP Request1 | HTTP Request |
| Loop Over Items1 | 分批处理 |
| Wait1 | 等待 |
| When clicking ‘Test workflow’ | 手动触发 |
| Loop Over Items4 | 分批处理 |
| get website with Jina.ai | HTTP Request |
| If1 | IF 判断 |
| Gmail1 | Email 发送 |
| Generate Email content | OpenAI |
| Wait2 | 等待 |
| Code6 | Code |
| Generate queries | OpenAI |
| fomate queries | Code |
| Loop Over queries | 分批处理 |
| Gmail search | HTTP Request |
| Extract Urls | Code |
| Filter urls | 过滤器 |
| If url is not empty | IF 判断 |
| Extract Domain Name | Code |
| Extract Emails | Code |
| Limit Markdown | Code |

## 触发方式
- When clicking ‘Test workflow’ 触发

## 统计
- 节点总数：27
- 触发节点：1
- 处理节点：22
- 输出节点：4
- 分类：workflow-automation
