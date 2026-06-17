## 简介
**Generate SEO Seed Keywords Using AI**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2473

---

# Generate SEO Seed Keywords Using AI


## 节点清单

| 节点 | 类型 |
|------|------|
| Anthropic Chat Model | OpenAI Chat Model |
| Split Out | 数据拆分 |
| Set Ideal Customer Profile (ICP) | 数据设置 |
| Aggregate for AI node | 数据聚合 |
| AI Agent | AI Agent |
| Connect to your own database | 空操作 |
| When clicking ‘Test workflow’ | 手动触发 |



## 功能说明

SEO 优化工具，关键词分析和内容优化。

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

- 节点总数：7
- 触发方式：手动触发

## 触发方式
- When clicking ‘Test workflow’ 触发

## 统计
- 节点总数：7
- 触发节点：1
- 处理节点：6
- 输出节点：0
- 分类：workflow-automation
