## 简介
**Daily Podcast Summary**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2433

---

# Daily Podcast Summary


## 节点清单

| 节点 | 类型 |
|------|------|
| Gmail | Email 发送 |
| TaddyTopDaily | HTTP Request |
| Genre | 数据设置 |
| Split Out | 数据拆分 |
| Whisper Transcribe Audio | HTTP Request |
| Final Data | 数据设置 |
| Merge Results | Code |
| HTML | HTML |
| Summarize Podcast | OpenAI |
| Schedule | 定时触发器 |
| Request Audio Crop | HTTP Request |
| Get Download Link | HTTP Request |
| Download Cut MP3 | HTTP Request |
| Download Podcast | HTTP Request |
| Wait | 等待 |
| If Downloads Ready | IF 判断 |



## 功能说明

AI 内容摘要工具，自动提炼长文关键信息，定时执行。

定时触发，通过 邮箱 + HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com
- 邮箱 SMTP/IMAP 账号密码
- 通义万相 API Key → https://dashscope.aliyun.com

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：16
- 触发方式：定时触发

## 触发方式
- Schedule 触发

## 统计
- 节点总数：16
- 触发节点：1
- 处理节点：8
- 输出节点：7
- 分类：workflow-automation
