## 简介
**Deploy Docker Grafana, API Backend for WHMCS-WISECP**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4011

---

# Deploy Docker Grafana, API Backend for WHMCS-WISECP


## 节点清单

| 节点 | 类型 |
|------|------|
| If | IF 判断 |
| Parametrs | 数据设置 |
| API | Webhook |
| 422-Invalid server domain | 响应 Webhook |
| Code1 | Code |
| SSH | SSH |
| Container Actions | Switch 路由 |
| Service Actions | Switch 路由 |
| API answer | 响应 Webhook |
| Inspect | 数据设置 |
| Stat | 数据设置 |
| Start | 数据设置 |
| Stop | 数据设置 |
| Test Connection1 | 数据设置 |
| Deploy | 数据设置 |
| Suspend | 数据设置 |
| Terminated | 数据设置 |
| Unsuspend | 数据设置 |
| Mount Disk | 数据设置 |
| Unmount Disk | 数据设置 |
| Log | 数据设置 |
| ChangePackage | 数据设置 |
| Deploy-docker-compose | 数据设置 |
| Version | 数据设置 |
| If1 | IF 判断 |
| nginx | 数据设置 |
| Container Stat | Switch 路由 |
| GET ACL | 数据设置 |
| SET ACL | 数据设置 |
| GET NET | 数据设置 |
| Change Password | 数据设置 |
| Grafana | Switch 路由 |

## 触发方式
- API 触发

## 统计
- 节点总数：32
- 触发节点：1
- 处理节点：29
- 输出节点：2
- 分类：devops
