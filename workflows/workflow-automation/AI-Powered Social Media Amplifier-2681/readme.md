## 简介
**AI-Powered Social Media Amplifier**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：18 | 难度：⭐⭐⭐ 高级
> 原始来源：https://n8nworkflows.xyz/workflows/2681

---

# AI-Powered Social Media Amplifier


## 节点清单

| 节点 | 类型 |
|------|------|
| Crawl HN Home | HTTP Request |
| Extract Meta | Code |
| Filter Unposted Items | Code |
| Visit GH Page | HTTP Request |
| Convert HTML To Markdown | Markdown |
| Filter Errored | 过滤器 |
| No Operation, do nothing | 空操作 |
| Update X Status | Airtable |
| LinkedIn | linkedIn |
| Update L Status | Airtable |
| Search Item | Airtable |
| Create Item | Airtable |
| X | Twitter |
| Validate Generate Content | Code |
| Schedule Trigger | 定时触发器 |
| Merge | 数据合并 |
| Generate Content | OpenAI |
| Ping Me | Telegram |
| Wait for 5 mins before posting | 等待 |

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：19
- 触发节点：1
- 处理节点：15
- 输出节点：3
- 分类：workflow-automation
