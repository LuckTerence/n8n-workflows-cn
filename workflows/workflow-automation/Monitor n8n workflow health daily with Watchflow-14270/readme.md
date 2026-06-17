## 简介
**Monitor n8n workflow health daily with Watchflow**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/14270

---

# Monitor n8n workflow health daily with Watchflow


## 节点清单

| 节点 | 类型 |
|------|------|
| Get All Workflows | n8n |
| Get Last Execution | n8n |
| Is Successful? | IF 判断 |
| Watchflow: Ping | watchflow |
| Watchflow: Fail | watchflow |
| Every Day | 定时触发器 |

## 触发方式
- Every Day 触发

## 统计
- 节点总数：6
- 触发节点：1
- 处理节点：5
- 输出节点：0
- 分类：workflow-automation
