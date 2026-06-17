## 简介
**ScriptSentry: Detect Sensitive Information in JavaScript**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5497

---

# ScriptSentry: Detect Sensitive Information in JavaScript


## 节点清单

| 节点 | 类型 |
|------|------|
| Landing Page Url1 | 表单触发器 |
| Puppeteer1 | puppeteer |
| JavaScript Extractor1 | Code |
| Aggregate1 | 数据聚合 |
| Data Mapper1 | 数据设置 |
| Format Report for Email1 | Code |
| Send a message1 | Email 发送 |
| OpenAI Chat Model | OpenAI Chat Model |
| JavaScript Search Agent w/Email Template1 | AI Agent |



## 功能说明

表单问卷工具，自动收集和处理用户反馈（Scriptsentry)表单提交触发，通过 邮箱 实现自动化。

，通过 邮箱 实现自动化。

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

- 节点总数：9
- 触发方式：表单提交触发

## 触发方式
- Landing Page Url1 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：7
- 输出节点：1
- 分类：workflow-automation
