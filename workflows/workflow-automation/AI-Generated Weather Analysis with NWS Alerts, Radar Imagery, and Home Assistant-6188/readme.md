## 简介
**AI-Generated Weather Analysis with NWS Alerts, Radar Imagery, and Home Assistant**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A-adapted（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/6188

---

# AI-Generated Weather Analysis with NWS Alerts, Radar Imagery, and Home Assistant


## 节点清单

| 节点 | 类型 |
|------|------|
| Webhook | Webhook |
| Get NWS Alerts | HTTP Request |
| Split Out | 数据拆分 |
| Remove Irrelevant Fields | 数据设置 |
| Filter by Severity | 过滤器 |
| Filter by Effective | 过滤器 |
| Filter by Status | 过滤器 |
| Fetch Weather.gov Radar Loop | HTTP Request |
| Filter by Expired | 过滤器 |
| Analyze Radar Image | OpenAI |
| Map JSON Response | 数据设置 |
| Get Local Weather Precipication | homeAssistant |
| Merge JSON with Image | 数据合并 |
| Merge Radar Analysis with NWS Data | 数据合并 |
| OpenAI Chat Model | OpenAI Chat Model |
| Code | Code |
| Aggregate | 数据聚合 |
| Generate a Summary | chainSummarization |
| Map JSON to Response | 数据设置 |

## 触发方式
- Webhook 触发

## 统计
- 节点总数：19
- 触发节点：1
- 处理节点：16
- 输出节点：2
- 分类：workflow-automation
