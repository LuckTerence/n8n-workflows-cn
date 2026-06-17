## 简介
**AI Prompt Generator Workflow**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5045

---

# AI Prompt Generator Workflow


## 节点清单

| 节点 | 类型 |
|------|------|
| On form submission | 表单触发器 |
| Google Gemini Chat Model | OpenAI Chat Model |
| Structured Output Parser | 结构化输出解析器 |
| BaseQuestions | 表单 |
| LoopQuestions | 分批处理 |
| RelevantQuestions | 表单 |
| MergeUserIntent | 数据合并 |
| PromptGenerator | LLM Chain |
| Google Gemini Chat Model1 | OpenAI Chat Model |
| RelatedQuestionAI | LLM Chain |
| SplitQuestions | 数据拆分 |
| Auto-fixing Output Parser | 自动修复输出解析器 |
| Structured Output Parser1 | 结构化输出解析器 |
| SendingPrompt | 表单 |



## 功能说明

n8n 工作流管理工具，编排控制工作流的启停（Prompt)表单提交触发，通过 n8n 内置节点实现自动化。

，通过 工作流编排 实现自动化。

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

- 节点总数：14
- 触发方式：表单提交触发

## 触发方式
- On form submission 触发

## 统计
- 节点总数：14
- 触发节点：1
- 处理节点：13
- 输出节点：0
- 分类：workflow-automation
