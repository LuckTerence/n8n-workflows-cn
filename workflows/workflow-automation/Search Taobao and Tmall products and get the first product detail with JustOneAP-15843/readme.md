## 简介
**Search Taobao and Tmall products and get the first product detail with JustOneAPI**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：8 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/15843

---

# Search Taobao and Tmall products and get the first product detail with JustOneAPI


## 节点清单

| 节点 | 类型 |
|------|------|
| Start Workflow Manually | 手动触发 |
| Set API and Search Parameters | 数据设置 |
| Search Taobao/Tmall Products | HTTP Request |
| Store Search Results Data | 数据设置 |
| Extract Product IDs from Results | Code |
| Store Extracted Product IDs | 数据设置 |
| Fetch Product Details by ID | HTTP Request |
| Build Product Detail Output | Code |
| Store Final Product Details | 数据设置 |

## 触发方式
- Start Workflow Manually 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：6
- 输出节点：2
- 分类：workflow-automation
