## 简介
**Handling Job Application Submissions with AI and n8n Forms**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2579

---

# Handling Job Application Submissions with AI and n8n Forms


## 节点清单

| 节点 | 类型 |
|------|------|
| Extract from File | 从文件提取 |
| OpenAI Chat Model1 | OpenAI Chat Model |
| Structured Output Parser | 结构化输出解析器 |
| OpenAI Chat Model2 | OpenAI Chat Model |
| Step 1 of 2 - Upload CV | 表单触发器 |
| Save to Airtable | Airtable |
| Classify Document | 文本分类器 |
| Upload File to Record | HTTP Request |
| Form Success | 表单 |
| Save to Airtable1 | Airtable |
| Step 2 of 2 - Application Form | 表单触发器 |
| Application Suitability Agent | LLM Chain |
| File Upload Retry | 表单 |
| Redirect To Step 2 of 2 | 表单 |
| Submission Success | 表单 |



## 功能说明

表单问卷工具，自动收集和处理用户反馈（Handling)表单提交触发，通过 在线表格 + HTTP API 实现自动化。

，通过 在线表格 + HTTP API 实现自动化。

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

- 节点总数：15
- 触发方式：表单提交触发

## 触发方式
- Step 1 of 2 - Upload CV 触发
- Step 2 of 2 - Application Form 触发

## 统计
- 节点总数：15
- 触发节点：2
- 处理节点：12
- 输出节点：1
- 分类：workflow-automation
