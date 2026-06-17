## 简介
**Fetch Threads analytics for your latest posts and email an HTML report**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/13509

---

# Fetch Threads analytics for your latest posts and email an HTML report


## 节点清单

| 节点 | 类型 |
|------|------|
| Split Out | 数据拆分 |
| Fetch Threads Posts | HTTP Request |
| Fetch Post Insights | HTTP Request |
| Email Analytics Report | Email 发送 |
| Build HTML Report | Code |
| Merge Posts and Insights | Code |
| Get Threads Token | 数据表 |
| Set Token | 数据设置 |
| Manual Trigger | 手动触发 |
| Schedule Trigger (Every 2 Days) | 定时触发器 |

## 触发方式
- Manual Trigger 触发
- Schedule Trigger (Every 2 Days) 触发

## 统计
- 节点总数：10
- 触发节点：2
- 处理节点：5
- 输出节点：3
- 分类：workflow-automation
