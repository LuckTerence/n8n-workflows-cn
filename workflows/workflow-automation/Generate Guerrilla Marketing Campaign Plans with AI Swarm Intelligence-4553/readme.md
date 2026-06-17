## 简介
**Generate Guerrilla Marketing Campaign Plans with AI Swarm Intelligence**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4553

---

# Generate Guerrilla Marketing Campaign Plans with AI Swarm Intelligence


## 节点清单

| 节点 | 类型 |
|------|------|
| When chat message received | Chat 触发器 |
| Introduction Writer | AI Agent |
| Campaign Definition Agent | AI Agent |
| Campaign Objectives Specialist | AI Agent |
| Current Situation Analyst | AI Agent |
| Target Persona Researcher | AI Agent |
| Key Messaging Specialist | AI Agent |
| Main Strategy Architect | AI Agent |
| guerrilla Tactics Designer | AI Agent |
| Channel Strategy Expert | AI Agent |
| Execution Planner | AI Agent |
| Budget Planning Specialist | AI Agent |
| Monitoring and KPIs Expert | AI Agent |
| Risk Management Expert | AI Agent |
| Do's and Don'ts Advisor | AI Agent |
| Final To-Do List Creator | AI Agent |
| Post-Campaign Analyst | AI Agent |
| Simple Memory | 记忆缓冲区 |
| Market Analyst | AI Agent |
| Idea Generator | AI Agent |
| Information Extractor | 信息提取器 |
| OpenAI Chat Model | OpenAI Chat Model |
| Input Parser | Code |
| Merge failed results | 数据合并 |
| combine outputs | Code |
| Merge successful result | 数据合并 |
| Combine outputs | Code |
| Merge results 1/2 | 数据合并 |
| Merge results 2/2 | 数据合并 |
| Merge results | 数据合并 |
| Result organizer | Code |
| Idea is good enough? | IF 判断 |
| Final result | 转换为文件 |



## 功能说明

Generate Guerrilla Marketing Campaign Plans with A（AI 增强)Chat 消息触发，通过 n8n 内置节点实现自动化。

Chat 消息触发，通过 工作流编排 实现自动化。

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

- 节点总数：33
- 触发方式：Chat 消息触发

## 触发方式
- When chat message received 触发

## 统计
- 节点总数：33
- 触发节点：1
- 处理节点：32
- 输出节点：0
- 分类：workflow-automation
