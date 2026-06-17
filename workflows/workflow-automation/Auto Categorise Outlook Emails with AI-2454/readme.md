## 简介
**Auto Categorise Outlook Emails with AI**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2454

---

# Auto Categorise Outlook Emails with AI


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Test workflow’ | 手动触发 |
| Ollama Chat Model1 | Ollama Chat Model |
| Microsoft Outlook10 | Outlook |
| Microsoft Outlook12 | Outlook |
| Loop Over Items1 | 分批处理 |
| Microsoft Outlook13 | Outlook |
| Microsoft Outlook15 | Outlook |
| Microsoft Outlook16 | Outlook |
| Microsoft Outlook17 | Outlook |
| Microsoft Outlook18 | Outlook |
| Microsoft Outlook19 | Outlook |
| Markdown1 | Markdown |
| varEmal1 | 数据设置 |
| Microsoft Outlook20 | Outlook |
| Microsoft Outlook21 | Outlook |
| Filter1 | 过滤器 |
| If1 | IF 判断 |
| Microsoft Outlook22 | Outlook |
| Catch Errors1 | 数据设置 |
| varJSON1 | 数据设置 |
| Microsoft Outlook23 | Outlook |
| varID & Category1 | 数据设置 |
| Microsoft Outlook Move Message1 | Outlook |
| AI Agent1 | AI Agent |
| Merge1 | 数据合并 |
| Switch1 | Switch 路由 |



## 功能说明

邮件自动化处理，AI 分类整理或。

定时触发、手动触发，通过 工作流编排 实现自动化。

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

- 节点总数：26
- 触发方式：手动触发

## 触发方式
- When clicking ‘Test workflow’ 触发

## 统计
- 节点总数：26
- 触发节点：1
- 处理节点：12
- 输出节点：13
- 分类：workflow-automation
