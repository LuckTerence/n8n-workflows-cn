## 简介
**Search Douyin videos by keyword and get the first video detail with JustOneAPI**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：8 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/15878

---

# Search Douyin videos by keyword and get the first video detail with JustOneAPI


## 节点清单

| 节点 | 类型 |
|------|------|
| Start Workflow Manually | 手动触发 |
| Set API and Search Parameters | 数据设置 |
| Fetch Douyin Video Search Results | HTTP Request |
| Store Raw Search Results | 数据设置 |
| Extract Video IDs from Search | Code |
| Store Extracted Video IDs | 数据设置 |
| Fetch First Video Details | HTTP Request |
| Build Clean Video Detail | Code |
| Store Final Video Details | 数据设置 |

## 触发方式
- Start Workflow Manually 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：6
- 输出节点：2
- 分类：workflow-automation
