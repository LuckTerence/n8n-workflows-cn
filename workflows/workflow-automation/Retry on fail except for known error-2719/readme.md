# Retry on fail except for known error

https://n8nworkflows.xyz/workflows/2719

## 节点清单

| 节点 | 类型 |
|------|------|
| Retry limit reached | 停止并报错 |
| Set tries | 数据设置 |
| Update tries | 数据设置 |
| Wait | 等待 |
| Catch known error | IF 判断 |
| Replace Me | 空操作 |
| Success | 空操作 |
| Known Error | 空操作 |
| Manual Trigger | 手动触发 |
| If tries left | IF 判断 |

## 触发方式
- Manual Trigger 触发

## 统计
- 节点总数：10
- 触发节点：1
- 处理节点：9
- 输出节点：0
- 分类：workflow-automation
