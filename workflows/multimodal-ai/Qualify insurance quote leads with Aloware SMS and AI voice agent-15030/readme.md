# Qualify insurance quote leads with Aloware SMS and AI voice agent

https://n8nworkflows.xyz/workflows/15030

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
