# Kubernetes Deployment & Pod Monitoring with Telegram Alerts

https://n8nworkflows.xyz/workflows/9613

## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Trigger | 定时触发器 |
| Kubeconfig Setup | Code |
| Get Pods | 执行命令 |
| Get Deployments | 执行命令 |
| Process & Generate Report | Code |
| Has Alerts? | IF 判断 |
| Send Telegram Alert | Telegram |
| Save Report | 写入二进制文件 |

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：8
- 触发节点：1
- 处理节点：6
- 输出节点：1
- 分类：devops
