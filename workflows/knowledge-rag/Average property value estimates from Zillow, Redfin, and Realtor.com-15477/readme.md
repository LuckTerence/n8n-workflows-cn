## 简介
**Average property value estimates from Zillow, Redfin, and Realtor.com**

（待补充中文描述）

> 分类：知识库 RAG | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：9 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/15477

---

# Average property value estimates from Zillow, Redfin, and Realtor.com


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
