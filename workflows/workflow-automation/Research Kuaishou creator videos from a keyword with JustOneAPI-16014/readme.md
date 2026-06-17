## 简介
**Research Kuaishou creator videos from a keyword with JustOneAPI**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：9 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/16014

---

# Research Kuaishou creator videos from a keyword with JustOneAPI


## 节点清单

| 节点 | 类型 |
|------|------|
| Manual Trigger | 手动触发 |
| Prepare API and Research Fields | 数据设置 |
| Search Kuaishou Users by Keyword | HTTP Request |
| Output Search User Results | 数据设置 |
| Extract User IDs from Search Results | Code |
| Output Extracted User IDs | 数据设置 |
| If User ID Exists | IF 判断 |
| Fetch User Video List from Kuaishou | HTTP Request |
| Build Creator Video List Structure | Code |
| Output Final Creator Video List | 数据设置 |

## 触发方式
- Manual Trigger 触发

## 统计
- 节点总数：10
- 触发节点：1
- 处理节点：7
- 输出节点：2
- 分类：workflow-automation
