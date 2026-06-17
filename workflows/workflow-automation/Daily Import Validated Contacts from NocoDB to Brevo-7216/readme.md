## 简介
**Daily Import Validated Contacts from NocoDB to Brevo**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/7216

---

# Daily Import Validated Contacts from NocoDB to Brevo


## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Trigger | 定时触发器 |
| Check if parameters are not empty | IF 判断 |
| Check if email is Disposal | IF 判断 |
| Loop Over Items | 分批处理 |
| Brevo: Create Contact | sendInBlue |
| NocoDB: Get new users list | NocoDB |
| NocoDB: change status to 1-empty-fields | NocoDB |
| NocoDB: change status to 2-disposal-email | NocoDB |
| NocoDB: change status to 3-contact-created | NocoDB |



## 功能说明

Daily Import Validated Contacts from NocoDB to Bre。

定时触发，通过 邮箱 实现自动化。

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

- 节点总数：9
- 触发方式：定时触发

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：8
- 输出节点：0
- 分类：workflow-automation
