# Export Zammad Objects (Users, Roles, Groups, Organizations) to Excel

https://n8nworkflows.xyz/workflows/2596

## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Test workflow’ | 手动触发 |
| Zammad Univeral User Object | 数据设置 |
| Zammad Univeral Organization Object | 数据设置 |
| Zammad Univeral Role Object | 数据设置 |
| Get all Organizations | zammad |
| Get all Roles | HTTP Request |
| Convert to Excel Organizations | 转换为文件 |
| Convert to Excel Roles | 转换为文件 |
| Convert to Excel Users | 转换为文件 |
| Get all Users | zammad |
| Zammad Univeral Group Object | 数据设置 |
| Get all Groups | HTTP Request |
| If | IF 判断 |
| Basic Variables | 数据设置 |
| Convert to Excel Groups | 转换为文件 |
| Filter Groups if needed | IF 判断 |
| Filter Roles if needed | IF 判断 |
| Filter Organizations if needed | IF 判断 |

## 触发方式
- When clicking ‘Test workflow’ 触发

## 统计
- 节点总数：18
- 触发节点：1
- 处理节点：15
- 输出节点：2
- 分类：workflow-automation
