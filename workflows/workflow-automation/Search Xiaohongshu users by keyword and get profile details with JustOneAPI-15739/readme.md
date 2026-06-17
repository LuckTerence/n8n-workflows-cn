## 简介
**Search Xiaohongshu users by keyword and get profile details with JustOneAPI**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：8 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/15739

---

# Search Xiaohongshu users by keyword and get profile details with JustOneAPI


## 节点清单

| 节点 | 类型 |
|------|------|
| Start Workflow | 手动触发 |
| Set API and Search Parameters | 数据设置 |
| Search Xiaohongshu Users by Keyword | HTTP Request |
| Output Search Results | 数据设置 |
| Extract User IDs from Search Results | Code |
| Output Extracted User IDs List | 数据设置 |
| Get Xiaohongshu User Profiles | HTTP Request |
| Build Combined User Profiles | Code |
| Output Final User Profile Data | 数据设置 |

## 触发方式
- Start Workflow 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：6
- 输出节点：2
- 分类：workflow-automation
