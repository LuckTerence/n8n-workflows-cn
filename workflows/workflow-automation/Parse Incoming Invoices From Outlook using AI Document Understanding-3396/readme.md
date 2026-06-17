## 简介
**Parse Incoming Invoices From Outlook using AI Document Understanding**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3396

---

# Parse Incoming Invoices From Outlook using AI Document Understanding


## 节点清单

| 节点 | 类型 |
|------|------|
| Split Attachments | Code |
| Download Attachments | Outlook |
| Parse Output | 数据设置 |
| For Each Message | 分批处理 |
| Message Ref | 空操作 |
| Message Classifier | 文本分类器 |
| Extract from File | 从文件提取 |
| Markdown | Markdown |
| Empty Response | 数据设置 |
| Wait | 等待 |
| Filter Invoices | 过滤器 |
| Has Invoice? | IF 判断 |
| Schedule Trigger | 定时触发器 |
| Get Recent Messages | Outlook |
| Model | OpenAI Chat Model |
| Microsoft Excel 365 | microsoftExcel |
| Invoice Classifier With Gemini 2.0 | HTTP Request |
| File-Based OCR with Gemini 2.0 | HTTP Request |



## 功能说明

AI 语音处理工作流，语音合成或转录，定时执行。

定时触发，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com
- 通义万相 API Key → https://dashscope.aliyun.com

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：18
- 触发方式：定时触发

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：18
- 触发节点：1
- 处理节点：13
- 输出节点：4
- 分类：workflow-automation
