# Deploy Docker NextCloud, API Backend for WHMCS-WISECP

https://n8nworkflows.xyz/workflows/4015

## 节点清单

| 节点 | 类型 |
|------|------|
| If | IF 判断 |
| Parametrs | 数据设置 |
| API | Webhook |
| 422-Invalid server domain | 响应 Webhook |
| Container Actions | Switch 路由 |
| Container Stats | Switch 路由 |
| Inspect | 数据设置 |
| Stat | 数据设置 |
| Start | 数据设置 |
| Stop | 数据设置 |
| Mount Disk | 数据设置 |
| Unmount Disk | 数据设置 |
| Log | 数据设置 |
| Deploy-docker-compose | 数据设置 |
| Version | 数据设置 |
| Users | 数据设置 |
| Change Password | 数据设置 |
| NextCloud | Switch 路由 |
| nginx | 数据设置 |
| Test Connection | 数据设置 |
| ChangePackage | 数据设置 |
| Terminated | 数据设置 |
| Unsuspend | 数据设置 |
| Suspend | 数据设置 |
| Deploy | 数据设置 |
| Service Actions | Switch 路由 |
| If1 | IF 判断 |
| Dependent containers Stat | 数据设置 |
| GET ACL | 数据设置 |
| SET ACL | 数据设置 |
| GET NET | 数据设置 |
| If2 | IF 判断 |
| Split domain | Code |
| DNS Service Actions | Switch 路由 |
| DNS Parametrs | 数据设置 |
| Add record | HTTP Request |
| Delete record | HTTP Request |
| API answer1 | 响应 Webhook |
| d01-test.uuq.pl | SSH |
| d02-test.uuq.pl | SSH |
| Servers Switch | Switch 路由 |
| Code | Code |
| API answer2 | 响应 Webhook |

## 触发方式
- API 触发

## 统计
- 节点总数：43
- 触发节点：1
- 处理节点：37
- 输出节点：5
- 分类：devops
