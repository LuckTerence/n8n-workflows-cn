# Average property value estimates from Zillow, Redfin, and Realtor.com

https://n8nworkflows.xyz/workflows/15477

## 节点清单

| 节点 | 类型 |
|------|------|
| When Execute Workflow | 手动触发 |
| Fetch Zillow Zestimate | HTTP Request |
| Fetch Redfin Property Data | HTTP Request |
| Fetch Realtor Property Data | HTTP Request |
| Set Property Address | 数据设置 |
| Fetch Redfin Estimate | HTTP Request |
| Merge Property Estimates | 数据合并 |
| Set Estimated Values | 数据设置 |
| Calculate Average Estimate | Code |
| Fetch Detailed Realtor Info | HTTP Request |

## 触发方式
- When Execute Workflow 触发

## 统计
- 节点总数：10
- 触发节点：1
- 处理节点：4
- 输出节点：5
- 分类：knowledge-rag
