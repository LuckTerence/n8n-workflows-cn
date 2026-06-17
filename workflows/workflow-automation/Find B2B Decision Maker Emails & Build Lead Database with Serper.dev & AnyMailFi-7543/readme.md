## 简介
**Find B2B Decision Maker Emails & Build Lead Database with Serper.dev & AnyMailFinder**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/7543

---

# Find B2B Decision Maker Emails & Build Lead Database with Serper.dev & AnyMailFinder


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Execute workflow’ | 手动触发 |
| Get many rows | NocoDB |
| serper search domains | HTTP Request |
| extract url & domain | OpenAI |
| Get Sales Decision Maker Email | HTTP Request |
| Get Marketing Email | HTTP Request |
| Get CEO Email | HTTP Request |
| Update Companies Domains | NocoDB |
| Update Company Status | NocoDB |
| Filter | 过滤器 |
| Remove Duplicates | 去重 |
| Merge1 | 数据合并 |
| Extract Data3 | 数据设置 |
| Extract Data4 | 数据设置 |
| Extract Data5 | 数据设置 |
| Determine Email Status by Company | Code |
| Get All Company Status | NocoDB |
| If Only Risky Emails1 | 过滤器 |
| If Email Found1 | IF 判断 |
| Get All Company Emails | HTTP Request |
| Update Company Emails | NocoDB |
| Loop Over Items | 分批处理 |
| Filter1 | 过滤器 |
| Create Contacts | NocoDB |
| Wait | 等待 |
| Schedule Trigger2 | 定时触发器 |
| Merge | 数据合并 |



## 功能说明

邮件自动化处理，AI 分类整理或。

定时触发、手动触发，通过 邮箱 + HTTP API 实现自动化。

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

- 节点总数：27
- 触发方式：手动触发, 定时触发

## 触发方式
- When clicking ‘Execute workflow’ 触发
- Schedule Trigger2 触发

## 统计
- 节点总数：27
- 触发节点：2
- 处理节点：20
- 输出节点：5
- 分类：workflow-automation
