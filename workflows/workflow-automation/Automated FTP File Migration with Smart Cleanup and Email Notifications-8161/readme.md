# Automated FTP File Migration with Smart Cleanup and Email Notifications

https://n8nworkflows.xyz/workflows/8161

## 节点清单

| 节点 | 类型 |
|------|------|
| Daily Schedule (2 AM) | 定时触发器 |
| List Files - Source FTP | FTP |
| Filter Files | 过滤器 |
| Download File | FTP |
| Upload to Destination | FTP |
| Upload Success? | 过滤器 |
| Delete Source File | FTP |
| Log Success | 数据设置 |
| Send Email Success Alert | Email 发送 |

## 触发方式
- Daily Schedule (2 AM) 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：7
- 输出节点：1
- 分类：workflow-automation
