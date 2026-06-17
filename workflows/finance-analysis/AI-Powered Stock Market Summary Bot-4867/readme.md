## 简介
**AI-Powered Stock Market Summary Bot**

（待补充中文描述）

> 分类：金融分析 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：9 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/4867

---

# AI-Powered Stock Market Summary Bot


## 节点清单

| 节点 | 类型 |
|------|------|
| Ticker List | 数据设置 |
| Fetch Stock Data | HTTP Request |
| Interpret Data | Code |
| Stock Analysis Assistant | OpenAI |
| Send Summary to User(s) | Slack |
| Schedule Trigger | 定时触发器 |
| Check if Market is open | IF 判断 |
| Market is Closed | 空操作 |
| Check Market Status | HTTP Request |
| End of Flow | 空操作 |

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：10
- 触发节点：1
- 处理节点：6
- 输出节点：3
- 分类：finance-analysis
