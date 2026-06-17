## 简介
**Automated Construction Project Alerts with Email Notifications and Data APIs**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/6963

---

# Automated Construction Project Alerts with Email Notifications and Data APIs


## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Trigger | 定时触发器 |
| Email Trigger | Email 读取 |
| Check Email Subject | IF 判断 |
| Extract Location Info | Code |
| Search Government Data | HTTP Request |
| Search Construction Sites | HTTP Request |
| Process Construction Data | Code |
| Check if Projects Found | IF 判断 |
| Generate Email Report | Code |
| Send Alert Email | Email 发送 |
| Send No Results Email | Email 发送 |
| Wait For Data | 等待 |



## 功能说明

邮件自动化处理，AI 分类整理或。

定时触发，通过 邮箱 + HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- 邮箱 SMTP/IMAP 账号密码
- 搜索 API Key（如 SerpAPI / Brave Search）

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：12
- 触发方式：定时触发

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：6
- 输出节点：5
- 分类：devops
