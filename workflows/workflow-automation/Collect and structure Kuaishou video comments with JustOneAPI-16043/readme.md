## 简介
**Collect and structure Kuaishou video comments with JustOneAPI**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/16043

---

# Collect and structure Kuaishou video comments with JustOneAPI


## 节点清单

| 节点 | 类型 |
|------|------|
| Start Workflow Execution | 手动触发 |
| Set API Request Parameters | 数据设置 |
| Fetch Kuaishou Video Comments API | HTTP Request |
| Output Raw Comment Data | 数据设置 |
| Process Comment Data Collection | Code |
| Output Final Comment Collection | 数据设置 |

## 触发方式
- Start Workflow Execution 触发

## 统计
- 节点总数：6
- 触发节点：1
- 处理节点：4
- 输出节点：1
- 分类：workflow-automation
