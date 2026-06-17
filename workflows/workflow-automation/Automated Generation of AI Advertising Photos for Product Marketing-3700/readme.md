## 简介
**Automated Generation of AI Advertising Photos for Product Marketing**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Google Drive)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3700

---

# Automated Generation of AI Advertising Photos for Product Marketing


## 节点清单

| 节点 | 类型 |
|------|------|
| OpenAI Chat Model | OpenAI Chat Model |
| Merge | 数据合并 |
| Read Image URLs | Google Sheets |
| Download Images | HTTP Request |
| Analyze Images | OpenAI |
| Product Photography Prompt | LLM Chain |
| Send Image with Prompt to OpenAI | HTTP Request |
| Convert Base64 to File | 转换为文件 |
| Upload to Drive | Google Drive |
| Insert Image URL in Table | Google Sheets |
| When clicking 'Test workflow' | 手动触发 |
| Convert to File | 转换为文件 |
| Generate Image | HTTP Request |



## 功能说明

AI 图像生成工作流，文生图或图生图。

手动触发，通过 HTTP API 实现自动化。

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

- 节点总数：13
- 触发方式：手动触发

## 触发方式
- When clicking 'Test workflow' 触发

## 统计
- 节点总数：13
- 触发节点：1
- 处理节点：9
- 输出节点：3
- 分类：workflow-automation
