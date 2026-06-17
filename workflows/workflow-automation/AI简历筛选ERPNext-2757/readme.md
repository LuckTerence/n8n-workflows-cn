## 简介
**AI简历筛选ERPNext**

自动筛选候选人关联ERPNext

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2757

---

# AI简历筛选ERPNext


## 节点清单

| 节点 | 类型 |
|------|------|
| Code | Code |
| ApplicantData | 数据设置 |
| ERPNext - Reject if Resume not Attached | erpNext |
| Applied Against Job | IF 判断 |
| ERPNext - Hold Applicant | erpNext |
| Get Job Opening | erpNext |
| Google Gemini Chat Model | Google Gemini |
| Convert to Fields | Code |
| If score less than 80 | IF 判断 |
| Reject Applicant | HTTP Request |
| Update Applicant Data | HTTP Request |
| Reume Attachment Link | 数据设置 |
| Resume Link Provided | IF 判断 |
| Accept Applicant | HTTP Request |
| Webhook | Webhook |
| File Type | Switch 路由 |
| Download PDF Resume | HTTP Request |
| PDF to Text | 从文件提取 |
| Txt File to Text (Example) | 从文件提取 |
| Merge1 | 数据合并 |
| Recruitment AI Agent | AI Agent |
| Microsoft Outlook | Outlook |
| WhatsApp Business Cloud | WhatsApp |



## 功能说明

AI 招聘助手，简历筛选或面试流程自动化，Webhook 触发。

Webhook触发，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：23
- 触发方式：Webhook 触发

## 触发方式
- Webhook 触发

## 统计
- 节点总数：23
- 触发节点：1
- 处理节点：16
- 输出节点：6
- 分类：workflow-automation
