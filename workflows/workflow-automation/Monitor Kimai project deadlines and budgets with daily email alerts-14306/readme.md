## 简介
**Monitor Kimai project deadlines and budgets with daily email alerts**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/14306

---

# Monitor Kimai project deadlines and budgets with daily email alerts


## 节点清单

| 节点 | 类型 |
|------|------|
| Send an Email | Email 发送 |
| Every Day at 9:00 | 定时触发器 |
| GET Projects | HTTP Request |
| Get only Bilable | Code |
| GET Projects Details | HTTP Request |
| GET Timesheet Records | HTTP Request |
| Calculate Budget Uses | Code |
| Combine Data | 数据合并 |
| Calculate expiration | Code |
| Need Email? | IF 判断 |
| Build Email HTML - Report | Code |



## 功能说明

邮件自动化处理，AI 分类整理或。

定时触发，通过 邮箱 + HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- 邮箱 SMTP/IMAP 账号密码

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：11
- 触发方式：定时触发

## 触发方式
- Every Day at 9:00 触发

## 统计
- 节点总数：11
- 触发节点：1
- 处理节点：6
- 输出节点：4
- 分类：workflow-automation
