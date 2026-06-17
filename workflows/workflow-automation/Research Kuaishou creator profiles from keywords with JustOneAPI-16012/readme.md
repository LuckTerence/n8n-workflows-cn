## 简介
**Research Kuaishou creator profiles from keywords with JustOneAPI**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/16012

---

# Research Kuaishou creator profiles from keywords with JustOneAPI


## 节点清单

| 节点 | 类型 |
|------|------|
| Manual Execution Trigger | 手动触发 |
| Set API and Research Parameters | 数据设置 |
| Fetch Kuaishou Users by Keyword | HTTP Request |
| Output Kuaishou Search Results | 数据设置 |
| Parse User IDs from Results | Code |
| Output Parsed User IDs | 数据设置 |
| Check User ID Exists | IF 判断 |
| Fetch Kuaishou User Details | HTTP Request |
| Build User Profile Data List | Code |
| Output User Profile Data | 数据设置 |

## 触发方式
- Manual Execution Trigger 触发

## 统计
- 节点总数：10
- 触发节点：1
- 处理节点：7
- 输出节点：2
- 分类：workflow-automation
