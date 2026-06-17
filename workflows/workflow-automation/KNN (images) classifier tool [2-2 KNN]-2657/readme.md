## 简介
**KNN (images) classifier tool [2-2 KNN]**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2657

---

# KNN (images) classifier tool [2-2 KNN]


## 节点清单

| 节点 | 类型 |
|------|------|
| Embed image | HTTP Request |
| Query Qdrant | HTTP Request |
| Majority Vote | Code |
| Increase limitKNN | 数据设置 |
| Propagate loop variables | 数据设置 |
| Image Test URL | 数据设置 |
| Return class | 数据设置 |
| Check tie | IF 判断 |
| Qdrant variables + embedding + KNN neigbours | 数据设置 |
| Execute Workflow Trigger | 执行工作流触发器 |

## 触发方式
- Execute Workflow Trigger 触发

## 统计
- 节点总数：10
- 触发节点：1
- 处理节点：7
- 输出节点：2
- 分类：workflow-automation
