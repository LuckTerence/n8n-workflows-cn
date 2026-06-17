## 简介
**IP Reputation Check & SOC Alerts with Splunk, VirusTotal and AlienVault**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（需替换Slack/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/6037

---

# IP Reputation Check & SOC Alerts with Splunk, VirusTotal and AlienVault


## 节点清单

| 节点 | 类型 |
|------|------|
| VirusTotal IP reputation check | HTTP Request |
| IP summary display | HTML |
| Extract IOCs | Code |
| AlienVault Lookup | HTTP Request |
| Merge Threat Data | 数据合并 |
| Process Intel Data | Code |
| Generate IP Summary | Code |
| Filter Suspicious IPs | Switch 路由 |
| Create IP Incident | serviceNow |
| Slack IP Alert | Slack |
| Gmail | Email 发送 |
| Splunk Alert | Webhook |

## 触发方式
- Splunk Alert 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：7
- 输出节点：4
- 分类：devops
