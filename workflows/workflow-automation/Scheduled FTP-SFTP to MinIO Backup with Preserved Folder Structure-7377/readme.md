# Scheduled FTP-SFTP to MinIO Backup with Preserved Folder Structure

https://n8nworkflows.xyz/workflows/7377

## 节点清单

| 节点 | 类型 |
|------|------|
| List FTP Folder contents | FTP |
| Download content | FTP |
| Create Path for MinIO | 数据设置 |
| Upload on MinIO with correct Path | S3 |
| Schedule Trigger | 定时触发器 |

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：5
- 触发节点：1
- 处理节点：4
- 输出节点：0
- 分类：workflow-automation
