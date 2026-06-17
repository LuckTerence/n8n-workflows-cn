## 简介
**KlickTipp tag manager: convert tag names to IDs**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：10 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/11923

---

# KlickTipp tag manager: convert tag names to IDs


## 节点清单

| 节点 | 类型 |
|------|------|
| Find tags to create | 数据合并 |
| Find existing tags | 数据合并 |
| Combine existing & new tags | 数据合并 |
| Split tagNames into items | 数据拆分 |
| Map tagNames -> value | 数据设置 |
| Get tag list | Klicktipp |
| Create new tag | Klicktipp |
| Aggregate tag IDs  | 数据聚合 |
| Extract only tag IDs | 数据设置 |
| Input: Tag names | 执行工作流触发器 |

## 触发方式
- Input: Tag names 触发

## 统计
- 节点总数：10
- 触发节点：1
- 处理节点：9
- 输出节点：0
- 分类：workflow-automation
