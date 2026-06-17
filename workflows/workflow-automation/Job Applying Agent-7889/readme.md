## 简介
**Job Applying Agent**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/7889

---

# Job Applying Agent


## 节点清单

| 节点 | 类型 |
|------|------|
| On form submission | 表单触发器 |
| AI Agent | AI Agent |
| OpenAI Chat Model | OpenAI Chat Model |
| Send a message in Gmail | Gmail 工具 |
| Get row(s) in sheet in Google Sheets | Google Sheets 工具 |
| Form | 表单 |
| HTTP Request | HTTP Request |
| Markdown | Markdown |
| Information Extractor | 信息提取器 |
| OpenAI Chat Model1 | OpenAI Chat Model |
| If | IF 判断 |
| No Operation, do nothing | 空操作 |



## 功能说明

Job Applying Agent（AI 增强)表单提交触发，通过 邮箱 + 在线表格 + HTTP API 实现自动化。

，通过 邮箱 + 在线表格 + HTTP API 实现自动化。

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

- 节点总数：12
- 触发方式：表单提交触发

## 触发方式
- On form submission 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：10
- 输出节点：1
- 分类：workflow-automation
