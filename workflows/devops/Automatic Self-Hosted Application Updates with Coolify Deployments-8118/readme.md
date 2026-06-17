# Automatic Self-Hosted Application Updates with Coolify Deployments

https://n8nworkflows.xyz/workflows/8118

## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule every time you want start the update check | 定时触发器 |
| No Operation, do nothing | 空操作 |
| If the 2 versions is not the same make an update of image | IF 判断 |
| CALL COOLIFY OR SIMILAR SERVICE FOR UPDATE IMAGE | HTTP Request |
| Rename variable and unify format | 数据设置 |
| Merge bot data and pass just what we need | 数据合并 |
| When clicking ‘Execute workflow | 手动触发 |
| CALL YOUR N8N INSTANCE and retrieve the version | HTTP Request |
| CALL GITHUB and retrieve the last n8n image stable version | HTTP Request |

## 触发方式
- Schedule every time you want start the update check 触发
- When clicking ‘Execute workflow 触发

## 统计
- 节点总数：9
- 触发节点：2
- 处理节点：4
- 输出节点：3
- 分类：devops
