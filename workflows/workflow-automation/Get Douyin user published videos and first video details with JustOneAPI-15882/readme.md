# Get Douyin user published videos and first video details with JustOneAPI

https://n8nworkflows.xyz/workflows/15882

## 节点清单

| 节点 | 类型 |
|------|------|
| Start Workflow Execution | 手动触发 |
| Prepare API and User Data | 数据设置 |
| Fetch User Published Videos | HTTP Request |
| Output Raw Video Data | 数据设置 |
| Extract Video IDs from Data | Code |
| Output Extracted Video IDs | 数据设置 |
| Fetch First Video Details | HTTP Request |
| Build Video Details Output | Code |
| Output Final Video Data | 数据设置 |

## 触发方式
- Start Workflow Execution 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：6
- 输出节点：2
- 分类：workflow-automation
