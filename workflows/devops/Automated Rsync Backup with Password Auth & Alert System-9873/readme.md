# Automated Rsync Backup with Password Auth & Alert System

https://n8nworkflows.xyz/workflows/9873

## 节点清单

| 节点 | 类型 |
|------|------|
| Manual Trigger | 手动触发 |
| Server Parameters | 数据设置 |
| Check Sshpass Local | 执行命令 |
| Is Installed Local? | IF 判断 |
| Install Sshpass Local | 执行命令 |
| Check Sshpass on Source | 执行命令 |
| Is Installed on Source? | IF 判断 |
| Install Sshpass on Source | 执行命令 |
| Execute Rsync Backup | 执行命令 |
| Success? | IF 判断 |
| Backup Successful | 数据设置 |
| Backup Failed | 数据设置 |
| Process Finish Report --- Telegam & SMS | 执行命令 |
| Schedule Trigger | 定时触发器 |

## 触发方式
- Manual Trigger 触发
- Schedule Trigger 触发

## 统计
- 节点总数：14
- 触发节点：2
- 处理节点：12
- 输出节点：0
- 分类：devops
