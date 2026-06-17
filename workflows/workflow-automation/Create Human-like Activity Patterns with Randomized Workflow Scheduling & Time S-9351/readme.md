# Create Human-like Activity Patterns with Randomized Workflow Scheduling & Time Slots

https://n8nworkflows.xyz/workflows/9351

## 节点清单

| 节点 | 类型 |
|------|------|
| Execute sub-process | 执行工作流 |
| Get Sub-workflow Name | n8n |
| Append Planning File | 读写文件 |
| Read Planning File | 读写文件 |
| ERROR: Execute Sub-worflow | 停止并报错 |
| Monitoring | Code |
| ERROR: Monitoring | 停止并报错 |
| Schedule Trigger | 定时触发器 |
| Go/no go | Switch 路由 |
| Daily Scheduler | Code |
| Init | Code |
| NOTHING Planned Email | Email 发送 |
| Write Planning File | 读写文件 |
| Send planning | Email 发送 |
| Write Log File | 读写文件 |
| Split Out | 数据拆分 |
| ERROR: Daily Scheduler | 停止并报错 |
| FINAL SUCCESS Email | Email 发送 |
| Read Final Planning File | 读写文件 |
| Loop Over Items | 分批处理 |
| LOOP SUCCESS email | Email 发送 |
| Aggregate | 数据聚合 |
| Return Monitoring Data | Code |
| Merge | 数据合并 |
| Extract from File | 从文件提取 |
| Read Log File | 读写文件 |

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：26
- 触发节点：1
- 处理节点：21
- 输出节点：4
- 分类：workflow-automation
