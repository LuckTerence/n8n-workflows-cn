## 简介
**Retrieve and Filter Kagi News by Category**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/9318

---

# Retrieve and Filter Kagi News by Category


## 节点清单

| 节点 | 类型 |
|------|------|
| Start | 执行工作流触发器 |
| Get Latest Categories | HTTP Request |
| Split Categories | 数据拆分 |
| Filter by wanted category | 过滤器 |
| Get Stories in Category | HTTP Request |
| Split out stories | 数据拆分 |
| Pick only title | 数据设置 |
| Limit to 1 category | 数据限制 |

## 触发方式
- Start 触发

## 统计
- 节点总数：8
- 触发节点：1
- 处理节点：5
- 输出节点：2
- 分类：workflow-automation
