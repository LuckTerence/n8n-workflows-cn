## 简介
**Simple Bluesky multi-image post using native Bluesky API**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：10 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/2562

---

# Simple Bluesky multi-image post using native Bluesky API


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Test workflow’ | 手动触发 |
| Create Bluesky Session | HTTP Request |
| Download Images | HTTP Request |
| Code | Code |
| Split Out | 数据拆分 |
| Post to Bluesky | HTTP Request |
| Define Credentials | 数据设置 |
| Aggregate | 数据聚合 |
| Set Images | 数据设置 |
| Post Image to Bluesky | HTTP Request |
| Set Caption | 数据设置 |

## 触发方式
- When clicking ‘Test workflow’ 触发

## 统计
- 节点总数：11
- 触发节点：1
- 处理节点：6
- 输出节点：4
- 分类：workflow-automation
