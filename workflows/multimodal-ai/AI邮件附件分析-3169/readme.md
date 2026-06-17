## 简介
**AI邮件附件分析**

分析PDF/图片附件保存到Drive+Telegram

> 分类：多模态 AI | 适配等级：A（需替换Google Sheets/Google Drive)（AI模型已替换为DeepSeek，部分边角节点可能仍需手动调整）
> 原始来源：https://n8nworkflows.xyz/workflows/3169

---

# AI邮件附件分析


## 节点清单

| 节点 | 类型 |
|------|------|
| Email Trigger (IMAP) | Email 读取 |
| DeepSeek R1 | OpenAI Chat Model |
| Email Summarization Chain | chainSummarization |
| Switch | Switch 路由 |
| Structured Output Parser | 结构化输出解析器 |
| Split Out | 数据拆分 |
| Aggregate | 数据聚合 |
| OpenRouter Chat Model1 | OpenRouter Chat Model |
| Contain attachments? | IF 判断 |
| Get PDF and images attachments | Code |
| Extract from PDF | 从文件提取 |
| PDF Analyzer | LLM Chain |
| Save summary PDF | Google Sheets |
| All summaries | 数据合并 |
| Map image summaries | 数据设置 |
| Upload attachments | Google Drive |
| Email summary | 数据设置 |
| Send final summary | Telegram |
| Create final summary | LLM Chain |
| Save summary image | Google Sheets |
| Save summary text | Google Sheets |
| Convert text | Markdown |
| Gemini 2.0 Flash | OpenRouter Chat Model |
| Parsing | Code |
| Analyze image | OpenAI |



## 功能说明

邮件自动化处理，AI 分类整理或。

定时触发、手动触发，通过 Telegram 通知 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com
- Telegram Bot Token → @BotFather 创建
- 邮箱 SMTP/IMAP 账号密码
- 通义万相 API Key → https://dashscope.aliyun.com

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：25
- 触发方式：手动或子流程调用

## 触发方式
- 手动触发

## 统计
- 节点总数：25
- 触发节点：0
- 处理节点：23
- 输出节点：2
- 分类：multimodal-ai
