# Send real estate lead inquiries to Aloware SMS and AI qualification sequence

https://n8nworkflows.xyz/workflows/15020

## 节点清单

| 节点 | 类型 |
|------|------|
| Property Inquiry Received | Webhook |
| Normalize Inquiry Data | 数据设置 |
| Aloware: Create Contact with Property Details | HTTP Request |
| Aloware: Send Property Inquiry SMS | HTTP Request |
| Aloware: Enroll in AI Buyer Qualification Sequence | HTTP Request |

## 触发方式
- Property Inquiry Received 触发

## 统计
- 节点总数：5
- 触发节点：1
- 处理节点：1
- 输出节点：3
- 分类：workflow-automation
