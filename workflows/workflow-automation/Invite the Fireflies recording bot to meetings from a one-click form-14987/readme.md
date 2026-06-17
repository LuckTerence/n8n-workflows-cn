## 简介
**Invite the Fireflies recording bot to meetings from a one-click form**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：5 | 难度：⭐ 入门
> 原始来源：https://n8nworkflows.xyz/workflows/14987

---

# Invite the Fireflies recording bot to meetings from a one-click form


## 节点清单

| 节点 | 类型 |
|------|------|
| 5. Set — Build Success Response | 数据设置 |
| 6. Respond — Bot Invited Successfully | 响应 Webhook |
| 1. Form — Invite Fireflies Bot | 表单触发器 |
| 2. Set — Validate and Prepare Inputs | 数据设置 |
| 3. IF — Valid Meeting Link? | IF 判断 |
| 4. HTTP — Send to Fireflies API | HTTP Request |

## 触发方式
- 1. Form — Invite Fireflies Bot 触发

## 统计
- 节点总数：6
- 触发节点：1
- 处理节点：3
- 输出节点：2
- 分类：workflow-automation
