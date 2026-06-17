## 简介
**Generate and verify email patterns from chat input with Reoon Email Verifier**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/16102

---

# Generate and verify email patterns from chat input with Reoon Email Verifier


## 节点清单

| 节点 | 类型 |
|------|------|
| Loop Over Email Variations | 分批处理 |
| If Score Above 70 | IF 判断 |
| Check Email Status | IF 判断 |
| Notify Chat Success | 聊天 |
| Notify No Email Result | 聊天 |
| Query First Name | 聊天 |
| Query Last Name | 聊天 |
| Query Domain Name | 聊天 |
| Create Email Variations | Code |
| Verify Email with Reoon | HTTP Request |
| Normalize Verification Data | Code |



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

- 节点总数：11
- 触发方式：手动或子流程调用

## 触发方式
- 手动触发

## 统计
- 节点总数：11
- 触发节点：0
- 处理节点：5
- 输出节点：6
- 分类：workflow-automation
