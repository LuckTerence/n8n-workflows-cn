## 简介
**Assign Zammad Users to Organizations Based on Email Domain**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：7 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/2588

---

# Assign Zammad Users to Organizations Based on Email Domain


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Test workflow’ | 手动触发 |
| Organization has domain and is shared | IF 判断 |
| User has email and no organization | IF 判断 |
| Extract Domain from User E-Mail | 数据设置 |
| Zammad | zammad |
| Zammad1 | zammad |
| Merge | 数据合并 |
| Update User | zammad |

## 触发方式
- When clicking ‘Test workflow’ 触发

## 统计
- 节点总数：8
- 触发节点：1
- 处理节点：7
- 输出节点：0
- 分类：workflow-automation
