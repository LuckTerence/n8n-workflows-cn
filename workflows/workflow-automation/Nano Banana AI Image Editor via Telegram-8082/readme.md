# Nano Banana AI Image Editor via Telegram

https://n8nworkflows.xyz/workflows/8082

## 节点清单

| 节点 | 类型 |
|------|------|
| Photo Message Receiver | Telegram 触发器 |
| Download Telegram Photo | Telegram |
| Convert Photo to Base64 | 从文件提取 |
| Format Image Data URL | Code |
| Parse AI Response Data | 数据设置 |
| Base64 to Binary File | 转换为文件 |
| Send Processed Photo | Telegram |
| Nano Banana Image Processor | HTTP Request |

## 触发方式
- Photo Message Receiver 触发

## 统计
- 节点总数：8
- 触发节点：1
- 处理节点：4
- 输出节点：3
- 分类：workflow-automation
