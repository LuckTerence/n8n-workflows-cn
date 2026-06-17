## 简介
**Automate purchase bill processing with AI OCR & QuickBooks integration**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/12013

---

# Automate purchase bill processing with AI OCR & QuickBooks integration


## 节点清单

| 节点 | 类型 |
|------|------|
| Split Items to Create | 数据拆分 |
| Create Items | HTTP Request |
| Merge Item Creation Paths | 数据合并 |
| Collect All Item Mappings | Code |
| Find Vendor | QuickBooks |
| Vendor Exists? | IF 判断 |
| Create Vendor | QuickBooks |
| Create Bill | HTTP Request |
| Need to Create Items? | IF 判断 |
| Get All QB Items | QuickBooks |
| Prepare Items to Check | Code |
| Extract Invoice Data | 信息提取器 |
| Clean Text | Code |
| Loop Over Invoices | 分批处理 |
| Convert to Separate Items | Code |
| Extract from PDF | 从文件提取 |
| Check Which Items to Create | Code |
| Build Bill Payload | Code |
| OpenRouter Chat Model | OpenRouter Chat Model |
| On bill submission | 表单触发器 |



## 功能说明

Automate purchase bill processing with AI OCR & Qu（AI 增强)表单提交触发，通过 HTTP API 实现自动化。

，通过 HTTP API 实现自动化。

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

- 节点总数：20
- 触发方式：表单提交触发

## 触发方式
- On bill submission 触发

## 统计
- 节点总数：20
- 触发节点：1
- 处理节点：17
- 输出节点：2
- 分类：workflow-automation
