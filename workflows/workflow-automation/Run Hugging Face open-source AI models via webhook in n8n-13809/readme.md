# Run Hugging Face open-source AI models via webhook in n8n

https://n8nworkflows.xyz/workflows/13809

## 节点清单

| 节点 | 类型 |
|------|------|
| Receive Task Request | Webhook |
| Set API Config | 数据设置 |
| Build Model Payload | Code |
| Call Hugging Face API | HTTP Request |
| Parse and Format Response | Code |
| Return Result | 响应 Webhook |

## 触发方式
- Receive Task Request 触发

## 统计
- 节点总数：6
- 触发节点：1
- 处理节点：3
- 输出节点：2
- 分类：workflow-automation
