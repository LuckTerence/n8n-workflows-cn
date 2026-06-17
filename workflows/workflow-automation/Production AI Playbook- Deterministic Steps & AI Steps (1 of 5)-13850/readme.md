## 简介
**Production AI Playbook: Deterministic Steps & AI Steps (1 of 5)**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：6 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/13850

---

# Production AI Playbook: Deterministic Steps & AI Steps (1 of 5)


## 节点清单

| 节点 | 类型 |
|------|------|
| Respond - Validation Error | 响应 Webhook |
| Invalid Lead - Error Handler | Code |
| Valid Lead - Ready for AI | Code |
| Validate Required Fields | IF 判断 |
| Normalize Input Data | Code |
| Webhook - Receive Lead Data | Webhook |
| Respond - Success | 响应 Webhook |

## 触发方式
- Webhook - Receive Lead Data 触发

## 统计
- 节点总数：7
- 触发节点：1
- 处理节点：4
- 输出节点：2
- 分类：workflow-automation
