## 简介
**Email reports on expiring Microsoft Entra ID app secrets and certificates with Microsoft Graph**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/12399

---

# Email reports on expiring Microsoft Entra ID app secrets and certificates with Microsoft Graph


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Execute workflow’ | 手动触发 |
| Split Out Applications | 数据拆分 |
| Set Variables | 数据设置 |
| Merge | 数据合并 |
| Filter Client Secrets | 过滤器 |
| Split Out Client Secrets | 数据拆分 |
| Split Out Certificates | 数据拆分 |
| Filter Client Certificates | 过滤器 |
| Build Client Secrets Report | 数据设置 |
| Build Certificates Report | 数据设置 |
| Get EntraID Applications and Secrets | HTTP Request |
| Aggregate | 数据聚合 |
| If Expiring Secrets not empty | IF 判断 |
| No Operation, do nothing | 空操作 |
| HTML Table with Expiring Secrets | HTML |
| Send email | Email 发送 |



## 功能说明

邮件自动化处理，AI 分类整理或。

定时触发、手动触发，通过 邮箱 + HTTP API 实现自动化。

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

- 节点总数：16
- 触发方式：手动触发

## 触发方式
- When clicking ‘Execute workflow’ 触发

## 统计
- 节点总数：16
- 触发节点：1
- 处理节点：13
- 输出节点：2
- 分类：workflow-automation
