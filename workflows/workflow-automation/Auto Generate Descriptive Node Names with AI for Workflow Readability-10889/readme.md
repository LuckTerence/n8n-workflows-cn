## 简介
**Auto Generate Descriptive Node Names with AI for Workflow Readability**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/10889

---

# Auto Generate Descriptive Node Names with AI for Workflow Readability


## 节点清单

| 节点 | 类型 |
|------|------|
| Save Renamed Workflow Version | n8n |
| Prepare LLM Validation Data | 数据设置 |
| Generate Node Rename Mapping | LLM Chain |
| Apply Renamed Nodes Connections | 数据设置 |
| Parse LLM Mapping ToJson | 结构化输出解析器 |
| Extract Workflow Nodes Connections | 数据设置 |
| Assemble New Workflow Object | 数据设置 |
| Validate All Nodes Renamed | IF 判断 |
| Build Workflow Version Links | 数据设置 |
| Parse Selected Workflow Id | 数据设置 |
| Check Trigger Source Type | IF 判断 |
| Display Workflow Version Links | 表单 |
| Set Target Workflow Id | 数据设置 |
| Select a Workflow | n8n |
| Stop | 停止并报错 |
| Fetch Target Workflow JSON | n8n |
| Aggregate Workflow List | 数据聚合 |
| Form Dynamic Workflow List | 表单 |
| OpenRouter Chat Model | OpenRouter Chat Model |
| Fetch All Workflows | n8n |
| Form Trigger | 表单触发器 |
| Manual Trigger | 手动触发 |
| Done | 数据设置 |



## 功能说明

n8n 工作流管理工具，编排控制工作流的启停（Auto)表单提交触发、手动触发，通过 n8n 内置节点实现自动化。

手动触发，通过 工作流编排 实现自动化。

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
- 触发方式：表单提交触发, 手动触发

## 触发方式
- Form Trigger 触发
- Manual Trigger 触发

## 统计
- 节点总数：23
- 触发节点：2
- 处理节点：21
- 输出节点：0
- 分类：workflow-automation
