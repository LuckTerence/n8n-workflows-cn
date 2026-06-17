## 简介
**Error Handling System with PostgreSQL Logging and Rate-Limited Notifications**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（需替换Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3882

---

# Error Handling System with PostgreSQL Logging and Rate-Limited Notifications


## 节点清单

| 节点 | 类型 |
|------|------|
| Error Trigger | 错误触发器 |
| Insert Log | PostgreSQL |
| Count for 5 minutes | PostgreSQL |
| Principal E-Mail | Email 发送 |
| Fallback E-Mail | Email 发送 |
| Push mobile notification | pushover |
| Truncate Log Database | PostgreSQL |
| Sometimes... just cleanup | 手动触发 |
| Call this Sample - Prepend to your error catcher | 执行工作流 |
| See below to prepend this at your error handling | 执行工作流触发器 |
| If there is no logs in 5 minutes | IF 判断 |
| CleanUp execution. See below if you will prepend this workflow | Code |
| Insert your error handling logic after this | 空操作 |



## 功能说明

内容管理工具，自动生成或发布内容。

手动触发，通过 邮箱 + 数据库 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- 邮箱 SMTP/IMAP 账号密码
- 数据库连接信息

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：13
- 触发方式：手动触发

## 触发方式
- Error Trigger 触发
- Sometimes... just cleanup 触发
- See below to prepend this at your error handling 触发

## 统计
- 节点总数：13
- 触发节点：3
- 处理节点：8
- 输出节点：2
- 分类：devops
