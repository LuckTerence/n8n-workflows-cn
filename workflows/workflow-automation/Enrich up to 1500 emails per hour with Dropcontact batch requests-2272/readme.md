## 简介
**Enrich up to 1500 emails per hour with Dropcontact batch requests**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Slack/Gmail)（基本改完，配置 API Key 应该就能跑）
> 节点数：10 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/2272

---

# Enrich up to 1500 emails per hour with Dropcontact batch requests


## 节点清单

| 节点 | 类型 |
|------|------|
| Aggregate | 数据聚合 |
| PROFILES QUERY | PostgreSQL |
| BULK DROPCONTACT REQUESTS | HTTP Request |
| Loop Over Items2 | 分批处理 |
| Split Out | 数据拆分 |
| Postgres | PostgreSQL |
| BULK DROPCONTACT DOWNLOAD | HTTP Request |
| Wait2 | 等待 |
| DATA TRANSFORMATION | Code |
| Slack | Slack |
| Schedule Trigger | 定时触发器 |

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：11
- 触发节点：1
- 处理节点：7
- 输出节点：3
- 分类：workflow-automation
