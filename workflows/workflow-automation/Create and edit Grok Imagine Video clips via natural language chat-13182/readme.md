# Create and edit Grok Imagine Video clips via natural language chat

https://n8nworkflows.xyz/workflows/13182

## 节点清单

| 节点 | 类型 |
|------|------|
| Run text to video | 工作流工具 |
| Run Text-to-Video1 | 执行工作流触发器 |
| When chat message received | Chat 触发器 |
| Simple Memory | 记忆缓冲区 |
| Get status | HTTP Request |
| Completed? | IF 判断 |
| Switch1 | Switch 路由 |
| Get status1 | HTTP Request |
| Completed?1 | IF 判断 |
| Run image to video | 工作流工具 |
| Get status2 | HTTP Request |
| Completed?2 | IF 判断 |
| Run video to video | 工作流工具 |
| Grok 4.1 Fast | OpenRouter Chat Model |
| Binary? | IF 判断 |
| Set Image Url | 数据设置 |
| Grok Imagine Video Agent | AI Agent |
| Edit Video | HTTP Request |
| Text to Video | HTTP Request |
| Image to Video | HTTP Request |
| Get final text to video url | HTTP Request |
| Get final edit video url | HTTP Request |
| Get final image to video url | HTTP Request |
| Wait 10 sec. | 等待 |
| Wait 10 sec.1 | 等待 |
| Wait 10 sec.2 | 等待 |
| Upload image | FTP |

## 触发方式
- Run Text-to-Video1 触发
- When chat message received 触发

## 统计
- 节点总数：27
- 触发节点：2
- 处理节点：16
- 输出节点：9
- 分类：workflow-automation
