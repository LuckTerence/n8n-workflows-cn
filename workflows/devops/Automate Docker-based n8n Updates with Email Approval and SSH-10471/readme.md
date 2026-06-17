# Automate Docker-based n8n Updates with Email Approval and SSH

https://n8nworkflows.xyz/workflows/10471

## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Trigger | 定时触发器 |
| If No Changes | IF 判断 |
| Check Existence of Update Script | SSH |
| If File Exists | IF 判断 |
| Create Update Script | SSH |
| If Approved | IF 判断 |
| No Updates | 空操作 |
| Do Nothing | 空操作 |
| Ask For Approval to Update | Email 发送 |
| Execute Update Script | SSH |
| Get Local Image Digest | SSH |
| Get Remote Image Digest | HTTP Request |
| Prepare Update Data | 数据设置 |
| Get Current n8n Version | SSH |

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：14
- 触发节点：1
- 处理节点：11
- 输出节点：2
- 分类：devops
