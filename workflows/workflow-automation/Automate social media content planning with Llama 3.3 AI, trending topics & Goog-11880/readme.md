## 简介
**Automate social media content planning with Llama 3.3 AI, trending topics & Google Suite**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Gmail)（基本改完，配置 API Key 应该就能跑）
> 节点数：19 | 难度：⭐⭐⭐ 高级
> 原始来源：https://n8nworkflows.xyz/workflows/11880

---

# Automate social media content planning with Llama 3.3 AI, trending topics & Google Suite


## 节点清单

| 节点 | 类型 |
|------|------|
| Daily 8 AM Trigger1 | 定时触发器 |
| Workflow Configuration1 | 数据设置 |
| Fetch News RSS1 | RSS Feed |
| Fetch Reddit Popular1 | reddit |
| Merge Trends1 | 数据合并 |
| Format Trending Topics1 | Code |
| Read Active Campaigns1 | Google Sheets |
| Check Campaign Status1 | IF 判断 |
| Enrich with Trends1 | 数据设置 |
| Groq Chat Model1 | Groq Chat Model |
| Generate Content Ideas1 | AI Agent |
| Structured Output Parser1 | 结构化输出解析器 |
| Format for Sheets1 | 数据设置 |
| Append to Daily Content Plan1 | Google Sheets |
| Format for Calendar1 | 数据设置 |
| Create Calendar Event1 | Google Calendar |
| Calculate Performance Metrics1 | Code |
| Aggregate Daily Summary1 | 数据聚合 |
| Format Email Content1 | 数据设置 |
| Send Gmail Summary1 | Email 发送 |

## 触发方式
- Daily 8 AM Trigger1 触发
- Fetch News RSS1 触发

## 统计
- 节点总数：20
- 触发节点：2
- 处理节点：17
- 输出节点：1
- 分类：workflow-automation
