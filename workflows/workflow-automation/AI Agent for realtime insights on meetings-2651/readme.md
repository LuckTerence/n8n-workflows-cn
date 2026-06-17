## 简介
**AI Agent for realtime insights on meetings**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：8 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/2651

---

# AI Agent for realtime insights on meetings


## 节点清单

| 节点 | 类型 |
|------|------|
| OpenAI1 | OpenAI |
| Insert Transcription Part | PostgreSQL |
| Create Note | PostgreSQL 工具 |
| Create Recall bot | HTTP Request |
| Create OpenAI thread | HTTP Request |
| Create data record | Supabase |
| Scenario 1 Start - Edit Fields | 数据设置 |
| Scenario 2 Start - Webhook | Webhook |
| If Jimmy word | IF 判断 |

## 触发方式
- Scenario 2 Start - Webhook 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：6
- 输出节点：2
- 分类：workflow-automation
