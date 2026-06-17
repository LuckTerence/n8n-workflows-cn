# Optimize inactive Microsoft 365 premium licenses with Graph and Teams

https://n8nworkflows.xyz/workflows/16110

## 节点清单

| 节点 | 类型 |
|------|------|
| Monthly Schedule Trigger at 6am | 定时触发器 |
| Set Configuration Parameters | 数据设置 |
| Validate Configuration | Code |
| Fetch Subscribed SKUs | HTTP Request |
| Generate Premium SKU Map | Code |
| Retrieve Exemption Group Members | HTTP Request |
| Compile Exemption List | 列表操作 |
| Fetch All Licensed Users | Code |
| Filter Inactive Premium Members | Code |
| Check Downgradable Users | IF 判断 |
| Notify No Downgrades Required | Teams |
| Complete No Action Needed | 空操作 |
| Divide Downgrade Plan | Code |
| Batch Process Downgrades | 分批处理 |
| Wait 0.5 Seconds | 等待 |
| Check Dry Run Mode | IF 判断 |
| Pass on Dry Run Mode | Code |
| Perform License Downgrade | HTTP Request |
| Verify Downgrade Success | IF 判断 |
| Log Downgrade Success | Code |
| Alert License Error | Teams |
| Prepare Next Downgrade | 空操作 |
| Gather Downgrade Results | 列表操作 |
| Create Summary Report | Code |
| Deliver Summary to IT Manager | Teams |
| Finalize Workflow | 空操作 |

## 触发方式
- Monthly Schedule Trigger at 6am 触发

## 统计
- 节点总数：26
- 触发节点：1
- 处理节点：19
- 输出节点：6
- 分类：workflow-automation
