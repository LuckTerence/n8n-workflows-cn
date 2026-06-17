# Perform Multi-type DNS Lookups with Google's Free Public DNS Service

https://n8nworkflows.xyz/workflows/10200

## 节点清单

| 节点 | 类型 |
|------|------|
| Split Out | 数据拆分 |
| DNS Lookup | HTTP Request |
| Set human readable type in output | Code |
| Aggregate results | Code |
| Default to all DNS types | 数据设置 |
| Use selected DNS types | 数据设置 |
| If no DNS type in input | IF 判断 |
| For each DNS type | 分批处理 |
| Form input | 表单触发器 |

## 触发方式
- Form input 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：7
- 输出节点：1
- 分类：workflow-automation
