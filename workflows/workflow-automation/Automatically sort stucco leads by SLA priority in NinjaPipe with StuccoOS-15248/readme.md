## 简介
**Automatically sort stucco leads by SLA priority in NinjaPipe with StuccoOS**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/15248

---

# Automatically sort stucco leads by SLA priority in NinjaPipe with StuccoOS


## 节点清单

| 节点 | 类型 |
|------|------|
| When Email Arrives | Webhook |
| Filter Sent Emails | 过滤器 |
| Loop Over Emails | 分批处理 |
| Extract Email Content | Code |
| AI Email Classifier | 信息提取器 |
| Filter Spam Emails | 过滤器 |
| Build Email Labels | Code |
| Route by SLA Category | Switch 路由 |
| Notify Owner Immediately | Code |
| Create Urgent Task | Code |
| Create Standard Task | Code |
| Log Email and Wait 48h | Code |
| Chat Model Integration | Groq Chat Model |
| Wait 30 Seconds | 等待 |
| Search CRM for Contact | HTTP Request |
| Check Contact Existence | IF 判断 |
| Utilize Existing Contact | Code |
| Add New CRM Contact | HTTP Request |
| Retrieve New Contact ID | Code |
| Add Contact to SLA List | HTTP Request |
| Confirm CRM Update | Code |
| Select CRM List for SLA | Code |



## 功能说明

客户关系管理工具，自动管理销售线索和客户数据，Webhook 触发。

Webhook触发，通过 邮箱 + HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com
- 邮箱 SMTP/IMAP 账号密码

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：22
- 触发方式：Webhook 触发

## 触发方式
- When Email Arrives 触发

## 统计
- 节点总数：22
- 触发节点：1
- 处理节点：18
- 输出节点：3
- 分类：workflow-automation
