# Assign Zammad Users to Organizations Based on Email Domain

https://n8nworkflows.xyz/workflows/2588

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
