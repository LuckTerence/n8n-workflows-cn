## 简介
**Effortless Job Hunting: Let this Automation Find Your Next Role**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Google Drive)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3051

---

# Effortless Job Hunting: Let this Automation Find Your Next Role


## 节点清单

| 节点 | 类型 |
|------|------|
| On clicking 'execute' | 手动触发 |
| Read PDF | readPDF |
| Download Resume (PDF File) | Google Drive |
| Filter Relevant Information | 数据拆分 |
| Analyse Resume | OpenAI |
| Find Suitable Job Offers | HTTP Request |
| Organise the Job Posts | 数据拆分 |
| Upload Job Posts Organised in a Spreadsheet | Google Sheets |



## 功能说明

联网搜索工具，AI 驱动的信息检索和分析。

手动触发，通过 HTTP API 实现自动化。

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

- 节点总数：8
- 触发方式：手动触发

## 触发方式
- On clicking 'execute' 触发

## 统计
- 节点总数：8
- 触发节点：1
- 处理节点：6
- 输出节点：1
- 分类：workflow-automation
