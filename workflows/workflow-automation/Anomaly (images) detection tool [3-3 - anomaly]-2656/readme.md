## 简介
**Anomaly (images) detection tool [3-3 - anomaly]**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2656

---

# Anomaly (images) detection tool [3-3 - anomaly]


## 节点清单

| 节点 | 类型 |
|------|------|
| Embed image | HTTP Request |
| Get similarity of medoids | HTTP Request |
| Compare scores | Code |
| Variables for medoids | 数据设置 |
| Info About Crop Labeled Clusters | 数据设置 |
| Total Points in Collection | HTTP Request |
| Each Crop Counts | HTTP Request |
| Image URL hardcode | 数据设置 |
| Execute Workflow Trigger | 执行工作流触发器 |

## 触发方式
- Execute Workflow Trigger 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：4
- 输出节点：4
- 分类：workflow-automation
