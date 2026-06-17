## 简介
**Generate Dynamic JSON Output Formats for AI Agents with Mistral**

（待补充中文描述）

> 分类：AI Agent | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5829

---

# Generate Dynamic JSON Output Formats for AI Agents with Mistral


## 节点清单

| 节点 | 类型 |
|------|------|
| Mistral Cloud Chat Model | Mistral Chat Model |
| JSON Output Parser | 结构化输出解析器 |
| JSON Generator | AI Agent |
| JSON Validator | AI Agent |
| JSON Output Parser 2 | 结构化输出解析器 |
| When clicking ‘Execute workflow’ | 手动触发 |
| Prepare Input | 数据设置 |
| Loop Until it Works | 分批处理 |
| Update Input | 数据设置 |
| If Valid JSON | IF 判断 |
| JSON Reviewer | AI Agent |
| Guarantee Input | 数据设置 |
| Mistral Cloud Chat Model 2 | Mistral Chat Model |
| Advanced JSON Output Parser | advancedOutputParser |
| Update Input 2 | 数据设置 |
| JSON Format Works! | 空操作 |
| Prepare Output | 数据设置 |
| If No More Rounds | IF 判断 |
| Round Limit Reached | 停止并报错 |



## 功能说明

表单问卷工具，自动收集和处理用户反馈。

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

- 节点总数：19
- 触发方式：手动触发

## 触发方式
- When clicking ‘Execute workflow’ 触发

## 统计
- 节点总数：19
- 触发节点：1
- 处理节点：18
- 输出节点：0
- 分类：ai-agent
