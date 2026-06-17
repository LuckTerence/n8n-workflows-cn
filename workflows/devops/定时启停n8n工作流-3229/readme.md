# 定时启停n8n工作流

https://n8nworkflows.xyz/workflows/3229

## 节点清单

| 节点 | 类型 |
|------|------|
| n8n Activate | n8n |
| n8n Deactivate | n8n |
| Workflow ID | 数据设置 |
| Merge in Workflow ID for deactivation | 数据合并 |
| Merge in Workflow ID for activation | 数据合并 |
| Activate at 08:00 daily | 定时触发器 |
| Deactivate at 20:00 daily | 定时触发器 |

## 触发方式
- Activate at 08:00 daily 触发
- Deactivate at 20:00 daily 触发

## 统计
- 节点总数：7
- 触发节点：2
- 处理节点：5
- 输出节点：0
- 分类：devops
