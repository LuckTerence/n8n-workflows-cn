## 简介
**AI Automated HR Workflow for CV Analysis and Candidate Evaluation**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Google Drive)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2860

---

# AI Automated HR Workflow for CV Analysis and Candidate Evaluation


## 节点清单

| 节点 | 类型 |
|------|------|
| On form submission | 表单触发器 |
| Extract from File | 从文件提取 |
| Qualifications | 信息提取器 |
| Summarization Chain | chainSummarization |
| Merge | 数据合并 |
| Profile Wanted | 数据设置 |
| Google Sheets | Google Sheets |
| Structured Output Parser | 结构化输出解析器 |
| HR Expert | LLM Chain |
| Personal Data | 信息提取器 |
| Upload CV | Google Drive |
| OpenAI | OpenAI Chat Model |



## 功能说明

AI 招聘助手，简历筛选或面试流程自动化（Workflow)表单提交触发，通过 在线表格 + HTTP API 实现自动化。

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

- 节点总数：12
- 触发方式：表单提交触发

## 触发方式
- On form submission 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：11
- 输出节点：0
- 分类：workflow-automation
