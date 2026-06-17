## 简介
**Auto-generate sticky notes and rename nodes**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Notion/Google Sheets/Slack/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/13868

---

# Auto-generate sticky notes and rename nodes


## 节点清单

| 节点 | 类型 |
|------|------|
| Start | 手动触发 |
| Parse Nodes | Code |
| AI Groups Logically | AI Agent |
| OpenAI Chat Model | OpenAI Chat Model |
| Structured Output Parser | 结构化输出解析器 |
| Generate Stickies | Code |
| Strip & Prepare | Code |
| Compute Bounding Boxes | Code |
| Collision Resolution | Code |
| Merge & Export | Code |
| Pick Best Result | Code |
| Collision Detector | Code |
| If | IF 判断 |
| Loop Controller (Automatic Fixer) | Code |
| Set Workflow Variables | 数据设置 |
| Should Rename Nodes | IF 判断 |
| Output Normalization | 数据设置 |
| Parse for Renaming | Code |
| AI Rename | AI Agent |
| Apply Renames | Code |
| Format for Export | Code |
| OpenAI Chat Model1 | OpenAI Chat Model |
| Structured Output Parser1 | 结构化输出解析器 |



## 功能说明

Auto-generate sticky notes and rename nodes（AI 增强)手动触发，通过 n8n 内置节点实现自动化。

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
- 触发方式：手动触发

## 触发方式
- Start 触发

## 统计
- 节点总数：23
- 触发节点：1
- 处理节点：22
- 输出节点：0
- 分类：workflow-automation
