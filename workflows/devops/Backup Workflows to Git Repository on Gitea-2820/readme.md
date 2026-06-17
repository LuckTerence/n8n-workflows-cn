# Backup Workflows to Git Repository on Gitea

https://n8nworkflows.xyz/workflows/2820

## 节点清单

| 节点 | 类型 |
|------|------|
| Globals | 数据设置 |
| n8n | n8n |
| Schedule Trigger | 定时触发器 |
| SetDataUpdateNode | 数据设置 |
| SetDataCreateNode | 数据设置 |
| Base64EncodeUpdate | Code |
| Base64EncodeCreate | Code |
| Exist | IF 判断 |
| Changed | IF 判断 |
| PutGitea | HTTP Request |
| GetGitea | HTTP Request |
| PostGitea | HTTP Request |
| ForEach | 分批处理 |

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：13
- 触发节点：1
- 处理节点：9
- 输出节点：3
- 分类：devops
