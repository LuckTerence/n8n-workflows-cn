## 简介
**Protect public webhooks with Ainoflow Guard rate limiting**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：8 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/13491

---

# Protect public webhooks with Ainoflow Guard rate limiting


## 节点清单

| 节点 | 类型 |
|------|------|
| Webhook | Webhook |
| Config | 数据设置 |
| BuildIdentity | Code |
| GuardCheck | HTTP Request |
| IfAllowed | IF 判断 |
| BusinessLogic | Code |
| RespondOk | 响应 Webhook |
| BuildDeniedResponse | 数据设置 |
| RespondRateLimited | 响应 Webhook |

## 触发方式
- Webhook 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：5
- 输出节点：3
- 分类：devops
