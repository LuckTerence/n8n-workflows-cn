## 简介
**Automated Nicereply Feedback Routing to MS Teams by Team and Sentiment**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/10113

---

# Automated Nicereply Feedback Routing to MS Teams by Team and Sentiment


## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Trigger | 定时触发器 |
| Filter | 过滤器 |
| Send to Support | Teams |
| Split Out | 数据拆分 |
| Send to Support1 | Teams |
| Get Feedback | HTTP Request |
| Edit Feedbacks | 数据设置 |
| Without Comment | IF 判断 |
| Happiness Value | Switch 路由 |
| Switch - Type of Team | Switch 路由 |
| Switch - Type of Team1 | Switch 路由 |
| Happiness Value2 | Switch 路由 |
| Send to Team Lead | Teams |
| Send to Team Lead1 | Teams |
| Change survey ID according Nicereply | aiTransform |
| Change happiness value | aiTransform |
| Set Empty Respondent to "Unknown Client" | Code |

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：17
- 触发节点：1
- 处理节点：11
- 输出节点：5
- 分类：workflow-automation
