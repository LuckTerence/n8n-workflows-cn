## 简介
**Send Matomo analytics data to A.I. to analyze then save results in Baserow**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2561

---

# Send Matomo analytics data to A.I. to analyze then save results in Baserow


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Test workflow’ | 手动触发 |
| Schedule Trigger | 定时触发器 |
| Get data from Matomo | HTTP Request |
| Parse data from Matomo | Code |
| Send data to A.I. for analysis | HTTP Request |
| Store results in Baserow | baserow |

## 触发方式
- When clicking ‘Test workflow’ 触发
- Schedule Trigger 触发

## 统计
- 节点总数：6
- 触发节点：2
- 处理节点：2
- 输出节点：2
- 分类：workflow-automation
