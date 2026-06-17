## 简介
**Automated Workflow & Credential Restoration System for Self-Hosted Environments**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/9154

---

# Automated Workflow & Credential Restoration System for Self-Hosted Environments


## 节点清单

| 节点 | 类型 |
|------|------|
| Start Restore | 手动触发 |
| SUCCESS email | Email 发送 |
| List Bkp Folders | 执行命令 |
| Restore Credentials | 执行命令 |
| SUCCESS email Workflows | Email 发送 |
| Exclude Current Workflow From Selection | 执行命令 |
| Restore Workflows | 执行命令 |
| Init | Code |
| Restore Credentials? | IF 判断 |
| Restore Workflows? | IF 判断 |
| Delete TEMP Folder | 执行命令 |
| ERROR: Find Most Recent Bkp Folder | 停止并报错 |
| Find Last Backup | Code |



## 功能说明

n8n 工作流管理工具，编排控制工作流的启停。

手动触发，通过 邮箱 实现自动化。

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

- 节点总数：13
- 触发方式：手动触发

## 触发方式
- Start Restore 触发

## 统计
- 节点总数：13
- 触发节点：1
- 处理节点：10
- 输出节点：2
- 分类：workflow-automation
