## 简介
**Automate Purchase Order Form Submissions from Outlook Excel Attachments with AI**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3545

---

# Automate Purchase Order Form Submissions from Outlook Excel Attachments with AI


## 节点清单

| 节点 | 类型 |
|------|------|
| Extract Purchase Order Details | 信息提取器 |
| Is Excel Document? | IF 判断 |
| Run Checks | 数据设置 |
| Is Valid Purchase Order? | IF 判断 |
| Extract from File | 从文件提取 |
| XLSX to Markdown Table | Code |
| OpenAI Chat Model | OpenAI Chat Model |
| Reply Invalid Format | Outlook |
| Outlook Trigger | microsoftOutlookTrigger |
| Reply Rejection | Outlook |
| Reply Accepted | Outlook |
| Do Something with Purchase Order | 空操作 |
| Fix Excel Dates | 数据设置 |
| Is Submitting a Purchase Order? | 文本分类器 |
| Do Nothing | 空操作 |
| OpenAI Chat Model1 | OpenAI Chat Model |



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

- 节点总数：16
- 触发方式：手动或子流程调用

## 触发方式
- Outlook Trigger 触发

## 统计
- 节点总数：16
- 触发节点：1
- 处理节点：12
- 输出节点：3
- 分类：workflow-automation
