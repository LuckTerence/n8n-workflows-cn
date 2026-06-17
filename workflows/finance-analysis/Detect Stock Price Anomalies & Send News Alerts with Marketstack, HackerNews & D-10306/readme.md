## 简介
**Detect Stock Price Anomalies & Send News Alerts with Marketstack, HackerNews & DeepL**

（待补充中文描述）

> 分类：金融分析 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：11 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/10306

---

# Detect Stock Price Anomalies & Send News Alerts with Marketstack, HackerNews & DeepL


## 节点清单

| 节点 | 类型 |
|------|------|
| Daily Check | 定时触发器 |
| Get Stock Data | marketstack |
| Calculate Deviation | Code |
| Is Anomaly? (status != "normal") | IF 判断 |
| Get Related News | hackerNews |
| Translate News | deepL |
| Send Alert to Slack | Slack |
| Send Normal Report to Slack | Slack |
| Merge Original + Translated | 数据合并 |
| Add Symbol Field | 数据设置 |
| Compose Slack Message | Code |
| Build News Keyword | Code |

## 触发方式
- Daily Check 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：9
- 输出节点：2
- 分类：finance-analysis
