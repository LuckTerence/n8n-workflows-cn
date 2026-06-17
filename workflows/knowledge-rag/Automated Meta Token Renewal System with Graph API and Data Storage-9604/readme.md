# Automated Meta Token Renewal System with Graph API and Data Storage

https://n8nworkflows.xyz/workflows/9604

## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Trigger | 定时触发器 |
| No Operation, do nothing | 空操作 |
| Get token expiration date | 数据表 |
| Needs renewal? | IF 判断 |
| Carry ID & Token | 数据设置 |
| User Exchange | HTTP Request |
| Compute new expiry | 数据设置 |
| Update Record | 数据表 |
| When clicking "Execute workflow" | 手动触发 |

## 触发方式
- Schedule Trigger 触发
- When clicking "Execute workflow" 触发

## 统计
- 节点总数：9
- 触发节点：2
- 处理节点：6
- 输出节点：1
- 分类：knowledge-rag
