## 简介
**Validate Seatable Webhooks with HMAC SHA256 Authentication**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：5 | 难度：⭐ 入门
> 原始来源：https://n8nworkflows.xyz/workflows/3439

---

# Validate Seatable Webhooks with HMAC SHA256 Authentication


## 节点清单

| 节点 | 类型 |
|------|------|
| 200 | 响应 Webhook |
| 403 | 响应 Webhook |
| Calculate sha256 | 加密 |
| Seatable Webhook | Webhook |
| Add nodes for processing | 空操作 |
| hash matches | IF 判断 |

## 触发方式
- Seatable Webhook 触发

## 统计
- 节点总数：6
- 触发节点：1
- 处理节点：3
- 输出节点：2
- 分类：workflow-automation
