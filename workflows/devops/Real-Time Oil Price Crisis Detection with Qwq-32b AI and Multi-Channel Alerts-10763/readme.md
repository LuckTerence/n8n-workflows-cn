## 简介
**Real-Time Oil Price Crisis Detection with Qwq-32b AI and Multi-Channel Alerts**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（需替换Slack/Gmail)（基本改完，配置 API Key 应该就能跑）
> 节点数：19 | 难度：⭐⭐⭐ 高级
> 原始来源：https://n8nworkflows.xyz/workflows/10763

---

# Real-Time Oil Price Crisis Detection with Qwq-32b AI and Multi-Channel Alerts


## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Every 5 Minutes | 定时触发器 |
| Workflow Configuration | 数据设置 |
| Fetch Oil Price Data (API) | HTTP Request |
| Fetch OPEC Reports | HTTP Request |
| Fetch Shipping Data | HTTP Request |
| Fetch News Feed | HTTP Request |
| Merge All Data Sources | 数据合并 |
| Data Cleaning & Preprocessing | Code |
| Statistical Anomaly Detection | Code |
| AI Trend & Geopolitical Analyzer | AI Agent |
| Calculate Crisis Risk Score | Code |
| Route by Alert Level | Switch 路由 |
| Format Info Alert | 数据设置 |
| Format Warning Alert | 数据设置 |
| Format Critical Alert | 数据设置 |
| Send Email Alert | Email 发送 |
| Send Slack Alert | Slack |
| Store Alert History | PostgreSQL |
| Send to Dashboard API | HTTP Request |
| OpenRouter Chat Model | OpenRouter Chat Model |

## 触发方式
- Schedule Every 5 Minutes 触发

## 统计
- 节点总数：20
- 触发节点：1
- 处理节点：12
- 输出节点：7
- 分类：devops
