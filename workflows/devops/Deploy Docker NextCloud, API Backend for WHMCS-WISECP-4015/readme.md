## 简介
**Deploy Docker NextCloud, API Backend for WHMCS-WISECP**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4015

---

# Deploy Docker NextCloud, API Backend for WHMCS-WISECP


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



## 功能说明

自动部署流水线，代码提交后自动构建和发布，Webhook 触发。

Webhook触发，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

无需额外 API Key，导入即可运行。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：43
- 触发方式：Webhook 触发

## 触发方式
- API 触发

## 统计
- 节点总数：43
- 触发节点：1
- 处理节点：37
- 输出节点：5
- 分类：devops
