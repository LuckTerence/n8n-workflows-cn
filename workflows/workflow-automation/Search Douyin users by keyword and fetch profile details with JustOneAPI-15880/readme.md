# Search Douyin users by keyword and fetch profile details with JustOneAPI

https://n8nworkflows.xyz/workflows/15880

## 节点清单

| 节点 | 类型 |
|------|------|
| Start Workflow | 手动触发 |
| Set API and Search Parameters | 数据设置 |
| Search Douyin Users by Keyword | HTTP Request |
| Output Search Results | 数据设置 |
| Extract SecUIDs from Results | Code |
| Output Extracted SecUIDs | 数据设置 |
| Fetch User Details from Douyin | HTTP Request |
| Build User Profile Data | Code |
| Output Final User Profiles | 数据设置 |

## 触发方式
- Start Workflow 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：6
- 输出节点：2
- 分类：workflow-automation
