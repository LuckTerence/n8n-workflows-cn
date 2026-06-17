## 简介
**Automated Property Lead Generation with BatchData and CRM Integration**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：10 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/3665

---

# Automated Property Lead Generation with BatchData and CRM Integration


## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Market Scan | 定时触发器 |
| BatchData API Configuration | 数据设置 |
| Query BatchData Properties | HTTP Request |
| Get Previous Results | Code |
| Compare Results | Code |
| Split Properties | 数据拆分 |
| Filter High Potential | 过滤器 |
| Get Property Details | HTTP Request |
| Format Email Content | 数据设置 |
| Send Email Alert | Email 发送 |
| Post to Slack | Slack |

## 触发方式
- Schedule Market Scan 触发

## 统计
- 节点总数：11
- 触发节点：1
- 处理节点：6
- 输出节点：4
- 分类：workflow-automation
