## 简介
**Evaluation metric example: Check if tool was called**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A-adapted（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4268

---

# Evaluation metric example: Check if tool was called


## 节点清单

| 节点 | 类型 |
|------|------|
| AI Agent | AI Agent |
| OpenAI Chat Model | OpenAI Chat Model |
| Calculator | 计算器工具 |
| Check if tool called | 数据设置 |
| Fetch a webpage | HTTP Request 工具 |
| When chat message received | Chat 触发器 |
| Match chat format | 数据设置 |
| Return chat response | 空操作 |
| When fetching a dataset row | evaluationTrigger |
| Evaluation | 条件评估 |
| Evaluating? | 条件评估 |

## 触发方式
- When chat message received 触发
- When fetching a dataset row 触发

## 统计
- 节点总数：11
- 触发节点：2
- 处理节点：8
- 输出节点：1
- 分类：workflow-automation
