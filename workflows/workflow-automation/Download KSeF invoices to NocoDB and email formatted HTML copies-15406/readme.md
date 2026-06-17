## 简介
**Download KSeF invoices to NocoDB and email formatted HTML copies**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/15406

---

# Download KSeF invoices to NocoDB and email formatted HTML copies


## 节点清单

| 节点 | 类型 |
|------|------|
| ⚙️ Config | 数据设置 |
| Get Public Key | HTTP Request |
| Get Challenge | HTTP Request |
| Encrypt Token | Code |
| Init Auth | HTTP Request |
| Check Auth Status | HTTP Request |
| Redeem Token | HTTP Request |
| Extract Invoices | Code |
| Send an Email | Email 发送 |
| Convert to File | 转换为文件 |
| Covert to Base64 | Code |
| Query Cost Invoices | HTTP Request |
| Query Issued Invoices | HTTP Request |
| Process only new invoices | 数据合并 |
| For each invoice | 分批处理 |
| Get invoice details | HTTP Request |
| to JSON | XML |
| Convert to HTML | Code |
| Created row with file input to be sent | 数据合并 |
| Insert new invoice details | NocoDB |
| Process both types | 数据合并 |
| Get existing invoices | NocoDB |
| Mark as "issued" invoice | 数据设置 |
| Mark as "cost" invoice | 数据设置 |
| Combine HTML with base invoice data | 数据合并 |
| Monitor Every Day for new invoices | 定时触发器 |
| Wait | 等待 |
| Terminate Auth Session | HTTP Request |
| Wait 2s | 等待 |
| Create Tables | 手动触发 |
| NocoDB Config | 数据设置 |
| Create NocoDB KSeF Invoices Table | HTTP Request |



## 功能说明

邮件自动化处理，AI 分类整理或。

定时触发、手动触发，通过 邮箱 + HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- 邮箱 SMTP/IMAP 账号密码
- 通义万相 API Key → https://dashscope.aliyun.com

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：32
- 触发方式：定时触发, 手动触发

## 触发方式
- Monitor Every Day for new invoices 触发
- Create Tables 触发

## 统计
- 节点总数：32
- 触发节点：2
- 处理节点：19
- 输出节点：11
- 分类：workflow-automation
