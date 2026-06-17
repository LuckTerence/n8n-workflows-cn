## 简介
**Easy Redmine and Microsoft Teams Workflow Template**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/7293

---

# Easy Redmine and Microsoft Teams Workflow Template


## 节点清单

| 节点 | 类型 |
|------|------|
| Daily Trigger (8:30 work-days) | 定时触发器 |
| Get Issues by Query | easyRedmine |
| Split Out Issues | 数据拆分 |
| Keep Relevant Fields & Add Link | 数据设置 |
| Message into Team Channel | Teams |
| Run for Each Task | 分批处理 |

## 触发方式
- Daily Trigger (8:30 work-days) 触发

## 统计
- 节点总数：6
- 触发节点：1
- 处理节点：4
- 输出节点：1
- 分类：workflow-automation
