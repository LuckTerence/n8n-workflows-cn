# Auto-Retry Engine: Error Recovery Workflow

https://n8nworkflows.xyz/workflows/3144

## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Test workflow’ | 手动触发 |
| n8n | n8n |
| Log into n8n | HTTP Request |
| retry workflow automatically | HTTP Request |
| If | IF 判断 |
| No Operation, do nothing | 空操作 |
| login_details | 数据设置 |
| Loop Over Items | 分批处理 |
| Schedule Trigger | 定时触发器 |

## 触发方式
- When clicking ‘Test workflow’ 触发
- Schedule Trigger 触发

## 统计
- 节点总数：9
- 触发节点：2
- 处理节点：5
- 输出节点：2
- 分类：workflow-automation
