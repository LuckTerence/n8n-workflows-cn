## 简介
**Automated Kubernetes Testing with Robot Framework, ArgoCD & Complete KinD Lifecycle**

（待补充中文描述）

> 分类：DevOps | 适配等级：B（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/10302

---

# Automated Kubernetes Testing with Robot Framework, ArgoCD & Complete KinD Lifecycle


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Execute workflow’ | 手动触发 |
| Webhook | Webhook |
| Schedule Trigger | 定时触发器 |
| Get a file - ROBOT Script | gitlab |
| Set Parameters | 数据设置 |
| Robot Framework | robotFramework |
| Switch | Switch 路由 |
| Set Initialized | 数据设置 |
| Set Tested | 数据设置 |
| Set Destroyed | 数据设置 |
| Write Dowloaded ROBOT Script | 读写文件 |
| Add Robot Framework, Browser Library, Chromium Driver | 执行命令 |
| Read ROBOT Script to Execute | 读写文件 |
| Pack ROBOT Script Exports | 执行命令 |
| Read ROBOT Script Exports to Send | 读写文件 |
| Send ROBOT Script Export Pack | Telegram |
| Check Sshpass Exist Local | 执行命令 |
| Is Installed Local? | IF 判断 |
| Install Sshpass Local | 执行命令 |
| Check Docker on Target | 执行命令 |
| Is Docker Installed on Target? | IF 判断 |
| Install Docker on Target | 执行命令 |
| Install KinD on Target | 执行命令 |
| Is KinD Installed on Target? | IF 判断 |
| Check KinD on Target | 执行命令 |
| Get a file - KinD Config | gitlab |
| Write Dowloaded KinD Config | 读写文件 |
| Open KinD Config | 执行命令 |
| Create KinD Cluster on Target | 执行命令 |
| Is Docker Installed on Target?1 | IF 判断 |
| Is KinD Installed on Target?1 | IF 判断 |
| Check Sshpass Exist Local (D) | 执行命令 |
| Is Installed Local? (D) | IF 判断 |
| Install Sshpass Local (D) | 执行命令 |
| Check Docker on Target (D) | 执行命令 |
| Delete KinD Cluster on Target | 执行命令 |
| Check KinD on Target (D) | 执行命令 |
| UnInstall KinD on Target | 执行命令 |
| UnInstall Docker on Target | 执行命令 |
| Process Finish Report --- Telegam & SMS1 | 执行命令 |
| Install Helm and Nginx-Ingress in KinD Cluster | 执行命令 |
| Install HAProxy on Target and Config Port-80 to KinD | 执行命令 |
| No Operation, do nothing | 空操作 |
| Is INIT Only? | IF 判断 |
| Is TEST Only? | IF 判断 |
| Delete HAProxy on Target | 执行命令 |
| Open ROBOT Script to Framework | 执行命令 |
| Add Target to Hosts | 执行命令 |
| Remove Target from Hosts | 执行命令 |
| Install ArgoCD to KinD Cluster | 执行命令 |
| Get a file - ArgoCD ApplicationSet | gitlab |
| Write Dowloaded ArgoCD ApplicationSet | 读写文件 |
| Open ArgoCD ApplicationSet | 执行命令 |
| Apply ArgoCD ApplicationSet | 执行命令 |

## 触发方式
- When clicking ‘Execute workflow’ 触发
- Webhook 触发
- Schedule Trigger 触发

## 统计
- 节点总数：54
- 触发节点：3
- 处理节点：50
- 输出节点：1
- 分类：devops
