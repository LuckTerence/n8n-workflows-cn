## 简介
**Qualify insurance quote leads with Aloware SMS and AI voice agent**

（待补充中文描述）

> 分类：多模态 AI | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/15030

---

# Qualify insurance quote leads with Aloware SMS and AI voice agent


## 节点清单

| 节点 | 类型 |
|------|------|
| Quote Request Received | Webhook |
| Normalize Quote Data | 数据设置 |
| Aloware: Create Contact with Quote Details | HTTP Request |
| Aloware: Send Quote Acknowledgment SMS | HTTP Request |
| Is Urgent Quote? | IF 判断 |
| Aloware: Enroll in AI Voice Agent Sequence | HTTP Request |
| Aloware: Enroll in Nurture Sequence | HTTP Request |

## 触发方式
- Quote Request Received 触发

## 统计
- 节点总数：7
- 触发节点：1
- 处理节点：2
- 输出节点：4
- 分类：multimodal-ai
