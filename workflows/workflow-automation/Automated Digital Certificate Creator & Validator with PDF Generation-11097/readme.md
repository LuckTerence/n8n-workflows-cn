## 简介
**Automated Digital Certificate Creator & Validator with PDF Generation**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/11097

---

# Automated Digital Certificate Creator & Validator with PDF Generation


## 节点清单

| 节点 | 类型 |
|------|------|
| Insert_Certificaton | 数据表 |
| Generate_Certification_ID | Code |
| Find_Certification_By_ID | 数据表 |
| Certification_ID_Exists | IF 判断 |
| Generate_PDF | pdfGeneratorApi |
| Email_Certification | Email 发送 |
| Webhook_Check | Webhook |
| Find_Certification_By_ID1 | 数据表 |
| Certification_Exists | IF 判断 |
| Respond_Found | 响应 Webhook |
| Respond_NotFound | 响应 Webhook |
| Webhook_Creation | Webhook |



## 功能说明

PDF 文档处理，解析或生成 PDF 文件，Webhook 触发。

Webhook触发，通过 邮箱 + HTTP API 实现自动化。

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

- 节点总数：12
- 触发方式：Webhook 触发

## 触发方式
- Webhook_Check 触发
- Webhook_Creation 触发

## 统计
- 节点总数：12
- 触发节点：2
- 处理节点：7
- 输出节点：3
- 分类：workflow-automation
