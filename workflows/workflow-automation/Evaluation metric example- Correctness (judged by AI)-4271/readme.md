## 简介
**Evaluation metric example: Correctness (judged by AI)**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 节点数：8 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/4271

---

# Evaluation metric example: Correctness (judged by AI)


## 节点清单

| 节点 | 类型 |
|------|------|
| OpenAI Chat Model | OpenAI Chat Model |
| When fetching a dataset row | evaluationTrigger |
| Evaluating? | 条件评估 |
| AI Agent | AI Agent |
| Calculate correctness metric | OpenAI |
| When chat message received | Chat 触发器 |
| Match chat format | 数据设置 |
| Return chat response | 空操作 |
| Set metrics | 条件评估 |

## 触发方式
- When fetching a dataset row 触发
- When chat message received 触发

## 统计
- 节点总数：9
- 触发节点：2
- 处理节点：7
- 输出节点：0
- 分类：workflow-automation
