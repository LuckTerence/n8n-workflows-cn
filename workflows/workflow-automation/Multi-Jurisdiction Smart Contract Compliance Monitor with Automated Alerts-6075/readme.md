## 简介
**Multi-Jurisdiction Smart Contract Compliance Monitor with Automated Alerts**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/6075

---

# Multi-Jurisdiction Smart Contract Compliance Monitor with Automated Alerts


## 节点清单

| 节点 | 类型 |
|------|------|
| Daily Compliance Check | 定时触发器 |
| Compliance Settings | 数据设置 |
| Monitor EU Regulations | HTTP Request |
| Monitor US Federal Register | HTTP Request |
| Monitor UK Legislation | HTTP Request |
| Get Active Contracts | PostgreSQL |
| Analyze Compliance Impact | Code |
| Filter Critical Compliance Issues | IF 判断 |
| Send Critical Legal Alert | Email 发送 |
| Filter High Risk Issues | IF 判断 |
| Send High Risk Alert | Email 发送 |
| Filter Medium Risk Issues | IF 判断 |
| Send Medium Risk Alert | Email 发送 |
| Log Compliance Check | Google Sheets |



## 功能说明

监控告警系统，异常检测并发送通知，定时执行。

定时触发，通过 邮箱 + 数据库 + HTTP API 实现自动化。

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

- 节点总数：14
- 触发方式：定时触发

## 触发方式
- Daily Compliance Check 触发

## 统计
- 节点总数：14
- 触发节点：1
- 处理节点：7
- 输出节点：6
- 分类：workflow-automation
