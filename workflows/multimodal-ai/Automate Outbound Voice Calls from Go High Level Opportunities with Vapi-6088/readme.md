## 简介
**Automate Outbound Voice Calls from Go High Level Opportunities with Vapi**

（待补充中文描述）

> 分类：多模态 AI | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/6088

---

# Automate Outbound Voice Calls from Go High Level Opportunities with Vapi


## 节点清单

| 节点 | 类型 |
|------|------|
| Start outbound Vapi call | HTTP Request |
| Set fields | 数据设置 |
| GHL opportunity created | Webhook |
| Get a GHL contact | highLevel |
| Wait 5min | 等待 |

## 触发方式
- GHL opportunity created 触发

## 统计
- 节点总数：5
- 触发节点：1
- 处理节点：3
- 输出节点：1
- 分类：multimodal-ai
