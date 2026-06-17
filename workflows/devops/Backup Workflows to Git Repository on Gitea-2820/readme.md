## 简介
**Backup Workflows to Git Repository on Gitea**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2820

---

# Backup Workflows to Git Repository on Gitea


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
