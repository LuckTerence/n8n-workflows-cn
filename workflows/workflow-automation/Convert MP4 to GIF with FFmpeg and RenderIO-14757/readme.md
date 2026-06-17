# Convert MP4 to GIF with FFmpeg and RenderIO

https://n8nworkflows.xyz/workflows/14757

## 节点清单

| 节点 | 类型 |
|------|------|
| When Video Submitted | 表单触发器 |
| Render MP4 to GIF | renderio |
| Wait 10 Seconds Initial | 等待 |
| Check Conversion Status | renderio |
| If Conversion Complete | IF 判断 |
| Display Download Link | 表单 |
| Wait 30 Seconds Retry | 等待 |

## 触发方式
- When Video Submitted 触发

## 统计
- 节点总数：7
- 触发节点：1
- 处理节点：6
- 输出节点：0
- 分类：workflow-automation
