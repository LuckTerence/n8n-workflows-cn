## 简介
**Calculate Embodied Carbon (CO2) for Revit-IFC Models using AI Classification**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/7653

---

# Calculate Embodied Carbon (CO2) for Revit-IFC Models using AI Classification


## 节点清单

| 节点 | 类型 |
|------|------|
| Find Category Fields1 | Code |
| Apply Classification to Groups1 | Code |
| Non-Building Elements Output1 | 数据设置 |
| Extract Headers and Data1 | Code |
| AI Analyze All Headers1 | OpenAI |
| Process AI Response1 | Code |
| Group Data with AI Rules1 | Code |
| AI Classify Categories1 | OpenAI |
| Is Building Element1 | IF 判断 |
| Check If All Batches Done | IF 判断 |
| Collect All Results | Code |
| Process in Batches1 | 分批处理 |
| Clean Empty Values1 | Code |
| AI Agent Enhanced | AI Agent |
| Accumulate Results | Code |
| Anthropic Chat Model1 | OpenAI Chat Model |
| Calculate Project Totals4 | Code |
| Enhance Excel Output | Code |
| Prepare Excel Data | Code |
| Create Excel File | 电子表格文件 |
| Prepare Enhanced Prompts | Code |
| Parse Enhanced Response | Code |
| Read Excel File | 读取二进制文件 |
| Parse Excel | 电子表格文件 |
| Setup - Define file paths | 数据设置 |
| Create - Excel filename | 数据设置 |
| Check - Does Excel file exist? | 读取二进制文件 |
| If - File exists? | IF 判断 |
| Extract - Run converter | 执行命令 |
| Info - Skip conversion | 数据设置 |
| Check - Did extraction succeed? | IF 判断 |
| Error - Show what went wrong | 数据设置 |
| Set xlsx_filename after success | 数据设置 |
| Merge - Continue workflow | 数据合并 |
| Set Parameters | 数据设置 |
| When clicking ‘Execute workflow’ | 手动触发 |
| Prepare HTML Path | Code |
| Write HTML to Project Folder | 写入二进制文件 |
| Open HTML in Browser | 执行命令 |
| Prepare Excel Path | Code |
| Write Excel to Project Folder | 写入二进制文件 |
| Generate HTML Report | Code |
| HTML to Binary | Code |
| OpenAI Chat Model | OpenAI Chat Model |
| xAI Grok Chat Model | lmChatXAiGrok |
| On the standard 3D View | IF 判断 |
| Non-3D View Elements Output | 数据设置 |



## 功能说明

Calculate Embodied Carbon (CO2) for Revit-IFC Mode（AI 增强)手动触发，通过 n8n 内置节点实现自动化。

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

- 节点总数：47
- 触发方式：手动触发

## 触发方式
- When clicking ‘Execute workflow’ 触发

## 统计
- 节点总数：47
- 触发节点：1
- 处理节点：46
- 输出节点：0
- 分类：workflow-automation
