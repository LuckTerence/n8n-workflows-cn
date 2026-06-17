## 简介
**Generate AI-Ready llms.txt Files from Screaming Frog Website Crawls**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Drive)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3219

---

# Generate AI-Ready llms.txt Files from Screaming Frog Website Crawls


## 节点清单

| 节点 | 类型 |
|------|------|
| Set useful fields | 数据设置 |
| Text Classifier | 文本分类器 |
| OpenAI Chat Model | OpenAI Chat Model |
| No Operation, do nothing | 空操作 |
| Filter URLs | 过滤器 |
| Summarize - Concatenate | 文本摘要 |
| Set Fields - llms.txt Content | 数据设置 |
| upload file anywhere | 空操作 |
| Set Field - llms.txt Row | 数据设置 |
| Form - Screaming frog internal_html.csv upload | 表单触发器 |
| Extract data from Screaming Frog file | 从文件提取 |
| Generate llms.txt file | 转换为文件 |



## 功能说明

数据采集工具，自动抓取网页或 API 数据（Ready)表单提交触发，通过 n8n 内置节点实现自动化。

，通过 工作流编排 实现自动化。

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

- 节点总数：12
- 触发方式：表单提交触发

## 触发方式
- Form - Screaming frog internal_html.csv upload 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：11
- 输出节点：0
- 分类：workflow-automation
