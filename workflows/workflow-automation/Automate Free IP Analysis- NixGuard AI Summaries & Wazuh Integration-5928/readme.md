## 简介
**Automate Free IP Analysis: NixGuard AI Summaries & Wazuh Integration**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Slack)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5928

---

# Automate Free IP Analysis: NixGuard AI Summaries & Wazuh Integration


## 节点清单

| 节点 | 类型 |
|------|------|
| Execute NixGuard & Wazuh Workflow | 执行工作流 |
| Format NixGuard AI Summary & Wazuh Insights | 数据设置 |
| (Optional) Send Slack Alert for High-Risk Events | Slack |
| Set API Key & Initial Prompt1 | 数据设置 |
| Webhook Trigger
(REAL-WORLD USE)1 | Webhook |



## 功能说明

AI 内容摘要工具，自动提炼长文关键信息，Webhook 触发。

Webhook触发，通过 Slack + HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

无需额外 API Key，导入即可运行。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：5
- 触发方式：Webhook 触发

## 触发方式
- Webhook Trigger
(REAL-WORLD USE)1 触发

## 统计
- 节点总数：5
- 触发节点：1
- 处理节点：3
- 输出节点：1
- 分类：workflow-automation
