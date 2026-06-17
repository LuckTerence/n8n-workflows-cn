## 简介
**Send Fireflies meeting talk-time dominance reports to Telegram**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：4 | 难度：⭐ 入门
> 原始来源：https://n8nworkflows.xyz/workflows/15097

---

# Send Fireflies meeting talk-time dominance reports to Telegram


## 节点清单

| 节点 | 类型 |
|------|------|
| 1. Webhook — Fireflies Transcript Done | Webhook |
| 2. Set — Config Values | 数据设置 |
| 3. HTTP — Fetch Speaker Analytics | HTTP Request |
| 4. Code — Analyze Speaker Data | Code |
| 5. Telegram — Send Talk-Time Report | Telegram |

## 触发方式
- 1. Webhook — Fireflies Transcript Done 触发

## 统计
- 节点总数：5
- 触发节点：1
- 处理节点：2
- 输出节点：2
- 分类：workflow-automation
