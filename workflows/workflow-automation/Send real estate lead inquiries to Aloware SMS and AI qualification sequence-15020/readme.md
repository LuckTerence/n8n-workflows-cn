## 简介
**Send real estate lead inquiries to Aloware SMS and AI qualification sequence**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：4 | 难度：⭐ 入门
> 原始来源：https://n8nworkflows.xyz/workflows/15020

---

# Send real estate lead inquiries to Aloware SMS and AI qualification sequence


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
