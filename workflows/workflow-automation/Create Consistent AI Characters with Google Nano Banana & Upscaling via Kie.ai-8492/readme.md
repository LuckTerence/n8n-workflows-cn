## 简介
**Create Consistent AI Characters with Google Nano Banana & Upscaling via Kie.ai**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Google Drive/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/8492

---

# Create Consistent AI Characters with Google Nano Banana & Upscaling via Kie.ai


## 节点清单

| 节点 | 类型 |
|------|------|
| Poll Task | HTTP Request |
| Set TaskId | 数据设置 |
| Create Task (no callback) | HTTP Request |
| When clicking ‘Execute workflow’ | 手动触发 |
| Switch | Switch 路由 |
| Create folder | Google Drive |
| Edit Fields | 数据设置 |
| Add Fields | Google Sheets |
| Create spreadsheet | Google Sheets |
| Move Sheet | Google Drive |
| Update Image Status | Google Sheets |
| Wait 1 Min | 等待 |
| Story Status Update | Google Sheets |
| Code1 | Code |
| Json parser4 | 结构化输出解析器 |
| OpenAI Chat Model3 | OpenAI Chat Model |
| Story Creator Agent | LLM Chain |
| Folder Name | Code |
| Upscale Image | HTTP Request |
| Wait 1 Min1 | 等待 |
| Switch1 | Switch 路由 |
| Set TaskId for upscale | 数据设置 |
| Get Upscaled Image | HTTP Request |
| Get ResultUrls | Code |
| Get ResultUrls from UpScale | Code |
| Upload file | Google Drive |
| Move Images | Google Drive |
| Get Binary | HTTP Request |



## 功能说明

Create Consistent AI Characters with Google Nano B（AI 增强)手动触发，通过 HTTP API 实现自动化。

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

- 节点总数：28
- 触发方式：手动触发

## 触发方式
- When clicking ‘Execute workflow’ 触发

## 统计
- 节点总数：28
- 触发节点：1
- 处理节点：22
- 输出节点：5
- 分类：workflow-automation
