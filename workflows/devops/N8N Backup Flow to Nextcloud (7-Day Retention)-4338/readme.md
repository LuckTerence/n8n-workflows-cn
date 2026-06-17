# N8N Backup Flow to Nextcloud (7-Day Retention)

https://n8nworkflows.xyz/workflows/4338

## 节点清单

| 节点 | 类型 |
|------|------|
| On clicking 'execute' | 手动触发 |
| n8n | n8n |
| Loop Over Items | 分批处理 |
| Convert to File | 转换为文件 |
| Backups | 数据排序 |
| Schedule Trigger | 定时触发器 |
| Backup Path | 数据设置 |
| Nextcloud Directory | NextCloud |
| Nextcloud Upload | NextCloud |
| Nextcloud List Dir | NextCloud |
| Limits Backups | Code |
| Nextcloud - Delete old backups | NextCloud |

## 触发方式
- On clicking 'execute' 触发
- Schedule Trigger 触发

## 统计
- 节点总数：12
- 触发节点：2
- 处理节点：10
- 输出节点：0
- 分类：devops
